document.addEventListener('DOMContentLoaded', () => {
  // Sidebar toggle setup
  const toggleBtn = document.getElementById('tabToggle');
  const sidebar = document.getElementById('sidebar');
  const iconSpan = toggleBtn.querySelector('span.material-symbols-outlined');

  toggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('sidebar-expanded');

    // Update the icon based on sidebar state
    const isExpanded = sidebar.classList.contains('sidebar-expanded');
    iconSpan.textContent = isExpanded ? 'left_panel_close' : 'left_panel_open';
  });

  // History menu toggle setup
  const historyBtn = document.getElementById('history-button');
  const historyMenu = document.getElementById('history-menu');

  historyBtn.addEventListener('click', (event) => {
    event.stopPropagation(); // Prevent click from closing menu immediately
    
    // Close import menu if open
    importMenu.classList.add('hidden');
    ctaMenu.classList.add('hidden');
   
    // Toggle history menu
    historyMenu.classList.toggle('hidden');
  });

    // Import menu toggle setup
  const importBtn = document.getElementById('import-button');
  const importMenu = document.getElementById('import-menu');

  importBtn.addEventListener('click', (event) => {
    event.stopPropagation();
    historyMenu.classList.add('hidden');
    ctaMenu.classList.add('hidden');
    importMenu.classList.toggle('hidden');
  });

    // CTA menu toggle setup
  const ctaBtn = document.getElementById('cta-button');
  const ctaMenu = document.getElementById('cta-menu');

  ctaBtn.addEventListener('click', (event) => {
    event.stopPropagation();
    historyMenu.classList.add('hidden');
    importMenu.classList.add('hidden');
    ctaMenu.classList.toggle('hidden');
});

    // Close history menu when clicking outside
    document.addEventListener('click', (event) => {
      if (!historyMenu.contains(event.target) && !historyBtn.contains(event.target)) {
        historyMenu.classList.add('hidden');
      }
      if (!importMenu.contains(event.target) && !importBtn.contains(event.target)) {
        importMenu.classList.add('hidden');
      }
      if (!ctaMenu.contains(event.target) && !ctaBtn.contains(event.target)) {
        ctaMenu.classList.add('hidden');
      }
    });
});
