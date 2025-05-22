from flask import Blueprint, render_template, request, jsonify
import json
import os
import datetime
import random

betting_bp = Blueprint('betting', __name__)

# Simulação de dados para sugestões de apostas
betting_data = {
    'leagues': ['Premier League', 'La Liga', 'Serie A', 'Bundesliga', 'Ligue 1'],
    'markets': ['Resultado Final (1X2)', 'Over/Under Golos', 'Ambas Marcam', 'Cantos', 'Cartões'],
    'bookmakers': ['Bet365', 'Betano', 'Betfair', '1xBet', 'Bwin'],
    'suggestions': []
}

# Dados simulados para análise estatística
statistical_data = {
    'teams': {
        'Manchester City': {
            'home_win_rate': 0.75,
            'away_win_rate': 0.60,
            'goals_scored_avg': 2.8,
            'goals_conceded_avg': 0.9,
            'btts_rate': 0.65,
            'over25_rate': 0.70,
            'corners_avg': 7.5,
            'cards_avg': 1.8
        },
        'Liverpool': {
            'home_win_rate': 0.70,
            'away_win_rate': 0.55,
            'goals_scored_avg': 2.5,
            'goals_conceded_avg': 1.0,
            'btts_rate': 0.60,
            'over25_rate': 0.65,
            'corners_avg': 7.8,
            'cards_avg': 1.9
        },
        'Barcelona': {
            'home_win_rate': 0.72,
            'away_win_rate': 0.50,
            'goals_scored_avg': 2.6,
            'goals_conceded_avg': 1.1,
            'btts_rate': 0.62,
            'over25_rate': 0.68,
            'corners_avg': 6.5,
            'cards_avg': 2.0
        },
        'Real Madrid': {
            'home_win_rate': 0.74,
            'away_win_rate': 0.58,
            'goals_scored_avg': 2.7,
            'goals_conceded_avg': 1.0,
            'btts_rate': 0.64,
            'over25_rate': 0.72,
            'corners_avg': 6.7,
            'cards_avg': 1.7
        },
        'Juventus': {
            'home_win_rate': 0.68,
            'away_win_rate': 0.45,
            'goals_scored_avg': 2.0,
            'goals_conceded_avg': 0.8,
            'btts_rate': 0.55,
            'over25_rate': 0.60,
            'corners_avg': 5.7,
            'cards_avg': 2.1
        },
        'Inter': {
            'home_win_rate': 0.65,
            'away_win_rate': 0.48,
            'goals_scored_avg': 2.2,
            'goals_conceded_avg': 1.0,
            'btts_rate': 0.58,
            'over25_rate': 0.62,
            'corners_avg': 5.8,
            'cards_avg': 2.2
        }
    },
    'head_to_head': {
        'Manchester City-Liverpool': {
            'home_win_rate': 0.40,
            'away_win_rate': 0.35,
            'draw_rate': 0.25,
            'btts_rate': 0.75,
            'over25_rate': 0.80,
            'avg_goals': 3.2,
            'corners_avg': 10.5,
            'cards_avg': 3.8
        },
        'Barcelona-Real Madrid': {
            'home_win_rate': 0.38,
            'away_win_rate': 0.37,
            'draw_rate': 0.25,
            'btts_rate': 0.80,
            'over25_rate': 0.70,
            'avg_goals': 3.0,
            'corners_avg': 9.8,
            'cards_avg': 5.2
        },
        'Juventus-Inter': {
            'home_win_rate': 0.42,
            'away_win_rate': 0.33,
            'draw_rate': 0.25,
            'btts_rate': 0.65,
            'over25_rate': 0.55,
            'avg_goals': 2.2,
            'corners_avg': 8.5,
            'cards_avg': 4.5
        }
    }
}

