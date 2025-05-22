from flask import Blueprint, render_template, request

api_bp = Blueprint('api', __name__, url_prefix='/api')
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/relatorios')
def reports():
    jogo_id = request.args.get('jogo')
    return render_template('reports.html', jogo_id=jogo_id)

@main_bp.route('/analise-mercados')
def market_analysis():
    tipo = request.args.get('tipo', 'gols')
    return render_template('market_analysis.html', tipo=tipo)

@main_bp.route('/comparacao-odds')
def odds_comparison():
    return render_template('odds_comparison.html')

@main_bp.route('/estatisticas')
def statistics():
    return render_template('statistics.html')

@main_bp.route('/sobre')
def about():
    return render_template('about.html')
