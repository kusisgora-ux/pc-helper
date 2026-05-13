import sqlite3
import os

DB_NAME = "pc_helper.db"

def init_db():
    if os.path.exists(DB_NAME):
        try:
            os.remove(DB_NAME)
        except PermissionError:
            print("❌ Ошибка: Закрой все программы, использующие pc_helper.db")
            return

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # ================= СОЗДАНИЕ ТАБЛИЦ =================
    cur.execute("""
    CREATE TABLE processors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, socket TEXT, cores INTEGER, threads INTEGER, 
        freq FLOAT, tdp INTEGER, price INTEGER, url TEXT, img TEXT
    )""")

    cur.execute("""
    CREATE TABLE gpus (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, memory INTEGER, freq INTEGER, power INTEGER, 
        price INTEGER, url TEXT, img TEXT
    )""")

    cur.execute("""
    CREATE TABLE motherboards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, socket TEXT, chipset TEXT, form_factor TEXT, 
        ram_type TEXT, price INTEGER, url TEXT, img TEXT
    )""")

    cur.execute("""
    CREATE TABLE ram (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, size INTEGER, freq INTEGER, type TEXT, price INTEGER, url TEXT, img TEXT
    )""")

    cur.execute("""
    CREATE TABLE psu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, power INTEGER, certificate TEXT, price INTEGER, url TEXT, img TEXT
    )""")

    cur.execute("""
    CREATE TABLE coolers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, socket TEXT, tdp INTEGER, price INTEGER, url TEXT, img TEXT
    )""")

    cur.execute("""
    CREATE TABLE ssd (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, size INTEGER, speed INTEGER, type TEXT, price INTEGER, url TEXT, img TEXT
    )""")

    cur.execute("""
    CREATE TABLE cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, form_factor TEXT, max_gpu INTEGER, price INTEGER, url TEXT, img TEXT
    )""")

    def adapt_data(data_list, total_cols):
        final_list = []
        for item in data_list:
            row = list(item)
            # Если нет URL (последний элемент перед img)
            if len(row) < total_cols - 1:
                row.append("https://www.dns-shop.ru")
            # Если нет картинки
            if len(row) < total_cols:
                row.append("default.jpg")
            final_list.append(tuple(row))
        return final_list

    # ================= ПРОЦЕССОРЫ (12 шт) =================
    cpus = [
        ("Intel Core i3-12100F", "LGA1700", 4, 8, 3.3, 58, 10299, "https://www.dns-shop.ru/search/?q=i3-12100f"),
        ("Intel Core i5-12400F", "LGA1700", 6, 12, 2.5, 65, 12499, "https://www.dns-shop.ru/search/?q=i5-12400f"),
        ("Intel Core i5-13400F", "LGA1700", 10, 16, 2.5, 65, 14499, "https://www.dns-shop.ru/search/?q=i5-13400f"),
        ("Intel Core i7-14700KF", "LGA1700", 20, 28, 3.4, 125, 32799, "https://www.dns-shop.ru/search/?q=i7-14700kf"),
        ("Intel Core i9-14900K", "LGA1700", 24, 32, 3.2, 150, 48299, "https://www.dns-shop.ru/search/?q=i9-14900k"),
        ("AMD Ryzen 5 5500", "AM4", 6, 12, 3.6, 65, 7500, "https://www.dns-shop.ru/search/?q=ryzen+5+5500"),
        ("AMD Ryzen 5 5600", "AM4", 6, 12, 3.5, 65, 11299, "https://www.dns-shop.ru/search/?q=ryzen+5+5600"),
        ("AMD Ryzen 7 5700X", "AM4", 8, 16, 3.4, 65, 14899, "https://www.dns-shop.ru/search/?q=ryzen+7+5700x"),
        ("AMD Ryzen 5 7500F", "AM5", 6, 12, 3.7, 65, 11299, "https://www.dns-shop.ru/search/?q=ryzen+5+7500f"),
        ("AMD Ryzen 7 7700X", "AM5", 8, 16, 4.5, 105, 21599, "https://www.dns-shop.ru/search/?q=ryzen+7+7700x"),
        ("AMD Ryzen 7 7800X3D", "AM5", 8, 16, 4.2, 120, 28999, "https://www.dns-shop.ru/search/?q=7800x3d"),
        ("AMD Ryzen 9 7950X", "AM5", 16, 32, 4.5, 170, 46299, "https://www.dns-shop.ru/search/?q=ryzen+9+7950x")
    ]
    cur.executemany("INSERT INTO processors (name, socket, cores, threads, freq, tdp, price, url, img) VALUES (?,?,?,?,?,?,?,?,?)", adapt_data(cpus, 9))

    # ================= ВИДЕОКАРТЫ (10 шт) =================
    gpus = [
        ("RTX 3060", 12, 1320, 170, 32499, "https://www.dns-shop.ru/search/?q=rtx+3060+12gb"),
        ("RTX 4060", 8, 1830, 115, 33999, "https://www.dns-shop.ru/search/?q=rtx+4060"),
        ("RTX 4060 Ti", 8, 2310, 160, 46000, "https://www.dns-shop.ru/search/?q=rtx+4060+ti"),
        ("RTX 4070 Super", 12, 1980, 220, 59999, "https://www.dns-shop.ru/search/?q=rtx+4070+super"),
        ("RTX 4080 Super", 16, 2295, 320, 99999, "https://www.dns-shop.ru/search/?q=rtx+4080+super"),
        ("RTX 4090", 24, 2230, 450, 209999, "https://www.dns-shop.ru/search/?q=rtx+4090"),
        ("RX 6600", 8, 1626, 132, 269999, "https://www.dns-shop.ru/search/?q=rx+6600"),
        ("RX 7600", 8, 2250, 165, 28999, "https://www.dns-shop.ru/search/?q=rx+7600"),
        ("RX 7700 XT", 12, 2171, 245, 34999, "https://www.dns-shop.ru/search/?q=rx+7700+xt"),
        ("RX 7800 XT", 16, 2124, 263, 60499, "https://www.dns-shop.ru/search/?q=rx+7800+xt")
    ]
    cur.executemany("INSERT INTO gpus (name, memory, freq, power, price, url, img) VALUES (?,?,?,?,?,?,?)", adapt_data(gpus, 7))

    # ================= МАТЕРИНСКИЕ ПЛАТЫ (9 шт) =================
    mbs = [
        ("MSI H610M-E DDR4", "LGA1700", "H610", "mATX", "DDR4", 5399, "https://www.dns-shop.ru/search/?q=msi+h610m-e"),
        ("MSI B550M PRO-VDH WIFI", "AM4", "B550", "mATX", "DDR4", 8999, "https://www.dns-shop.ru/search/?q=MSI+B550M+PRO-VDH"),
        ("GIGABYTE B760 DS3H", "LGA1700", "B760", "ATX", "DDR5", 10399, "https://www.dns-shop.ru/search/?q=GIGABYTE+B760+DS3H"),
        ("ASUS TUF GAMING B550-PLUS", "AM4", "B550", "ATX", "DDR4", 16699, "https://www.dns-shop.ru/search/?q=asus+tuf+gaming+b550-plus"),
        ("ASRock B650M-H/M.2", "AM5", "B650", "mATX", "DDR5", 7499, "https://www.dns-shop.ru/search/?q=asrock+b650m-h"),
        ("ASUS TUF GAMING B650-PLUS", "AM5", "B650", "ATX", "DDR5", 14399, "https://www.dns-shop.ru/search/?q=ASUS+TUF+GAMING+B650-PLUS"),
        ("GIGABYTE Z790 GAMING X", "LGA1700", "Z790", "ATX", "DDR5", 26599, "https://www.dns-shop.ru/search/?q=gigabyte+z790+gaming+x"),
        ("MSI MAG B650 TOMAHAWK", "AM5", "B650", "ATX", "DDR5", 15499, "https://www.dns-shop.ru/search/?q=msi+mag+b650+tomahawk"),
        ("ASUS ROG STRIX Z790-F", "LGA1700", "Z790", "ATX", "DDR5", 39999, "https://www.dns-shop.ru/search/?q=asus+rog+strix+z790-f")
    ]
    cur.executemany("INSERT INTO motherboards (name, socket, chipset, form_factor, ram_type, price, url, img) VALUES (?,?,?,?,?,?,?,?)", adapt_data(mbs, 8))

    # ================= ОПЕРАТИВНАЯ ПАМЯТЬ (9 шт) =================
    rams = [
        ("Kingston FURY Beast 8GB", 8, 3200, "DDR4", 7499, "https://www.dns-shop.ru/search/?q=kingston+fury+8gb"),
        ("Kingston FURY Beast 16GB", 16, 3200, "DDR4", 14999, "https://www.dns-shop.ru/search/?q=kingston+fury+16gb"),
        ("ADATA XPG Spectrix 16GB", 16, 3600, "DDR4", 13999, "https://www.dns-shop.ru/search/?q=adata+xpg+16gb"),
        ("G.Skill AEGIS 32GB", 32, 3200, "DDR4", 22499, "https://www.dns-shop.ru/search/?q=g.skill+32gb+ddr4"),
        ("Crucial DDR5 16GB", 16, 4800, "DDR5", 23099, "https://www.dns-shop.ru/search/?q=crucial+16gb+ddr5"),
        ("Kingston FURY Renegade 32GB", 32, 6000, "DDR5", 31599, "https://www.dns-shop.ru/search/?q=fury+renegade+32gb+ddr5"),
        ("ADATA XPG Lancer 32GB", 32, 5200, "DDR5", 39999, "https://www.dns-shop.ru/search/?q=adata+lancer+32gb"),
        ("G.Skill TRIDENT Z5 32GB", 32, 7200, "DDR5", 44999, "https://www.dns-shop.ru/search/?q=g.skill+z5+32gb"),
        ("Team Group T-Force 16GB", 16, 3600, "DDR4", 37999, "https://www.dns-shop.ru/search/?q=team+group+16gb")
    ]
    cur.executemany("INSERT INTO ram (name, size, freq, type, price, url, img) VALUES (?,?,?,?,?,?,?)", adapt_data(rams, 7))

    # ================= БЛОКИ ПИТАНИЯ (8 шт) =================
    psus = [
        ("Deepcool PF500", 500, "80+", 2999, "https://www.dns-shop.ru/search/?q=deepcool+pf500"),
        ("Deepcool PK650D", 650, "80+ Bronze", 5299, "https://www.dns-shop.ru/search/?q=Deepcool+PK650D"),
        ("Cooler Master MWE 700W", 700, "80+ Bronze", 6399, "https://www.dns-shop.ru/search/?q=mwe+700w"),
        ("Montech Century 850W", 850, "80+ Gold", 8599, "https://www.dns-shop.ru/search/?q=Montech+Century+850W"),
        ("Cougar GEX 750W", 750, "80+ Gold", 5699, "https://www.dns-shop.ru/search/?q=cougar+gex+750"),
        ("be quiet! Straight Power 850W", 850, "80+ Gold", 13399, "https://www.dns-shop.ru/search/?q=be+quiet+850w"),
        ("Corsair RM1000e", 1000, "80+ Gold", 18599, "https://www.dns-shop.ru/search/?q=corsair+rm1000e"),
        ("Chieftec Polaris 750W", 750, "80+ Gold", 7899, "https://www.dns-shop.ru/search/?q=chieftec+polaris+750")
    ]
    cur.executemany("INSERT INTO psu (name, power, certificate, price, url, img) VALUES (?,?,?,?,?,?)", adapt_data(psus, 6))

    # ================= КУЛЕРЫ (8 шт) =================
    coolers = [
        ("ID-COOLING SE-903-SD", "Multi", 130, 950, "https://www.dns-shop.ru/search/?q=se-903-sd"),
        ("ID-COOLING SE-224-XTS", "Multi", 220, 1799, "https://www.dns-shop.ru/search/?q=SE-224-XTS"),
        ("Deepcool AK400", "Multi", 220, 2050, "https://www.dns-shop.ru/search/?q=deepcool+ak400"),
        ("Deepcool AK620", "Multi", 260, 4799, "https://www.dns-shop.ru/search/?q=Deepcool+AK620"),
        ("be quiet! Dark Rock Pro 4", "Multi", 250, 4299, "https://www.dns-shop.ru/search/?q=dark+rock+pro+4"),
        ("Noctua NH-D15", "Multi", 250, 5499, "https://www.dns-shop.ru/search/?q=noctua+nh-d15"),
        ("ID-COOLING ZOOMFLOW 240", "Multi", 250, 3999, "https://www.dns-shop.ru/search/?q=zoomflow+240"),
        ("Deepcool LS720 (СЖО)", "Multi", 300, 6899, "https://www.dns-shop.ru/search/?q=deepcool+ls720")
    ]
    cur.executemany("INSERT INTO coolers (name, socket, tdp, price, url, img) VALUES (?,?,?,?,?,?)", adapt_data(coolers, 6))

    # ================= SSD (8 шт) =================
    ssds = [
        ("Kingston NV2 500GB", 500, 3500, "NVMe", 9199, "https://www.dns-shop.ru/search/?q=kingston+nv2+500gb"),
        ("Kingston NV2 1TB", 1000, 3500, "NVMe", 12899, "https://www.dns-shop.ru/search/?q=Kingston+NV2+1TB"),
        ("ADATA Legend 800 1TB", 1000, 3500, "NVMe", 16999, "https://www.dns-shop.ru/search/?q=legend+800"),
        ("Samsung 980 1TB", 1000, 3500, "NVMe", 18999, "https://www.dns-shop.ru/search/?q=samsung+980+1tb"),
        ("Samsung 980 PRO 1TB", 1000, 7000, "NVMe", 21999, "https://www.dns-shop.ru/search/?q=Samsung+980+PRO+1TB"),
        ("Samsung 990 PRO 2TB", 2000, 7450, "NVMe", 18399, "https://www.dns-shop.ru/search/?q=samsung+990+pro+2tb"),
        ("WD Blue SN580 1TB", 1000, 4150, "NVMe", 16899, "https://www.dns-shop.ru/search/?q=sn580+1tb"),
        ("Netac N535N 250GB", 250, 500, "SATA", 9099, "https://www.dns-shop.ru/search/?q=netac+n535n")
    ]
    cur.executemany("INSERT INTO ssd (name, size, speed, type, price, url, img) VALUES (?,?,?,?,?,?,?)", adapt_data(ssds, 7))

    # ================= КОРПУСА (8 шт) =================
    cases = [
        ("Deepcool CC560", "ATX", 370, 4799, "https://www.dns-shop.ru/search/?q=Deepcool+CC560"),
        ("Cougar Duoface Pro", "ATX", 390, 7099, "https://www.dns-shop.ru/search/?q=Cougar+Duoface+Pro"),
        ("AeroCool Cylon", "ATX", 346, 3199 , "https://www.dns-shop.ru/search/?q=aerocool+cylon"),
        ("Zalman i3 Edge", "ATX", 360, 5399, "https://www.dns-shop.ru/search/?q=zalman+i3+edge"),
        ("Montech AIR 1000 Lite", "ATX", 340, 4199, "https://www.dns-shop.ru/search/?q=air+1000+lite"),
        ("Lian Li PC-O11 Dynamic", "ATX", 420, 15999, "https://www.dns-shop.ru/search/?q=lian+li+o11"),
        ("Powercase Mistral Z4", "ATX", 310, 3999, "https://www.dns-shop.ru/search/?q=mistral+z4"),
        ("ARDOR GAMING Rare M2", "ATX", 350, 4499, "https://www.dns-shop.ru/search/?q=rare+m2")
    ]
    cur.executemany("INSERT INTO cases (name, form_factor, max_gpu, price, url, img) VALUES (?,?,?,?,?,?)", adapt_data(cases, 6))

    conn.commit()
    conn.close()
    print("✅ База успешно создана!")

if __name__ == "__main__":
    init_db()