# Função para gerar probabilidades baseadas em dados estatísticos
def generate_probabilities(home_team, away_team):
    h2h_key = f"{home_team}-{away_team}"
    h2h_data = statistical_data['head_to_head'].get(h2h_key, None)
    
    home_data = statistical_data['teams'].get(home_team, {})
    away_data = statistical_data['teams'].get(away_team, {})
    
    if h2h_data:
        # Usar dados de confronto direto quando disponíveis
        home_win_prob = h2h_data['home_win_rate'] * 100
        draw_prob = h2h_data['draw_rate'] * 100
        away_win_prob = h2h_data['away_win_rate'] * 100
        btts_prob = h2h_data['btts_rate'] * 100
        over25_prob = h2h_data['over25_rate'] * 100
        corners_avg = h2h_data['corners_avg']
        cards_avg = h2h_data['cards_avg']
    else:
        # Calcular baseado em dados individuais das equipas
        home_win_prob = home_data.get('home_win_rate', 0.5) * 100
        away_win_prob = away_data.get('away_win_rate', 0.3) * 100
        draw_prob = 100 - home_win_prob - away_win_prob
        
        # Ajustar para garantir que a soma seja 100%
        total = home_win_prob + draw_prob + away_win_prob
        home_win_prob = (home_win_prob / total) * 100
        draw_prob = (draw_prob / total) * 100
        away_win_prob = (away_win_prob / total) * 100
        
        btts_prob = (home_data.get('btts_rate', 0.5) + away_data.get('btts_rate', 0.5)) / 2 * 100
        over25_prob = (home_data.get('over25_rate', 0.5) + away_data.get('over25_rate', 0.5)) / 2 * 100
        corners_avg = (home_data.get('corners_avg', 6) + away_data.get('corners_avg', 6)) / 2
        cards_avg = (home_data.get('cards_avg', 2) + away_data.get('cards_avg', 2)) / 2
    
    return {
        'home_win': round(home_win_prob, 1),
        'draw': round(draw_prob, 1),
        'away_win': round(away_win_prob, 1),
        'btts': round(btts_prob, 1),
        'over25': round(over25_prob, 1),
        'corners_avg': round(corners_avg, 1),
        'cards_avg': round(cards_avg, 1)
    }

# Função para gerar odds baseadas em probabilidades
def generate_odds(probabilities):
    # Converter probabilidade para odd decimal (com margem de lucro da casa de apostas)
    margin = 1.1  # 10% de margem
    
    home_odd = round((100 / probabilities['home_win']) * margin, 2)
    draw_odd = round((100 / probabilities['draw']) * margin, 2)
    away_odd = round((100 / probabilities['away_win']) * margin, 2)
    
    btts_yes_odd = round((100 / probabilities['btts']) * margin, 2)
    btts_no_odd = round((100 / (100 - probabilities['btts'])) * margin, 2)
    
    over25_odd = round((100 / probabilities['over25']) * margin, 2)
    under25_odd = round((100 / (100 - probabilities['over25'])) * margin, 2)
    
    # Adicionar variação entre casas de apostas
    odds = {
        'Resultado Final (1X2)': {
            'Bet365': {'1': home_odd, 'X': draw_odd, '2': away_odd},
            'Betano': {'1': round(home_odd * random.uniform(0.98, 1.02), 2), 
                       'X': round(draw_odd * random.uniform(0.98, 1.02), 2), 
                       '2': round(away_odd * random.uniform(0.98, 1.02), 2)},
            'Betfair': {'1': round(home_odd * random.uniform(0.98, 1.02), 2), 
                        'X': round(draw_odd * random.uniform(0.98, 1.02), 2), 
                        '2': round(away_odd * random.uniform(0.98, 1.02), 2)},
            '1xBet': {'1': round(home_odd * random.uniform(0.98, 1.02), 2), 
                      'X': round(draw_odd * random.uniform(0.98, 1.02), 2), 
                      '2': round(away_odd * random.uniform(0.98, 1.02), 2)},
            'Bwin': {'1': round(home_odd * random.uniform(0.98, 1.02), 2), 
                     'X': round(draw_odd * random.uniform(0.98, 1.02), 2), 
                     '2': round(away_odd * random.uniform(0.98, 1.02), 2)}
        },
        'Over/Under Golos': {
            'Bet365': {'Over 2.5': over25_odd, 'Under 2.5': under25_odd},
            'Betano': {'Over 2.5': round(over25_odd * random.uniform(0.98, 1.02), 2), 
                       'Under 2.5': round(under25_odd * random.uniform(0.98, 1.02), 2)},
            'Betfair': {'Over 2.5': round(over25_odd * random.uniform(0.98, 1.02), 2), 
                        'Under 2.5': round(under25_odd * random.uniform(0.98, 1.02), 2)},
            '1xBet': {'Over 2.5': round(over25_odd * random.uniform(0.98, 1.02), 2), 
                      'Under 2.5': round(under25_odd * random.uniform(0.98, 1.02), 2)},
            'Bwin': {'Over 2.5': round(over25_odd * random.uniform(0.98, 1.02), 2), 
                     'Under 2.5': round(under25_odd * random.uniform(0.98, 1.02), 2)}
        },
        'Ambas Marcam': {
            'Bet365': {'Sim': btts_yes_odd, 'Não': btts_no_odd},
            'Betano': {'Sim': round(btts_yes_odd * random.uniform(0.98, 1.02), 2), 
                       'Não': round(btts_no_odd * random.uniform(0.98, 1.02), 2)},
            'Betfair': {'Sim': round(btts_yes_odd * random.uniform(0.98, 1.02), 2), 
                        'Não': round(btts_no_odd * random.uniform(0.98, 1.02), 2)},
            '1xBet': {'Sim': round(btts_yes_odd * random.uniform(0.98, 1.02), 2), 
                      'Não': round(btts_no_odd * random.uniform(0.98, 1.02), 2)},
            'Bwin': {'Sim': round(btts_yes_odd * random.uniform(0.98, 1.02), 2), 
                     'Não': round(btts_no_odd * random.uniform(0.98, 1.02), 2)}
        }
    }
    
    return odds

