/* Прячем стандартную мышь, чтобы она не мешала визуалу */
html, body, a, button, .card, .part, select, input {
    cursor: none !important;
}

.cursor-glow {
    position: fixed;
    top: 0;
    left: 0;
    width: 14px;
    height: 14px;
    background: #2563eb; /* Тот самый синий */
    border-radius: 50%;
    pointer-events: none;
    z-index: 9999999;
    will-change: transform;
    box-shadow: 0 0 10px rgba(37, 99, 235, 0.8);
}

/* Ореол синего света */
.cursor-glow::before {
    content: "";
    position: absolute;
    inset: -20px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(37, 99, 235, 0.4) 0%, transparent 70%);
    filter: blur(10px);
    z-index: -1;
    animation: pulseLoop 2s infinite ease-in-out;
}

@keyframes pulseLoop {
    0% { transform: scale(1); opacity: 0.6; }
    50% { transform: scale(1.4); opacity: 0.3; }
    100% { transform: scale(1); opacity: 0.6; }
}
.cursor-glow {
    /* ... твои остальные стили ... */
    opacity: 0; /* Скрываем по умолчанию */
    transition: opacity 0.3s ease, width 0.2s, height 0.2s; /* Плавное появление */
}