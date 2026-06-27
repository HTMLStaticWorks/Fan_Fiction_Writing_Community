// Dashboard specific scripts
document.addEventListener('DOMContentLoaded', () => {
  // Toggle Sidebar
  const sidebarToggle = document.getElementById('sidebarToggle');
  const sidebar = document.getElementById('dashboardSidebar');
  
  if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener('click', () => {
      sidebar.classList.toggle('show');
    });
  }
  
  // Dummy Chart Initialization (Requires Chart.js)
  const ctx = document.getElementById('statsChart');
  if (ctx && typeof Chart !== 'undefined') {
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
          label: 'Story Views',
          data: [1200, 1900, 3000, 5000, 2000, 3000],
          borderColor: '#6a1b9a',
          tension: 0.1
        }]
      }
    });
  }
});
