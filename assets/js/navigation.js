(function () {
  const header = document.querySelector("[data-site-header]");
  if (!header) {
    return;
  }

  const toggle = header.querySelector("[data-nav-toggle]");
  const menu = header.querySelector("[data-nav-menu]");
  if (!toggle || !menu) {
    return;
  }

  const closeMenu = () => {
    header.classList.remove("is-nav-open");
    toggle.setAttribute("aria-expanded", "false");
  };

  const openMenu = () => {
    header.classList.add("is-nav-open");
    toggle.setAttribute("aria-expanded", "true");
  };

  header.dataset.navReady = "true";

  toggle.addEventListener("click", () => {
    if (header.classList.contains("is-nav-open")) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  menu.addEventListener("click", (event) => {
    if (event.target instanceof Element && event.target.closest("a")) {
      closeMenu();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMenu();
    }
  });

  document.addEventListener("click", (event) => {
    if (!header.contains(event.target)) {
      closeMenu();
    }
  });
})();