# Função para gerar sugestões de apostas baseadas em valor
def generate_betting_suggestions(home_team, away_team, probabilities, odds):
    suggestions = []
    
    # Verificar valor em 1X2
    for bookmaker, values in odds['Resultado Final (1X2)'].items():
        # Home win
        implied_prob = 100 / values['1']
        if probabilities['home_win'] > implied_prob:
            value_percent = round(((probabilities['home_win'] / implied_prob) - 1) * 100, 1)
            if value_percent > 5:  # Apenas sugerir se tiver pelo menos 5% de valor
                confidence = min(3, 1 + int(value_percent / 5))  # 1-3 estrelas baseado no valor
                suggestions.append({
                    'match': f"{home_team} vs {away_team}",
                    'market': 'Resultado Final (1X2)',
                    'selection': f"{home_team} Vence",
                    'odd': values['1'],
                    'bookmaker': bookmaker,
                    'value': value_percent,
                    'confidence': confidence,
                    'justification': f"Probabilidade calculada: {probabilities['home_win']}%, Probabilidade implícita na odd: {round(implied_prob, 1)}%"
                })
        
        # Away win
        implied_prob = 100 / values['2']
        if probabilities['away_win'] > implied_prob:
            value_percent = round(((probabilities['away_win'] / implied_prob) - 1) * 100, 1)
            if value_percent > 5:
                confidence = min(3, 1 + int(value_percent / 5))
                suggestions.append({
                    'match': f"{home_team} vs {away_team}",
                    'market': 'Resultado Final (1X2)',
                    'selection': f"{away_team} Vence",
                    'odd': values['2'],
                    'bookmaker': bookmaker,
                    'value': value_percent,
                    'confidence': confidence,
                    'justification': f"Probabilidade calculada: {probabilities['away_win']}%, Probabilidade implícita na odd: {round(implied_prob, 1)}%"
                })
    
    # Verificar valor em Over/Under
    for bookmaker, values in odds['Over/Under Golos'].items():
        # Over 2.5
        implied_prob = 100 / values['Over 2.5']
        if probabilities['over25'] > implied_prob:
            value_percent = round(((probabilities['over25'] / implied_prob) - 1) * 100, 1)
            if value_percent > 5:
                confidence = min(3, 1 + int(value_percent / 5))
                suggestions.append({
                    'match': f"{home_team} vs {away_team}",
                    'market': 'Over/Under Golos',
                    'selection': 'Over 2.5',
                    'odd': values['Over 2.5'],
                    'bookmaker': bookmaker,
                    'value': value_percent,
                    'confidence': confidence,
                    'justification': f"Probabilidade calculada: {probabilities['over25']}%, Probabilidade implícita na odd: {round(implied_prob, 1)}%"
                })
        
        # Under 2.5
        implied_prob = 100 / values['Under 2.5']
        if (100 - probabilities['over25']) > implied_prob:
            value_percent = round((((100 - probabilities['over25']) / implied_prob) - 1) * 100, 1)
            if value_percent > 5:
                confidence = min(3, 1 + int(value_percent / 5))
                suggestions.append({
                    'match': f"{home_team} vs {away_team}",
                    'market': 'Over/Under Golos',
                    'selection': 'Under 2.5',
                    'odd': values['Under 2.5'],
                    'bookmaker': bookmaker,
                    'value': value_percent,
                    'confidence': confidence,
                    'justification': f"Probabilidade calculada: {100 - probabilities['over25']}%, Probabilidade implícita na odd: {round(implied_prob, 1)}%"
                })
    
    # Verificar valor em Ambas Marcam
    for bookmaker, values in odds['Ambas Marcam'].items():
        # Sim
        implied_prob = 100 / values['Sim']
        if probabilities['btts'] > implied_prob:
            value_percent = round(((probabilities['btts'] / implied_prob) - 1) * 100, 1)
            if value_percent > 5:
                confidence = min(3, 1 + int(value_percent / 5))
                suggestions.append({
                    'match': f"{home_team} vs {away_team}",
                    'market': 'Ambas Marcam',
                    'selection': 'Sim',
                    'odd': values['Sim'],
                    'bookmaker': bookmaker,
                    'value': value_percent,
                    'confidence': confidence,
                    'justification': f"Probabilidade calculada: {probabilities['btts']}%, Probabilidade implícita na odd: {round(implied_prob, 1)}%"
                })
        
        # Não
        implied_prob = 100 / values['Não']
        if (100 - probabilities['btts']) > implied_prob:
            value_percent = round((((100 - probabilities['btts']) / implied_prob) - 1) * 100, 1)
            if value_percent > 5:
                confidence = min(3, 1 + int(value_percent / 5))
                suggestions.append({
                    'match': f"{home_team} vs {away_team}",
                    'market': 'Ambas Marcam',
                    'selection': 'Não',
                    'odd': values['Não'],
                    'bookmaker': bookmaker,
                    'value': value_percent,
                    'confidence': confidence,
                    'justification': f"Probabilidade calculada: {100 - probabilities['btts']}%, Probabilidade implícita na odd: {round(implied_prob, 1)}%"
                })
    
    # Ordenar sugestões por valor
    suggestions.sort(key=lambda x: x['value'], reverse=True)
    
    # Limitar a 5 sugestões
    return suggestions[:5]

