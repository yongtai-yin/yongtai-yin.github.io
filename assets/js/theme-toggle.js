document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('theme-toggle');
    if (!toggleButton) {
        return;
    }

    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
    const currentTheme = localStorage.getItem('theme');

    const applyTheme = (theme) => {
        document.documentElement.setAttribute('data-theme', theme);
        if (theme === 'dark') {
            toggleButton.innerHTML = '<i class="fas fa-sun" aria-hidden="true"></i>';
            toggleButton.setAttribute('aria-label', 'Switch to light mode');
        } else {
            toggleButton.innerHTML = '<i class="fas fa-moon" aria-hidden="true"></i>';
            toggleButton.setAttribute('aria-label', 'Switch to dark mode');
        }
    };

    const initialTheme = currentTheme || (prefersDarkScheme.matches ? 'dark' : 'light');
    applyTheme(initialTheme);

    toggleButton.addEventListener('click', () => {
        const theme = document.documentElement.getAttribute('data-theme');
        if (theme === 'dark') {
            localStorage.setItem('theme', 'light');
            applyTheme('light');
        } else {
            localStorage.setItem('theme', 'dark');
            applyTheme('dark');
        }
    });
});
