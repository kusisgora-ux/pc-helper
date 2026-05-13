{% extends "base.html" %}

{% block content %}

<h1 class="section-title">Обучение сборке ПК</h1>

<div class="catalog-buttons">

<button onclick="showLevel('beginner', event)">Новичок</button>
<button onclick="showLevel('intermediate', event)">Любитель</button>
<button onclick="showLevel('pro', event)">Профессионал</button>

</div>
<div class="cursor-glow"></div>
<div class="orb"></div>
<!-- ===================== -->
<!-- 🟢 BEGINNER -->
<!-- ===================== -->

<div id="beginner" class="catalog-section">

<h2>🟢 Новичок</h2>

<div class="cards">

<div class="card" onclick="openArticle('cpu', 'Процессор (CPU)')">

<div class="card-top">
    <div class="card-title">
        <h2>Процессор</h2>
        <span id="status-cpu" class="status">❌</span>
    </div>
</div>

<p>Главный вычислительный компонент ПК</p>


</div>

<div class="card" onclick="openArticle('gpu', 'Видеокарта (GPU)')">
<div class="card-header">
<h2>Видеокарта</h2>
<span id="status-gpu">❌</span>
</div>
<p>Отвечает за графику и игры</p>
</div>

<div class="card" onclick="openArticle('ram', 'Оперативная память')">
<div class="card-header">
<h2>Оперативная память</h2>
<span id="status-ram">❌</span>
</div>
<p>Временное хранилище данных</p>
</div>

<div class="card" onclick="openArticle('storage', 'SSD / HDD')">
<div class="card-header">
<h2>Накопители</h2>
<span id="status-storage">❌</span>
</div>
<p>Хранение системы и файлов</p>
</div>

<div class="card" onclick="openArticle('mb', 'Материнская плата')">
<div class="card-header">
<h2>Материнская плата</h2>
<span id="status-mb">❌</span>
</div>
<p>Связывает все компоненты</p>
</div>

<div class="card" onclick="openArticle('psu', 'Блок питания')">
<div class="card-header">
<h2>Блок питания</h2>
<span id="status-psu">❌</span>
</div>
<p>Питание системы</p>
</div>

</div>
</div>

<!-- ===================== -->
<!-- 🟡 INTERMEDIATE -->
<!-- ===================== -->

<div id="intermediate" class="catalog-section hidden">

<h2>🟡 Любитель</h2>

<div class="cards">

<div class="card" onclick="openArticle('compatibility', 'Совместимость')">
<div class="card-header">
<h2>Совместимость</h2>
<span id="status-compatibility">❌</span>
</div>
<p>Как подбирать железо</p>
</div>

<div class="card" onclick="openArticle('build', 'Сборка ПК')">
<div class="card-header">
<h2>Сборка ПК</h2>
<span id="status-build">❌</span>
</div>
<p>Пошаговая сборка</p>
</div>

<div class="card" onclick="openArticle('cooling', 'Охлаждение')">
<div class="card-header">
<h2>Охлаждение</h2>
<span id="status-cooling">❌</span>
</div>
<p>Температуры и airflow</p>
</div>

    <div class="card" onclick="openArticle('thermal', 'Термопасты и температуры')">
    <div class="card-header">
        <h2>Термопасты</h2>
        <span id="status-thermal">❌</span>
    </div>
    <p>Как охлаждать CPU и GPU правильно</p>
</div>

<div class="card" onclick="openArticle('ssd_types', 'Типы SSD')">
    <div class="card-header">
        <h2>SSD типы</h2>
        <span id="status-ssd_types">❌</span>
    </div>
    <p>SATA, NVMe, M.2 — разница</p>
</div>

<div class="card" onclick="openArticle('pc_assembly_rules', 'Правила сборки ПК')">
    <div class="card-header">
        <h2>Правила сборки</h2>
        <span id="status-pc_assembly_rules">❌</span>
    </div>
    <p>Ошибки новичков и как их избежать</p>
</div>

<div class="card" onclick="openArticle('airflow', 'Airflow в корпусе')">
    <div class="card-header">
        <h2>Airflow</h2>
        <span id="status-airflow">❌</span>
    </div>
    <p>Как правильно охлаждать корпус</p>
</div>

</div>
</div>

<!-- ===================== -->
<!-- 🔴 PRO -->
<!-- ===================== -->