# Rota para a página de sugestões de apostas
@betting_bp.route('/sugestoes-apostas', methods=['GET'])
def betting_suggestions_page():
    """Página de sugestões de apostas"""
    return render_template('betting_suggestions.html')

# API para gerar sugestões de apostas
@betting_bp.route('/api/betting/generate-suggestions', methods=['POST'])
def generate_suggestions():
    """API para gerar sugestões de apostas baseadas em dados estatísticos"""
    data = request.json
    
    # Obter dados dos jogos
    matches = data.get('matches', [])
    if not matches:
        # Usar jogos padrão se nenhum for fornecido
        matches = [
            {'home': 'Manchester City', 'away': 'Liverpool', 'league': 'Premier League', 'time': '20:45'},
            {'home': 'Barcelona', 'away': 'Real Madrid', 'league': 'La Liga', 'time': '20:45'},
            {'home': 'Juventus', 'away': 'Inter', 'league': 'Serie A', 'time': '20:45'}
        ]
    
    all_suggestions = []
    match_analyses = []
    
    for match in matches:
        home_team = match['home']
        away_team = match['away']
        league = match['league']
        time = match['time']
        
        # Gerar probabilidades
        probabilities = generate_probabilities(home_team, away_team)
        
        # Gerar odds
        odds = generate_odds(probabilities)
        
        # Gerar sugestões
        suggestions = generate_betting_suggestions(home_team, away_team, probabilities, odds)
        
        # Adicionar à lista de todas as sugestões
        all_suggestions.extend(suggestions)
        
        # Adicionar análise do jogo
        match_analyses.append({
            'home': home_team,
            'away': away_team,
            'league': league,
            'time': time,
            'probabilities': probabilities,
            'odds': odds
        })
    
    # Ordenar todas as sugestões por valor
    all_suggestions.sort(key=lambda x: x['value'], reverse=True)
    
    # Limitar a 10 sugestões
    top_suggestions = all_suggestions[:10]
    
    # Atualizar dados de sugestões
    betting_data['suggestions'] = top_suggestions
    
    return jsonify({
        'success': True,
        'suggestions': top_suggestions,
        'match_analyses': match_analyses
    })

