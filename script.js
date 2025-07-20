window.addEventListener('DOMContentLoaded', () => {
  const icons = document.querySelectorAll('.bg-icon');
  icons.forEach(icon => {
    const x = Math.random() * window.innerWidth;
    const y = Math.random() * window.innerHeight;
    const duration = 20 + Math.random() * 20;
    icon.style.left = `${x}px`;
    icon.style.top = `${y}px`;
    icon.style.animationDuration = `${duration}s`;
  });
});
