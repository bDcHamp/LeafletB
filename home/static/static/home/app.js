(function () {
  // --------------------------------------------------------
  // Highlight the current page link in the navbar
  // --------------------------------------------------------
  const path = location.pathname.split('/').filter(Boolean).pop() || '';
  document.querySelectorAll('nav a').forEach((a) => {
    const href = a.getAttribute('href');
    if (href && path && href.includes(path)) {
      a.setAttribute('aria-current', 'page');
    }
  });

  // --------------------------------------------------------
  // Accessibility: focus the <main> element on page load
  // --------------------------------------------------------
  window.addEventListener('load', () => {
    const main = document.getElementById('main');
    if (main) {
      main.setAttribute('tabindex', '-1');
      main.focus({ preventScroll: true });
    }
  });
})();
