let isTransitioning = false;

// =========================
// PAGE TRANSITIONS FIXED
// =========================

document.addEventListener("click", (e) => {

    const link = e.target.closest("a");
    if (!link) return;

    const href = link.getAttribute("href");

    if (!href || href.startsWith("#") || href.startsWith("http") || href.startsWith("mailto:")) return;

    e.preventDefault();

    if (isTransitioning) return;
    isTransitioning = true;

    document.body.classList.add("fade-out");

    setTimeout(() => {
        window.location.href = href;
    }, 300);
});

// =========================
// FIX BACK/FORWARD CACHE
// =========================

window.addEventListener("pageshow", (e) => {
    document.body.classList.remove("fade-out");
    isTransitioning = false;
});

window.addEventListener("pageshow", (e) => {
    document.body.classList.remove("fade-out");
    isTransitioning = false;
});