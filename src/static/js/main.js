// JavaScript principal para o FC Statistics

document.addEventListener('DOMContentLoaded', function() {
    // Definir a data atual no seletor de data
    const today = new Date();
    const formattedDate = today.toISOString().split('T')[0];
    const dateSelector = document.getElementById('date-selector');
    
    if (dateSelector) {
        dateSelector.value = formattedDate;
        dateSelector.addEventListener('change', loadGames);
    }
    
    // Carregar jogos do dia
    loadGames();
    
    // Inicializar tooltips e popovers do Bootstrap
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

// Função para carregar jogos do dia
function loadGames() {
    const jogosContainer = document.getElementById('jogos-container');
    const dateSelector = document.getElementById('date-selector');
    
    if (!jogosContainer) return;
    
    // Mostrar spinner de carregamento
    jogosContainer.innerHTML = `
        <div class="col-12 text-center">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Carregando...</span>
            </div>
        </div>
    `;
    
    // Parâmetro de data (se disponível)
    const dataParam = dateSelector ? `?data=${dateSelector.value}` : '';
    
    // Simular chamada à API (em produção, substituir por fetch real)
    setTimeout(() => {
        // Dados simulados - em produção, estes viriam da API
        const jogos = [
            {
                id: 1,
                data: '2025-05-22',
                campeonato: 'Premier League',
                casa: 'Manchester City',
                fora: 'Liverpool',
                odds_casa: 1.85,
                odds_empate: 3.50,
                odds_fora: 4.20,
                previsao_gols: 'Over 2.5',
                previsao_cantos: '10-12',
                previsao_cartoes: '3-5'
            },
            {
                id: 2,
                data: '2025-05-22',
                campeonato: 'La Liga',
                casa: 'Barcelona',
                fora: 'Real Madrid',
                odds_casa: 2.10,
                odds_empate: 3.30,
                odds_fora: 3.40,
                previsao_gols: 'Over 2.5',
                previsao_cantos: '9-11',
                previsao_cartoes: '4-6'
            },
            {
                id: 3,
                data: '2025-05-22',
                campeonato: 'Serie A',
                casa: 'Juventus',
                fora: 'Inter',
                odds_casa: 2.25,
                odds_empate: 3.10,
                odds_fora: 3.30,
                previsao_gols: 'Under 2.5',
                previsao_cantos: '8-10',
                previsao_cartoes: '5-7'
            }
        ];
        
        // Limpar o container
        jogosContainer.innerHTML = '';
        
        // Se não houver jogos
        if (jogos.length === 0) {
            jogosContainer.innerHTML = `
                <div class="col-12">
                    <div class="alert alert-info">
                        Não há jogos disponíveis para esta data.
                    </div>
                </div>
            `;
            return;
        }
        
        // Renderizar os jogos
        jogos.forEach(jogo => {
            const jogoCard = document.createElement('div');
            jogoCard.className = 'col-md-4 mb-4';
            jogoCard.innerHTML = `
                <div class="card game-card">
                    <div class="card-header">
                        <span class="league-name">${jogo.campeonato}</span>
                        <span class="game-time">20:45</span>
                    </div>
                    <div class="card-body">
                        <div class="teams">
                            <div class="home-team">${jogo.casa}</div>
                            <div class="vs">vs</div>
                            <div class="away-team">${jogo.fora}</div>
                        </div>
                        <div class="odds-container mt-3">
                            <div class="odds-item">
                                <span class="odds-label">1</span>
                                <span class="odds-value">${jogo.odds_casa}</span>
                            </div>
                            <div class="odds-item">
                                <span class="odds-label">X</span>
                                <span class="odds-value">${jogo.odds_empate}</span>
                            </div>
                            <div class="odds-item">
                                <span class="odds-label">2</span>
                                <span class="odds-value">${jogo.odds_fora}</span>
                            </div>
                        </div>
                        <div class="predictions mt-3">
                            <div class="prediction-item">
                                <span class="prediction-label">Golos:</span>
                                <span class="prediction-value">${jogo.previsao_gols}</span>
                            </div>
                            <div class="prediction-item">
                                <span class="prediction-label">Cantos:</span>
                                <span class="prediction-value">${jogo.previsao_cantos}</span>
                            </div>
                            <div class="prediction-item">
                                <span class="prediction-label">Cartões:</span>
                                <span class="prediction-value">${jogo.previsao_cartoes}</span>
                            </div>
                        </div>
                    </div>
                    <div class="card-footer">
                        <a href="/relatorios?jogo=${jogo.id}" class="btn btn-sm btn-outline-primary w-100">Ver Análise Completa</a>
                    </div>
                </div>
            `;
            jogosContainer.appendChild(jogoCard);
        });
        
        // Adicionar estilos CSS para os cards de jogos
        const style = document.createElement('style');
        style.textContent = `
            .game-card {
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                height: 100%;
            }
            
            .game-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
            }
            
            .card-header {
                background-color: #f3f4f6;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0.7rem 1rem;
            }
            
            .league-name {
                font-weight: 600;
                color: var(--primary-color);
                font-size: 0.9rem;
            }
            
            .game-time {
                font-size: 0.8rem;
                color: #6b7280;
            }
            
            .teams {
                text-align: center;
                margin-bottom: 1rem;
            }
            
            .home-team, .away-team {
                font-weight: 600;
                font-size: 1.1rem;
                color: var(--dark-color);
            }
            
            .vs {
                font-size: 0.9rem;
                color: #6b7280;
                margin: 0.3rem 0;
            }
            
            .odds-container {
                display: flex;
                justify-content: space-between;
                background-color: #f3f4f6;
                border-radius: 6px;
                padding: 0.5rem;
            }
            
            .odds-item {
                text-align: center;
                flex: 1;
            }
            
            .odds-label {
                display: block;
                font-size: 0.8rem;
                color: #6b7280;
            }
            
            .odds-value {
                display: block;
                font-weight: 700;
                color: var(--primary-color);
            }
            
            .predictions {
                display: flex;
                flex-direction: column;
                gap: 0.5rem;
            }
            
            .prediction-item {
                display: flex;
                justify-content: space-between;
                font-size: 0.9rem;
            }
            
            .prediction-label {
                color: #6b7280;
            }
            
            .prediction-value {
                font-weight: 600;
            }
            
            .card-footer {
                background-color: white;
                border-top: 1px solid #e5e7eb;
                padding: 1rem;
            }
        `;
        document.head.appendChild(style);
        
    }, 1000); // Simular tempo de carregamento
}
