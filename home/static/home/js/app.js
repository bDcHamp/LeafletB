(function(){
  // Highlight current page in navbar
  const path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('nav a').forEach(a => {
    if (a.getAttribute('href') === path) {
      a.setAttribute('aria-current', 'page');
    }
  });

  // Focus main for accessibility
  window.addEventListener('load', () => {
    const main = document.getElementById('main');
    if (main) {
      main.setAttribute('tabindex','-1');
      main.focus({preventScroll:true});
    }
  });
})();