<div id="pro" class="catalog-section hidden">

<h2>🔴 Профессионал</h2>

<div class="cards">

<div class="card" onclick="openArticle('bios', 'BIOS / UEFI')">
<div class="card-header">
<h2>BIOS</h2>
<span id="status-bios">❌</span>
</div>
<p>Настройка системы</p>
</div>

<div class="card" onclick="openArticle('overclock', 'Разгон CPU')">
<div class="card-header">
<h2>Разгон CPU</h2>
<span id="status-overclock">❌</span>
</div>
<p>Overclocking</p>
</div>

<div class="card" onclick="openArticle('diagnostic', 'Диагностика')">
<div class="card-header">
<h2>Диагностика</h2>
<span id="status-diagnostic">❌</span>
</div>
<p>Поиск неисправностей</p>
</div>
    <div class="card" onclick="openArticle('undervolting', 'Undervolting CPU/GPU')">
    <div class="card-header">
        <h2>Undervolting</h2>
        <span id="status-undervolting">❌</span>
    </div>
    <p>Снижение температуры без потери FPS</p>
</div>

<div class="card" onclick="openArticle('ram_tuning', 'Тонкая настройка RAM')">
    <div class="card-header">
        <h2>RAM Tuning</h2>
        <span id="status-ram_tuning">❌</span>
    </div>
    <p>XMP, тайминги, разгон памяти</p>
</div>

<div class="card" onclick="openArticle('vrm', 'VRM и питание CPU')">
    <div class="card-header">
        <h2>VRM</h2>
        <span id="status-vrm">❌</span>
    </div>
    <p>Почему важно питание процессора</p>
</div>

<div class="card" onclick="openArticle('benchmark', 'Бенчмарки и тесты')">
    <div class="card-header">
        <h2>Бенчмарки</h2>
        <span id="status-benchmark">❌</span>
    </div>
    <p>Как тестировать производительность</p>
</div>

</div>
</div>

<!-- ===================== -->
<!-- 🌑 MODAL -->
<!-- ===================== -->
<!-- ===================== -->
<!-- 🌑 MODAL -->
<!-- ===================== -->

<div id="modal" class="modal hidden">

    <div class="modal-content">

        <!-- HEADER -->
        <div class="modal-header">

            <h2 id="modal-title"></h2>

            <span class="close-btn" onclick="closeArticle()">×</span>

        </div>

        <!-- CONTENT -->
        <div id="modal-body" class="article"></div>
        <!-- FOOTER -->
<div class="modal-footer">

    <button onclick="markDone()">
        ✓ Отметить как пройдено
    </button>

</div>
    </div>

</div>

<script>

function showLevel(level){

    document.querySelectorAll(".catalog-section").forEach(el=>{
        el.classList.add("hidden");
    });

    document.getElementById(level).classList.remove("hidden");

    document.querySelectorAll(".catalog-buttons button").forEach(btn=>{
        btn.classList.remove("active");
    });

    event.target.classList.add("active");
}

</script>
<!-- ===================== -->
<!-- SCRIPT -->
<!-- ===================== -->

<script>

let currentLesson = null;