# API para obter sugestões de apostas
@betting_bp.route('/api/betting/suggestions', methods=['GET'])
def get_suggestions():
    """API para obter sugestões de apostas armazenadas"""
    return jsonify({
        'success': True,
        'suggestions': betting_data['suggestions']
    })

# API para obter dados para o relatório diário
@betting_bp.route('/api/betting/daily-report', methods=['GET'])
def get_daily_report():
    """API para obter dados para o relatório diário"""
    # Gerar dados para o relatório se não houver sugestões
    if not betting_data['suggestions']:
        matches = [
            {'home': 'Manchester City', 'away': 'Liverpool', 'league': 'Premier League', 'time': '20:45'},
            {'home': 'Barcelona', 'away': 'Real Madrid', 'league': 'La Liga', 'time': '20:45'},
            {'home': 'Juventus', 'away': 'Inter', 'league': 'Serie A', 'time': '20:45'}
        ]
        
        match_analyses = []
        all_suggestions = []
        
        for match in matches:
            home_team = match['home']
            away_team = match['away']
            league = match['league']
            time = match['time']
            
            # Gerar probabilidades
            probabilities = generate_probabilities(home_team, away_team)
            
            # Gerar odds
            odds = generate_odds(probabilities)
            
            # Gerar sugestões
            suggestions = generate_betting_suggestions(home_team, away_team, probabilities, odds)
            
            # Adicionar à lista de todas as sugestões
            all_suggestions.extend(suggestions)
            
            # Adicionar análise do jogo
            match_analyses.append({
                'home': home_team,
                'away': away_team,
                'league': league,
                'time': time,
                'probabilities': probabilities,
                'odds': odds
            })
        
        # Ordenar todas as sugestões por valor
        all_suggestions.sort(key=lambda x: x['value'], reverse=True)
        
        # Limitar a 5 sugestões
        top_suggestions = all_suggestions[:5]
        
        # Atualizar dados de sugestões
        betting_data['suggestions'] = top_suggestions
    else:
        # Usar dados existentes
        top_suggestions = betting_data['suggestions']
        
        # Gerar análises de jogos
        match_analyses = []
        unique_matches = set()
        
        for suggestion in top_suggestions:
            match = suggestion['match']
            if match not in unique_matches:
                unique_matches.add(match)
                home_team, away_team = match.split(' vs ')
                
                # Determinar a liga com base nas equipas
                league = 'Premier League'
                if home_team in ['Barcelona', 'Real Madrid']:
                    league = 'La Liga'
                elif home_team in ['Juventus', 'Inter']:
                    league = 'Serie A'
                
                # Gerar probabilidades
                probabilities = generate_probabilities(home_team, away_team)
                
                # Gerar odds
                odds = generate_odds(probabilities)
                
                match_analyses.append({
                    'home': home_team,
                    'away': away_team,
                    'league': league,
                    'time': '20:45',
                    'probabilities': probabilities,
                    'odds': odds
                })
    
    # Formatar dados para o relatório
    today = datetime.datetime.now().strftime('%d/%m/%Y')
    
    report_data = {
        'date': today,
        'match_analyses': match_analyses,
        'suggestions': top_suggestions
    }
    
    return jsonify({
        'success': True,
        'report_data': report_data
    })
