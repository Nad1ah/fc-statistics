import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory, render_template, redirect, url_for
from src.routes.views.main import main_bp
from src.routes.views.telegram import telegram_bp
from src.routes.views.betting import betting_bp
from src.routes.api.data import data_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Registrar blueprints
app.register_blueprint(main_bp)
app.register_blueprint(telegram_bp)
app.register_blueprint(betting_bp)
app.register_blueprint(data_bp, url_prefix='/api/data')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    # Rotas específicas já são tratadas pelos blueprints
    # Esta função serve apenas para arquivos estáticos ou redirecionar para a página inicial
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        # Verificar se é uma rota conhecida
        if path in ['relatorios', 'analise-mercados', 'comparacao-odds', 'estatisticas', 'telegram-config', 'sugestoes-apostas', 'sobre']:
            # Redirecionar para a rota correta
            return redirect(url_for(f'main.{path.replace("-", "_")}'))
        
        # Se não for uma rota conhecida, tentar servir o index.html
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            # Se não encontrar o index.html, redirecionar para a página inicial
            return redirect(url_for('main.index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Adicionar esta linha para o Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
