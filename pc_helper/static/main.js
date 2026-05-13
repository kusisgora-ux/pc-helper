const build = {
    cpu: null, gpu: null, ram: null, mb: null,
    psu: null, ssd: null, cooler: null, case: null
};

function selectPart(domEl) {
    const d = domEl.dataset;
    const type = d.type;

    const parentCardContent = domEl.closest('.card-content');
    if (parentCardContent) {
        parentCardContent.querySelectorAll('.part').forEach(p => p.classList.remove('ok', 'bad'));
    }

    build[type] = {
        name: d.name,
        price: Number(d.price),
        url: d.url || "#",
        socket: d.socket || null,
        ddr: d.ddr || null, // Сюда теперь попадет значение из базы
        watt: Number(d.watt || d.power || 0)
    };

    domEl.classList.add('ok');

    const card = domEl.closest('.card');
    setTimeout(() => {
        if (card) card.classList.add('collapsed');
    }, 300);

    updateUI(type, d.name, build[type].url);
    calculatePrice();
    checkCompatibility();
}

function checkCompatibility() {
    const warnEl = document.getElementById("warn");
    let errors = [];

    // 1. Проверка Сокета
    if (build.cpu && build.mb) {
        const cpuSock = String(build.cpu.socket).toUpperCase().trim();
        const mbSock = String(build.mb.socket).toUpperCase().trim();
        if (cpuSock !== mbSock) {
            errors.push(`Сокеты не совпадают: CPU (${cpuSock}) и MB (${mbSock})`);
        }
    }

    // 2. Проверка DDR (Теперь точно заработает)
    if (build.ram && build.mb) {
        const ramType = String(build.ram.ddr).toUpperCase().trim();
        const mbType = String(build.mb.ddr).toUpperCase().trim();

        if (ramType !== mbType) {
            errors.push(`Конфликт памяти: Мать поддерживает ${mbType}, а выбрана ${ramType}`);
        }
    }

    // 3. Проверка БП
    if (build.psu) {
        const consumption = (build.cpu?.watt || 0) + (build.gpu?.watt || 0) + 150;
        if (build.psu.watt < consumption) {
            errors.push(`Слабый БП: нужно минимум ${consumption}W`);
        }
    }

    // Рендер ошибок
    if (errors.length > 0) {
        warnEl.innerHTML = "❌ " + errors.join("<br>");
        warnEl.style.color = "#ef4444";
    } else if (build.cpu || build.mb || build.ram) {
        warnEl.innerHTML = "✅ Сборка совместима";
        warnEl.style.color = "#10b981";
    }
}

// Функции UI и событий остаются прежними
function updateUI(type, name, url) {
    const el = document.getElementById("sel-" + type);
    if (el) el.innerHTML = `<a href="${url}" target="_blank" style="color:#2563eb;text-decoration:none;font-weight:bold;">${name}</a>`;
}

function calculatePrice() {
    let total = 0;
    for (let key in build) { if (build[key]) total += build[key].price; }
    document.getElementById("total-price").innerText = total.toLocaleString() + " ₽";
}

document.addEventListener("click", (e) => {
    const part = e.target.closest(".part");
    if (part) selectPart(part);
});
function toggleTheme() {
    const body = document.body;
    const icon = document.getElementById('theme-icon');

    body.classList.toggle('dark-theme');

    if (body.classList.contains('dark-theme')) {
        icon.innerText = '☀️'; // Солнце для возврата к светлой
        localStorage.setItem('theme', 'dark');
    } else {
        icon.innerText = '🌙'; // Луна для перехода в темную
        localStorage.setItem('theme', 'light');
    }
}

// Проверка сохраненной темы при загрузке
window.onload = () => {
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-theme');
        document.getElementById('theme-icon').innerText = '☀️';
    }
};