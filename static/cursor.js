document.addEventListener("DOMContentLoaded", () => {
    const cursor = document.querySelector(".cursor-glow");
    if (!cursor) return;

    let x = 0, y = 0;
    let fx = 0, fy = 0;
    let scale = 1;
    let initialized = false;

    // Следим за реальными координатами мыши
    document.addEventListener("mousemove", (e) => {
        x = e.clientX;
        y = e.clientY;

        if (!initialized) {
            cursor.style.opacity = "1";
            fx = x;
            fy = y;
            initialized = true;
        }
    });

    function animate() {
        // Плавное следование за курсором без привязки к элементам
        fx += (x - fx) * 0.15;
        fy += (y - fy) * 0.15;

        cursor.style.transform = `translate(${fx}px, ${fy}px) translate(-50%, -50%) scale(${scale})`;

        requestAnimationFrame(animate);
    }

    animate();

    // Hover эффект: только увеличение масштаба
    const interactiveTags = "button, .card, .part, a, select, .close-btn, .build-btn";

    document.addEventListener("mouseover", (e) => {
        if (e.target.closest(interactiveTags)) {
            scale = 1.8; // Увеличиваем точку на ховере
        }
    });

    document.addEventListener("mouseout", (e) => {
        if (e.target.closest(interactiveTags)) {
            scale = 1; // Возвращаем в обычное состояние
        }
    });
});
document.addEventListener("mouseover", (e) => {
    if (e.target.closest(".config-box")) return;

    if (e.target.closest(interactiveTags)) {
        scale = 1.8;
    }
});

document.addEventListener("mouseout", (e) => {
    if (e.target.closest(".config-box")) return;

    if (e.target.closest(interactiveTags)) {
        scale = 1;
    }
});