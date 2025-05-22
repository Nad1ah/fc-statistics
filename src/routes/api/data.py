from flask import Blueprint, jsonify, request

api_bp = Blueprint('api', __name__)

@api_bp.route('/jogos', methods=['GET'])
def get_games():
    # Simulação de dados - será substituída por dados reais da base de dados
    jogos = [
        {
            'id': 1,
            'data': '2025-05-22',
            'campeonato': 'Premier League',
            'casa': 'Manchester City',
            'fora': 'Liverpool',
            'odds_casa': 1.85,
            'odds_empate': 3.50,
            'odds_fora': 4.20,
            'previsao_gols': 'Over 2.5',
            'previsao_cantos': '10-12',
            'previsao_cartoes': '3-5'
        },
        {
            'id': 2,
            'data': '2025-05-22',
            'campeonato': 'La Liga',
            'casa': 'Barcelona',
            'fora': 'Real Madrid',
            'odds_casa': 2.10,
            'odds_empate': 3.30,
            'odds_fora': 3.40,
            'previsao_gols': 'Over 2.5',
            'previsao_cantos': '9-11',
            'previsao_cartoes': '4-6'
        },
        {
            'id': 3,
            'data': '2025-05-22',
            'campeonato': 'Serie A',
            'casa': 'Juventus',
            'fora': 'Inter',
            'odds_casa': 2.25,
            'odds_empate': 3.10,
            'odds_fora': 3.30,
            'previsao_gols': 'Under 2.5',
            'previsao_cantos': '8-10',
            'previsao_cartoes': '5-7'
        }
    ]
    
    # Filtro por data (se fornecido)
    data_filtro = request.args.get('data')
    if data_filtro:
        jogos = [jogo for jogo in jogos if jogo['data'] == data_filtro]
    
    return jsonify(jogos)

@api_bp.route('/odds', methods=['GET'])
def get_odds():
    # Simulação de dados de odds de diferentes casas de apostas
    odds = [
        {
            'jogo_id': 1,
            'casas': [
                {'nome': 'Bet365', 'casa': 1.85, 'empate': 3.50, 'fora': 4.20},
                {'nome': 'Betano', 'casa': 1.87, 'empate': 3.45, 'fora': 4.15},
                {'nome': 'Betfair', 'casa': 1.90, 'empate': 3.40, 'fora': 4.10}
            ]
        },
        {
            'jogo_id': 2,
            'casas': [
                {'nome': 'Bet365', 'casa': 2.10, 'empate': 3.30, 'fora': 3.40},
                {'nome': 'Betano', 'casa': 2.15, 'empate': 3.25, 'fora': 3.35},
                {'nome': 'Betfair', 'casa': 2.05, 'empate': 3.35, 'fora': 3.45}
            ]
        },
        {
            'jogo_id': 3,
            'casas': [
                {'nome': 'Bet365', 'casa': 2.25, 'empate': 3.10, 'fora': 3.30},
                {'nome': 'Betano', 'casa': 2.20, 'empate': 3.15, 'fora': 3.35},
                {'nome': 'Betfair', 'casa': 2.30, 'empate': 3.05, 'fora': 3.25}
            ]
        }
    ]
    
    # Filtro por jogo_id (se fornecido)
    jogo_id = request.args.get('jogo_id')
    if jogo_id:
        odds = [odd for odd in odds if odd['jogo_id'] == int(jogo_id)]
    
    return jsonify(odds)

@api_bp.route('/estatisticas', methods=['GET'])
def get_statistics():
    # Simulação de dados estatísticos
    estatisticas = [
        {
            'equipa': 'Manchester City',
            'jogos': 10,
            'vitorias': 7,
            'empates': 2,
            'derrotas': 1,
            'gols_marcados': 22,
            'gols_sofridos': 8,
            'media_cantos': 7.5,
            'media_cartoes': 2.3
        },
        {
            'equipa': 'Liverpool',
            'jogos': 10,
            'vitorias': 6,
            'empates': 3,
            'derrotas': 1,
            'gols_marcados': 18,
            'gols_sofridos': 7,
            'media_cantos': 6.8,
            'media_cartoes': 1.9
        }
    ]
    
    # Filtro por equipa (se fornecido)
    equipa = request.args.get('equipa')
    if equipa:
        estatisticas = [est for est in estatisticas if est['equipa'].lower() == equipa.lower()]
    
    return jsonify(estatisticas)