/* открыть урок */
function openArticle(type, title) {

currentLesson = type;

const modal = document.getElementById("modal");
const body = document.getElementById("modal-body");
const titleEl = document.getElementById("modal-title");

titleEl.innerText = title;

let content = "";

/* ===== BEGINNER ===== */

if (type === "cpu") {

content = `
<h1>Процессор (CPU)</h1>

<p>
Процессор — это главный вычислительный компонент компьютера.
Именно CPU выполняет вычисления, обрабатывает команды системы,
управляет программами и взаимодействует со всеми комплектующими.
</p>

<h2>Что делает процессор</h2>

<ul>
<li>Выполняет вычисления</li>
<li>Обрабатывает данные</li>
<li>Запускает игры и программы</li>
<li>Управляет системой</li>
<li>Передает команды видеокарте и памяти</li>
</ul>

<h2>Главные характеристики</h2>

<ul>
<li><b>Ядра</b> — количество вычислительных блоков</li>
<li><b>Потоки</b> — количество одновременных задач</li>
<li><b>Частота</b> — скорость работы CPU</li>
<li><b>Кэш</b> — сверхбыстрая память процессора</li>
<li><b>TDP</b> — тепловыделение</li>
</ul>

<h2>Intel vs AMD</h2>

<p>
Intel традиционно сильнее в некоторых играх и стабильности,
AMD предлагает больше ядер за меньшую цену и лучше подходит
для многозадачности.
</p>

<h2>Для игр</h2>

<p>
Современным игровым ПК желательно иметь минимум 6 ядер и 12 потоков.
Оптимальные варианты:
Ryzen 5 / Ryzen 7 или Intel Core i5 / i7 последних поколений.
</p>

<h2>Важно помнить</h2>

<p>
Процессор должен подходить к сокету материнской платы.
Например:
AM4 ↔ Ryzen,
LGA1700 ↔ Intel 12/13/14 gen.
</p>
`;
}
if (type === "gpu") {
content = `
<h1>Видеокарта (GPU)</h1>

<p>
Видеокарта отвечает за обработку графики, рендеринг изображений,
игры, работу с видео и 3D-графикой.
Современные GPU используются не только в играх,
но и в нейросетях, монтаже и профессиональных задачах.
</p>

<h2>Основные задачи GPU</h2>

<ul>
<li>Обработка графики в играх</li>
<li>Рендеринг видео</li>
<li>Работа с 3D</li>
<li>Поддержка высоких разрешений</li>
<li>Ускорение программ</li>
</ul>

<h2>Главные характеристики</h2>

<ul>
<li><strong>VRAM</strong> — объём видеопамяти</li>
<li><strong>Частота GPU</strong> — скорость чипа</li>
<li><strong>TDP</strong> — энергопотребление</li>
<li><strong>Ray Tracing</strong> — трассировка лучей</li>
</ul>

<h2>NVIDIA vs AMD</h2>

<p>
NVIDIA обычно сильнее в трассировке лучей и рабочих задачах,
AMD предлагает больше производительности за меньшие деньги.
</p>

<h2>Для игр</h2>

<p>
Для Full HD обычно хватает 8GB VRAM.
Для 2K и 4K желательно 12–16GB видеопамяти.
</p>
`;
}

if (type === "storage") {

content = `
<h1>SSD и HDD</h1>

<p>
Накопители используются для хранения Windows,
игр, программ и файлов пользователя.
</p>

<h2>SSD</h2>

<p>
SSD намного быстрее HDD.
Система загружается за секунды,
игры и программы открываются быстрее.
</p>

<h2>HDD</h2>

<p>
HDD медленнее, но дешевле и подходит
для хранения больших объемов файлов.
</p>

<h2>Типы SSD</h2>

<ul>
<li>SATA SSD</li>
<li>M.2 NVMe</li>
<li>PCIe Gen4 / Gen5</li>
</ul>

<h2>Что выбрать</h2>

<p>
Для современного ПК рекомендуется SSD минимум на 500GB.
Лучший вариант — NVMe M.2.
</p>
`;
}
if (type === "storage") {

content = `
<h1>SSD и HDD</h1>

<p>
Накопители используются для хранения Windows,
игр, программ и файлов пользователя.
</p>

<h2>SSD</h2>

<p>
SSD намного быстрее HDD.
Система загружается за секунды,
игры и программы открываются быстрее.
</p>

<h2>HDD</h2>

<p>
HDD медленнее, но дешевле и подходит
для хранения больших объемов файлов.
</p>

<h2>Типы SSD</h2>

<ul>
<li>SATA SSD</li>
<li>M.2 NVMe</li>
<li>PCIe Gen4 / Gen5</li>
</ul>

<h2>Что выбрать</h2>

<p>
Для современного ПК рекомендуется SSD минимум на 500GB.
Лучший вариант — NVMe M.2.
</p>
`;
}

if (type === "mb") {

content = `
<h1>Материнская плата</h1>

<p>
Материнская плата соединяет все компоненты компьютера
в единую систему.
</p>

<h2>Что находится на плате</h2>

<ul>
<li>Сокет процессора</li>
<li>Слоты RAM</li>
<li>PCIe для видеокарты</li>
<li>M.2 для SSD</li>
<li>Питание CPU</li>
</ul>

<h2>Сокеты</h2>

<p>
AMD и Intel используют разные сокеты.
Процессор должен совпадать с сокетом платы.
</p>

<h2>Чипсет</h2>

<p>
Чипсет определяет возможности платы:
разгон, количество USB, PCIe и накопителей.
</p>

<h2>Форматы</h2>

<ul>
<li>ATX</li>
<li>Micro-ATX</li>
<li>Mini-ITX</li>
</ul>
`;
}

if (type === "psu") {

content = `
<h1>Блок питания</h1>

<p>
Блок питания обеспечивает электроэнергией
все комплектующие компьютера.
</p>

<h2>Почему важен БП</h2>

<ul>
<li>Стабильность системы</li>
<li>Защита комплектующих</li>
<li>Безопасность</li>
<li>Надежность работы</li>
</ul>

<h2>Мощность</h2>

<p>
Для игровых ПК обычно хватает 650–850W,
но мощные видеокарты требуют больше.
</p>

<h2>Сертификаты</h2>

<ul>
<li>80+ Bronze</li>
<li>80+ Gold</li>
<li>80+ Platinum</li>
</ul>

<h2>Важно</h2>

<p>
Дешевые блоки питания могут повредить комплектующие.
Экономить на БП не рекомендуется.
</p>
`;
}
/* ===== INTERMEDIATE ===== */

if (type === "compatibility") {

content = `
<h1>Совместимость комплектующих</h1>

<p>
При сборке ПК важно учитывать совместимость всех компонентов.
Даже мощные комплектующие не будут работать вместе,
если они несовместимы между собой.
</p>

<h2>Процессор и материнская плата</h2>

<p>
CPU должен подходить под сокет материнской платы.
Например:
AM4 ↔ Ryzen,
LGA1700 ↔ Intel 12/13/14 gen.
</p>

<h2>Оперативная память</h2>

<p>
Материнская плата должна поддерживать тип памяти:
DDR4 или DDR5.
Они физически несовместимы между собой.
</p>

<h2>Блок питания</h2>

<p>
БП должен обеспечивать достаточную мощность
для процессора и видеокарты.
</p>

<h2>Корпус</h2>

<p>
Некоторые видеокарты слишком длинные
для компактных корпусов.
</p>

<h2>Охлаждение</h2>

<p>
Кулер должен поддерживать сокет процессора
и помещаться в корпус.
</p>
`;
}

if (type === "build") {

content = `
<h1>Сборка компьютера</h1>

<p>
Сборка ПК — процесс установки и подключения
всех комплектующих в правильном порядке.
</p>

<h2>Этапы сборки</h2>

<ol>
<li>Установка процессора</li>
<li>Установка оперативной памяти</li>
<li>Монтаж SSD</li>
<li>Установка материнской платы</li>
<li>Подключение блока питания</li>
<li>Установка видеокарты</li>
<li>Подключение кабелей</li>
</ol>

<h2>Термопаста</h2>

<p>
Перед установкой кулера на процессор
нужно нанести термопасту.
Она улучшает передачу тепла.
</p>

<h2>Cable Management</h2>

<p>
Правильная укладка кабелей улучшает airflow
и делает сборку аккуратнее.
</p>

<h2>Первый запуск</h2>

<p>
После сборки проверь подключение питания,
RAM и видеокарты перед включением системы.
</p>
`;
}

if (type === "cooling") {

content = `
<h1>Охлаждение ПК</h1>

<p>
Охлаждение отвечает за температуру компонентов.
Высокие температуры снижают производительность
и срок службы комплектующих.
</p>

<h2>Типы охлаждения</h2>

<ul>
<li>Воздушное</li>
<li>Водяное (СЖО)</li>
</ul>

<h2>Airflow</h2>

<p>
Правильный airflow обеспечивает движение воздуха
через корпус.
Передние вентиляторы обычно вдувают воздух,
задние и верхние — выдувают.
</p>

<h2>Температуры</h2>

<ul>
<li>CPU: 60–85°C</li>
<li>GPU: 65–85°C</li>
</ul>

<h2>Термопаста</h2>

<p>
Со временем термопасту рекомендуется менять,
так как она высыхает.
</p>

<h2>Почему охлаждение важно</h2>

<p>
Перегрев может вызывать троттлинг,
фризы и выключение системы.
</p>
`;
}

if (type === "thermal") {
content = `
<h1>Термопаста и температуры</h1>

<p>
Термопаста — это теплопроводящий материал, который передаёт тепло от процессора к кулеру.
Без неё процессор может перегреваться даже при слабой нагрузке.
</p>

<h2>Зачем нужна термопаста</h2>
<ul>
<li>Улучшает теплопередачу</li>
<li>Снижает температуру CPU и GPU</li>
<li>Увеличивает стабильность системы</li>
</ul>

<h2>Температуры</h2>
<ul>
<li>40–60°C — норма в простое</li>
<li>70–85°C — нагрузка</li>
<li>90°C+ — перегрев</li>
</ul>

<h2>Ошибки</h2>
<p>
Слишком много термопасты ухудшает охлаждение так же, как и её отсутствие.
</p>
`;
}

if (type === "ssd_types") {
content = `
<h1>Типы SSD</h1>

<p>
SSD бывают разных типов и отличаются скоростью и подключением.
</p>

<h2>Основные типы</h2>
<ul>
<li><b>SATA SSD</b> — медленный, но дешёвый</li>
<li><b>M.2 SATA</b> — компактный формат</li>
<li><b>NVMe SSD</b> — самый быстрый вариант</li>
</ul>

<h2>Сравнение</h2>
<p>
NVMe может быть в 5–10 раз быстрее SATA SSD.
</p>

<h2>Вывод</h2>
<p>
Для игр и системы лучше использовать NVMe, а SATA — для хранения файлов.
</p>
`;
}

if (type === "pc_assembly_rules") {
content = `
<h1>Правила сборки ПК</h1>

<p>
Сборка ПК требует аккуратности и соблюдения базовых правил.
Ошибка может привести к повреждению компонентов.
</p>

<h2>Основные правила</h2>
<ul>
<li>Всегда отключай питание</li>
<li>Не применяй силу при установке</li>
<li>Проверяй совместимость деталей</li>
<li>Соблюдай антистатическую защиту</li>
</ul>

<h2>Частые ошибки</h2>
<ul>
<li>Неправильная установка RAM</li>
<li>Перепутанные кабели питания</li>
<li>Отсутствие термопасты</li>
</ul>
`;
}

if (type === "airflow") {
content = `
<h1>Airflow в корпусе</h1>

<p>
Airflow — это движение воздуха внутри корпуса, которое влияет на охлаждение всех компонентов.
</p>

<h2>Основные принципы</h2>
<ul>
<li>Холодный воздух заходит спереди</li>
<li>Горячий выходит сзади и сверху</li>
<li>Нужно балансировать вентиляторы</li>
</ul>

<h2>Плохой airflow</h2>
<p>
Приводит к перегреву GPU и CPU даже при мощном охлаждении.
</p>

<h2>Совет</h2>
<p>
Лучший вариант — 2 вентилятора на вход и 1–2 на выход.
</p>
`;
}

/* ===== PRO ===== */

if (type === "bios") {

content = `
<h1>BIOS / UEFI</h1>

<p>
BIOS или UEFI — встроенная система
материнской платы, управляющая запуском ПК.
</p>

<h2>Что можно настроить</h2>

<ul>
<li>Частоты CPU</li>
<li>XMP профиль RAM</li>
<li>Порядок загрузки</li>
<li>Вентиляторы</li>
<li>Напряжение компонентов</li>
</ul>

<h2>XMP / EXPO</h2>

<p>
Позволяет оперативной памяти работать
на заявленной частоте.
Без XMP RAM часто работает медленнее.
</p>

<h2>Обновление BIOS</h2>

<p>
Новые версии BIOS улучшают стабильность
и поддержку процессоров.
</p>

<h2>Важно</h2>

<p>
Неправильные настройки BIOS
могут привести к нестабильной работе системы.
</p>
`;
}

if (type === "overclock") {

content = `
<h1>Разгон процессора</h1>

<p>
Разгон позволяет увеличить производительность CPU
путем повышения частоты работы.
</p>

<h2>Что изменяется</h2>

<ul>
<li>Частота процессора</li>
<li>Напряжение</li>
<li>Power Limit</li>
</ul>

<h2>Плюсы разгона</h2>

<ul>
<li>Больше FPS</li>
<li>Выше производительность</li>
<li>Быстрее рендеринг</li>
</ul>

<h2>Минусы</h2>

<ul>
<li>Повышение температуры</li>
<li>Рост энергопотребления</li>
<li>Риск нестабильности</li>
</ul>

<h2>Важно</h2>

<p>
Для разгона нужен хороший кулер
и качественная материнская плата.
</p>
`;
}

if (type === "diagnostic") {

content = `
<h1>Диагностика компьютера</h1>

<p>
Диагностика помогает определить неисправности
и проблемы производительности ПК.
</p>

<h2>Основные проблемы</h2>

<ul>
<li>Компьютер не включается</li>
<li>Синий экран</li>
<li>Перегрев</li>
<li>Фризы в играх</li>
<li>Шум вентиляторов</li>
</ul>

<h2>Что проверяют</h2>

<ul>
<li>Температуры CPU и GPU</li>
<li>Состояние SSD</li>
<li>Оперативную память</li>
<li>Блок питания</li>
</ul>

<h2>Полезные программы</h2>

<ul>
<li>HWMonitor</li>
<li>CPU-Z</li>
<li>GPU-Z</li>
<li>MemTest</li>
<li>CrystalDiskInfo</li>
</ul>

<h2>Совет</h2>

<p>
Регулярная чистка ПК от пыли
сильно снижает риск перегрева.
</p>
`;
}

if (type === "undervolting") {
content = `
<h1>Undervolting CPU / GPU</h1>

<p>
Undervolting — это снижение напряжения процессора или видеокарты без потери производительности.
</p>

<h2>Зачем это нужно</h2>
<ul>
<li>Снижение температуры</li>
<li>Меньше шума вентиляторов</li>
<li>Повышение стабильности</li>
</ul>

<h2>Риски</h2>
<p>
Слишком сильный undervolt может вызвать вылеты игр или системы.
</p>

<h2>Итог</h2>
<p>
Это безопасный способ “охладить” ПК без покупки нового охлаждения.
</p>
`;
}

if (type === "ram_tuning") {
content = `
<h1>Тонкая настройка RAM</h1>

<p>
Настройка оперативной памяти позволяет увеличить производительность системы без замены комплектующих.
</p>

<h2>Что можно настроить</h2>
<ul>
<li>XMP профиль</li>
<li>Частота памяти</li>
<li>Тайминги (CL)</li>
</ul>

<h2>Эффект</h2>
<p>
В играх можно получить +5–20% FPS в зависимости от системы.
</p>

<h2>Важно</h2>
<p>
Слишком агрессивные настройки могут привести к нестабильности.
</p>
`;
}

if (type === "vrm") {
content = `
<h1>VRM и питание CPU</h1>

<p>
VRM — это система питания процессора на материнской плате.
От её качества зависит стабильность и разгон CPU.
</p>

<h2>Функции VRM</h2>
<ul>
<li>Стабилизация напряжения</li>
<li>Питание процессора</li>
<li>Контроль температуры</li>
</ul>

<h2>Проблемы</h2>
<p>
Слабый VRM может перегреваться и снижать производительность CPU.
</p>
`;
}

if (type === "benchmark") {
content = `
<h1>Бенчмарки и тесты</h1>

<p>
Бенчмарки — это тесты производительности компьютера.
Они помогают сравнить разные процессоры и видеокарты.
</p>

<h2>Популярные тесты</h2>
<ul>
<li>Cinebench — CPU тест</li>
<li>3DMark — GPU тест</li>
<li>AIDA64 — стресс тест</li>
</ul>

<h2>Зачем это нужно</h2>
<p>
Позволяет понять реальную мощность системы, а не только характеристики.
</p>
`;
}

document.getElementById("modal-body").innerHTML = content;
modal.classList.remove("hidden");

}

/* закрыть */
function closeArticle() {
document.getElementById("modal").classList.add("hidden");
currentLesson = null;
}

/* отметить как пройдено */
function markDone() {

if (!currentLesson) return;

localStorage.setItem("lesson_" + currentLesson, "done");

updateStatus(currentLesson);

closeArticle();

}

/* обновить статус */
function updateStatus(id) {

const el = document.getElementById("status-" + id);

if (!el) return;

if (localStorage.getItem("lesson_" + id) === "done") {
el.innerText = "✅";
} else {
el.innerText = "❌";
}

}

/* загрузка */
function loadProgress() {

[
"cpu","gpu","ram","storage","mb","psu",
"compatibility","build","cooling",
"bios","overclock","diagnostic"
].forEach(updateStatus);

}

window.onload = loadProgress;

</script>

{% endblock %}