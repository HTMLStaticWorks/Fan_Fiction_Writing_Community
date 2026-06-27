document.addEventListener('DOMContentLoaded', () => {
  // Theme Toggle
  const themeToggleBtn = document.getElementById('themeToggle');
  if (themeToggleBtn) {
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    
    themeToggleBtn.addEventListener('click', () => {
      let targetTheme = 'light';
      if (document.documentElement.getAttribute('data-theme') === 'light') {
        targetTheme = 'dark';
      }
      document.documentElement.setAttribute('data-theme', targetTheme);
      localStorage.setItem('theme', targetTheme);
    });
  }

  // RTL Toggle
  const rtlToggleBtn = document.getElementById('rtlToggle');
  if (rtlToggleBtn) {
    const currentDir = localStorage.getItem('dir') || 'ltr';
    document.documentElement.setAttribute('dir', currentDir);
    
    rtlToggleBtn.addEventListener('click', () => {
      let targetDir = 'ltr';
      if (document.documentElement.getAttribute('dir') === 'ltr') {
        targetDir = 'rtl';
      }
      document.documentElement.setAttribute('dir', targetDir);
      localStorage.setItem('dir', targetDir);
    });
  }

  // Back to Top
  const backToTopBtn = document.getElementById('backToTop');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        backToTopBtn.style.display = 'block';
      } else {
        backToTopBtn.style.display = 'none';
      }
    });
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Form Validation
  const forms = document.querySelectorAll('.needs-validation');
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add('was-validated');
    }, false);
  });
});
