/* Shared interactions. All article content remains readable without JavaScript. */
(() => {
  "use strict";
  document.body.classList.add("enhanced");
  const menuButton = document.querySelector(".menu-toggle");
  const navigation = document.querySelector(".site-nav");
  function closeMenu() {
    navigation.classList.remove("is-open");
    menuButton.setAttribute("aria-expanded", "false");
    menuButton.textContent = "目錄 ☰";
  }
  menuButton.addEventListener("click", () => {
    const open = menuButton.getAttribute("aria-expanded") !== "true";
    navigation.classList.toggle("is-open", open);
    menuButton.setAttribute("aria-expanded", String(open));
    menuButton.textContent = open ? "收起 ×" : "目錄 ☰";
  });
  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && menuButton.getAttribute("aria-expanded") === "true") {
      closeMenu();
      menuButton.focus();
    }
  });
  window.matchMedia("(max-width: 760px)").addEventListener("change", closeMenu);

  const catalogGrid = document.querySelector("#catalog-grid");
  if (!catalogGrid) return;
  const catalog = window.ARCHIVE_CATALOG || [];
  const cards = Array.from(catalogGrid.querySelectorAll(".catalog-card"));
  const search = document.querySelector("#archive-search");
  const filters = Array.from(document.querySelectorAll(".filter-button"));
  const count = document.querySelector("#result-count");
  const empty = document.querySelector("#empty-state");
  const storageStatus = document.querySelector("#storage-status");
  const storageKey = "xuantian-bookmarks-v1";
  const validIds = new Set(catalog.map(entry => entry.id));
  let bookmarks = new Set();
  let activeCategory = "all";
  let canPersist = true;
  try {
    const saved = JSON.parse(localStorage.getItem(storageKey) || "[]");
    if (Array.isArray(saved)) bookmarks = new Set(saved.filter(id => validIds.has(id)));
  } catch {
    canPersist = false;
    storageStatus.textContent = "此瀏覽器無法讀取收藏。你仍可在本次瀏覽暫存收藏。";
  }

  function updateCatalog() {
    const query = search.value.trim().toLocaleLowerCase("zh-Hant");
    let visibleCount = 0;
    cards.forEach(card => {
      const entry = catalog.find(item => item.id === card.dataset.id);
      if (!entry) return;
      const text = [entry.title, entry.summary, ...entry.keywords].join(" ").toLocaleLowerCase("zh-Hant");
      const inCategory = activeCategory === "all" || entry.category === activeCategory ||
        (activeCategory === "saved" && bookmarks.has(entry.id));
      const visible = inCategory && text.includes(query);
      card.hidden = !visible;
      if (visible) visibleCount += 1;
    });
    count.textContent = `共 ${visibleCount} 卷典籍`;
    empty.hidden = visibleCount !== 0;
    empty.textContent = activeCategory === "saved" && !query
      ? "尚無收藏。點選典籍右上角的「收藏」，留待下次細讀。"
      : "未找到符合的典籍，試試「雷」「劍」或切換至全部典籍。";
  }

  function syncBookmarkButtons() {
    cards.forEach(card => {
      const button = card.querySelector(".save-button");
      const saved = bookmarks.has(card.dataset.id);
      button.setAttribute("aria-pressed", String(saved));
      button.textContent = saved ? "已收藏 ✓" : "收藏 ＋";
    });
  }

  cards.forEach(card => {
    const button = card.querySelector(".save-button");
    button.hidden = false;
    button.addEventListener("click", () => {
      const id = card.dataset.id;
      if (bookmarks.has(id)) bookmarks.delete(id);
      else bookmarks.add(id);
      try {
        localStorage.setItem(storageKey, JSON.stringify([...bookmarks]));
        canPersist = true;
      } catch {
        canPersist = false;
      }
      storageStatus.textContent = canPersist
        ? "收藏已更新，儲存於此瀏覽器。"
        : "此瀏覽器無法儲存收藏，目前只在本次瀏覽有效。";
      syncBookmarkButtons();
      updateCatalog();
    });
  });
  filters.forEach(button => {
    button.addEventListener("click", () => {
      activeCategory = button.dataset.filter;
      filters.forEach(filter => filter.setAttribute("aria-pressed", String(filter === button)));
      updateCatalog();
    });
  });
  search.addEventListener("input", updateCatalog);
  document.querySelector("#clear-search").addEventListener("click", () => {
    search.value = "";
    updateCatalog();
    search.focus();
  });
  document.querySelector("#search-tools").hidden = false;
  syncBookmarkButtons();
  updateCatalog();
})();
