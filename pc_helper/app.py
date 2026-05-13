from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
show_smart = False

# =========================
# 💻 ГОТОВЫЕ СБОРКИ (БЕЗ ССЫЛОК)
# =========================

BUILDS_DATA = [
    {
        "title": "RTX 3050 базовый игровой ПК",
        "price": 60000,
        "cpu": "i3-12100F",
        "gpu": "RTX 3050",
        "ram": "16GB",
        "ssd": "512GB"
    },
    {
        "title": "RX 6600 народный ПК",
        "price": 65000,
        "cpu": "Ryzen 5 5500",
        "gpu": "RX 6600",
        "ram": "16GB",
        "ssd": "1TB"
    },
    {
        "title": "RTX 4060 оптимальный старт",
        "price": 80000,
        "cpu": "i5-12400F",
        "gpu": "RTX 4060",
        "ram": "16GB",
        "ssd": "1TB"
    },
    {
        "title": "RTX 4070 баланс 2K",
        "price": 135000,
        "cpu": "i5-13600KF",
        "gpu": "RTX 4070",
        "ram": "32GB",
        "ssd": "1TB"
    },
    {
        "title": "RTX 4080 Super 4K",
        "price": 220000,
        "cpu": "Ryzen 9 7900X",
        "gpu": "RTX 4080 Super",
        "ram": "32GB",
        "ssd": "2TB"
    },
    {
        "title": "RTX 4090 флагман",
        "price": 330000,
        "cpu": "i9-14900KF",
        "gpu": "RTX 4090",
        "ram": "64GB",
        "ssd": "2TB"
    }
]


# =========================
# DB
# =========================

def get_db():
    conn = sqlite3.connect("pc_helper.db")
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# ROUTES
# =========================

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/catalog")
def catalog():
    db = get_db()
    data = {
        "cpus": db.execute("SELECT * FROM processors").fetchall(),
        "gpus": db.execute("SELECT * FROM gpus").fetchall(),
        "ram": db.execute("SELECT * FROM ram").fetchall(),
        "motherboards": db.execute("SELECT * FROM motherboards").fetchall(),
        "psu": db.execute("SELECT * FROM psu").fetchall(),
        "ssd": db.execute("SELECT * FROM ssd").fetchall(),
        "coolers": db.execute("SELECT * FROM coolers").fetchall(),
        "cases": db.execute("SELECT * FROM cases").fetchall()
    }
    db.close()
    return render_template("catalog.html", **data)


@app.route("/configurator")
def configurator():
    db = get_db()
    data = {
        "cpus": db.execute("SELECT * FROM processors").fetchall(),
        "gpus": db.execute("SELECT * FROM gpus").fetchall(),
        "ram": db.execute("SELECT * FROM ram").fetchall(),
        "motherboards": db.execute("SELECT * FROM motherboards").fetchall(),
        "psu": db.execute("SELECT * FROM psu").fetchall(),
        "ssd": db.execute("SELECT * FROM ssd").fetchall(),
        "coolers": db.execute("SELECT * FROM coolers").fetchall(),
        "cases": db.execute("SELECT * FROM cases").fetchall()
    }
    db.close()
    return render_template("configurator.html", **data)


@app.route("/theory")
def theory():
    return render_template("theory.html")


# =========================
# 💥 SMART BUILD (СТАБИЛЬНЫЙ)
# =========================

#app.route("/smart/<int:budget>")
#def smart_build(budget):

    #builds = BUILDS_DATA

    ## защита от ошибок
    #safe_builds = []
    #for b in builds:
        #price = b.get("price", 0)

        #try:
        #    price = int(price)
        #except:
           # price = 0

      #  b["price"] = price
     #   safe_builds.append(b)

    # сначала под бюджет
    #under_budget = [b for b in safe_builds if b["price"] <= budget]
    #under_budget = sorted(under_budget, key=lambda x: x["price"])

    # если пусто — ближайшие
   # if not under_budget:
        #under_budget = sorted(
            #safe_builds,
           # key=lambda x: abs(x["price"] - budget)
       # )[:5]

    #return render_template(
        #"smart_build.html",
       # builds=under_budget,
       # budget=budget
    #


# =========================
# FORMAT FILTER
# =========================

@app.template_filter('min_format')
def min_format(value):
    return "{:,}".format(value).replace(",", " ")


if __name__ == "__main__":
    app.run(debug=True)