




document.addEventListener('DOMContentLoaded', function() {
    const html = document.documentElement;
    const btn = document.getElementById('theme-toggle');
    const icon = document.querySelector('.theme-icon');
    
    // Load saved theme or default to light
    const savedTheme = localStorage.getItem('theme') || 'light';
    html.setAttribute('data-theme', savedTheme);
    updateIcon(savedTheme);
    
    // Toggle theme on click
    btn.addEventListener('click', function() {
        const current = html.getAttribute('data-theme');
        const newTheme = current === 'dark' ? 'light' : 'dark';
        
        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateIcon(newTheme);
        
        // Rotate animation
        btn.classList.add('theme-toggle-rotate');
        setTimeout(() => btn.classList.remove('theme-toggle-rotate'), 300);
    });
    
    // Update icon
    function updateIcon(theme) {
        if (theme === 'dark') {
            icon.textContent = '☀️';
            btn.title = 'Switch to light mode';
        } else {
            icon.textContent = '🌙';
            btn.title = 'Switch to dark mode';
        }
    }
});