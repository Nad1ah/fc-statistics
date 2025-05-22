import os
from flask import Flask, render_template

app = Flask(__name__, static_folder="src/static", template_folder="src/templates")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/relatorios")
def relatorios():
    return render_template("reports.html")


@app.route("/analise-mercados")
def analise_mercados():
    return render_template("market_analysis.html")


@app.route("/comparacao-odds")
def comparacao_odds():
    return render_template("odds_comparison.html")


@app.route("/estatisticas")
def estatisticas():
    return render_template("statistics.html")


@app.route("/telegram-config")
def telegram_config():
    return render_template("telegram_config.html")


@app.route("/sugestoes-apostas")
def sugestoes_apostas():
    return render_template("betting_suggestions.html")


@app.route("/sobre")
def sobre():
    return render_template("index.html")  # Podemos criar uma página específica depois


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
