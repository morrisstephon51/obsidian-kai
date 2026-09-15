// Elite Career Compass - site behavior
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('nav.primary');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Pre-select the vertical on the Apply form when linked as /apply/?vertical=healthcare
  var select = document.querySelector('select[name="vertical"]');
  if (select) {
    try {
      var v = new URLSearchParams(window.location.search).get('vertical');
      if (v) {
        for (var i = 0; i < select.options.length; i++) {
          if (select.options[i].value === v) { select.selectedIndex = i; break; }
        }
      }
    } catch (e) { /* older browsers: form still works without preselect */ }
  }
})();
