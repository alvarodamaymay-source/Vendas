from flask import Flask, render_template_string, request, jsonify
import json
import os

app = Flask(__name__)

FEEDBACK_FILE = "feedbacks.json"
SUGESTOES_FILE = "sugestoes.json"

def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

html_code = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CYBER_CORE // Official Store</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Poppins', sans-serif; }
        body { background-color: #0b0713; color: #e2e8f0; line-height: 1.6; }
        header { background: #130b22; border-bottom: 1px solid #2b174a; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 18px; font-weight: 700; color: #c084fc; text-shadow: 0 0 10px rgba(192,132,252,0.4); cursor: pointer; display: flex; align-items: center; gap: 8px; transition: 0.3s; }
        .logo:hover { color: #e9d5ff; }
        .nav-links { display: flex; gap: 20px; align-items: center; flex-wrap: wrap; }
        .nav-links a { color: #cbd5e1; text-decoration: none; font-weight: 600; font-size: 14px; transition: 0.3s; cursor: pointer; display: flex; align-items: center; gap: 6px; }
        .nav-links a:hover, .nav-links a.active { color: #c084fc; text-shadow: 0 0 8px rgba(192,132,252,0.4); }
        
        .hero { text-align: center; padding: 70px 20px; background: radial-gradient(circle at center, #231245 0%, #0b0713 70%); }
        .hero h1 { font-size: 40px; color: #fff; margin-bottom: 15px; }
        .hero h1 span { color: #c084fc; }
        .hero p { font-size: 15px; color: #94a3b8; max-width: 600px; margin: 0 auto 25px auto; }
        
        .container { max-width: 1000px; margin: 0 auto; padding: 40px 20px; }
        .section-title { font-size: 24px; color: #fff; margin-bottom: 25px; text-align: center; border-bottom: 2px solid #2b174a; padding-bottom: 10px; display: flex; align-items: center; justify-content: center; gap: 10px; }
        
        .tab-content { display: none; }
        .tab-content.active { display: block; }

        .home-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-top: 20px; }
        .home-card { background: #130b22; border: 1px solid #2b174a; border-radius: 12px; padding: 25px 20px; text-align: center; cursor: pointer; transition: 0.3s; display: flex; flex-direction: column; align-items: center; justify-content: space-between; box-shadow: 0 0 15px rgba(147,51,234,0.05); }
        .home-card:hover { border-color: #9333ea; transform: translateY(-5px); box-shadow: 0 0 25px rgba(147,51,234,0.25); background: #180e2b; }
        .home-icon { font-size: 35px; margin-bottom: 12px; color: #c084fc; }
        .home-card h3 { color: #fff; font-size: 16px; margin-bottom: 8px; }
        .home-card p { color: #94a3b8; font-size: 12px; margin-bottom: 15px; }
        .home-btn { background: #2b174a; color: #c084fc; border: 1px solid #9333ea; padding: 8px 15px; border-radius: 6px; font-weight: 600; font-size: 12px; transition: 0.3s; width: 100%; }
        .home-card:hover .home-btn { background: #9333ea; color: #fff; box-shadow: 0 0 15px rgba(147,51,234,0.4); }

        .about-box { background: #130b22; border: 1px solid #2b174a; padding: 35px; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 0 20px rgba(147,51,234,0.1); }
        .about-box h3 { color: #c084fc; margin-bottom: 15px; font-size: 22px; display: flex; align-items: center; gap: 10px; }
        .about-box p { color: #94a3b8; margin-bottom: 15px; font-size: 15px; text-align: justify; }
        .about-features { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-top: 25px; }
        .feature-item { background: #0b0713; border: 1px solid #2b174a; padding: 20px; border-radius: 8px; }
        .feature-item h4 { color: #fff; margin-bottom: 8px; font-size: 16px; }
        .feature-item p { color: #94a3b8; font-size: 13px; margin: 0; }

        .products-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px; margin-bottom: 30px; }
        .product-card { background: #130b22; border: 1px solid #2b174a; padding: 25px; border-radius: 10px; display: flex; flex-direction: column; justify-content: space-between; transition: 0.3s; cursor: pointer; }
        .product-card:hover { border-color: #9333ea; box-shadow: 0 0 20px rgba(147,51,234,0.15); }
        .product-card h3 { color: #c084fc; margin-bottom: 10px; font-size: 20px; }
        .product-card p { color: #94a3b8; font-size: 14px; margin-bottom: 20px; }
        .product-price { font-size: 22px; color: #fff; font-weight: 700; margin-bottom: 20px; }

        .product-detail-view { background: #130b22; border: 1px solid #2b174a; border-radius: 12px; padding: 35px; margin-top: 30px; display: none; }
        .product-detail-view h2 { color: #c084fc; margin-bottom: 15px; font-size: 22px; }
        .product-detail-view p { color: #94a3b8; font-size: 14px; margin-bottom: 15px; text-align: justify; }
        .tutorial-box { background: #0b0713; border-left: 4px solid #9333ea; padding: 15px; margin: 15px 0; border-radius: 0 8px 8px 0; }
        .tutorial-box h4 { color: #fff; margin-bottom: 8px; font-size: 15px; }
        .tutorial-box ol { color: #94a3b8; padding-left: 20px; font-size: 13px; }
        .tutorial-box li { margin-bottom: 5px; }
        
        .btn-action { background: #9333ea; color: #fff; padding: 12px 25px; font-size: 14px; font-weight: 600; border-radius: 6px; text-decoration: none; text-align: center; box-shadow: 0 0 15px rgba(147,51,234,0.4); transition: 0.3s; display: inline-block; border: none; cursor: pointer; }
        .btn-action:hover { background: #a855f7; box-shadow: 0 0 25px rgba(168,85,247,0.7); }

        .checkout-box { background: #0b0713; border: 2px solid #9333ea; border-radius: 12px; padding: 25px; text-align: center; margin-top: 25px; display: none; box-shadow: 0 0 25px rgba(147,51,234,0.2); }
        .order-key { background: #130b22; border: 1px dashed #9333ea; padding: 12px; font-family: monospace; font-size: 13px; color: #fff; margin-bottom: 15px; border-radius: 6px; word-break: break-all; }
        .qrcode-placeholder { background: #fff; width: 180px; height: 180px; margin: 0 auto 15px auto; border-radius: 8px; display: flex; align-items: center; justify-content: center; padding: 10px; }
        .qrcode-placeholder img { width: 100%; height: 100%; }
        .btn-copy { background: #3b82f6; color: white; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-weight: 600; margin-bottom: 15px; display: inline-flex; align-items: center; gap: 6px; }
        .btn-copy:hover { background: #2563eb; }

        .btn-ja-pagou { background: none; border: none; color: #94a3b8; font-size: 13px; text-decoration: underline; cursor: pointer; margin-top: 20px; display: block; width: 100%; transition: 0.3s; }
        .btn-ja-pagou:hover { color: #c084fc; }

        .success-box { display: none; background: rgba(34, 197, 94, 0.1); border: 2px solid #22c55e; border-radius: 12px; padding: 25px; text-align: center; margin-top: 25px; box-shadow: 0 0 30px rgba(34, 197, 94, 0.25); animation: fadeIn 0.5s ease-in-out; }
        .success-box h3 { color: #22c55e; font-size: 22px; margin-bottom: 10px; display: flex; align-items: center; justify-content: center; gap: 10px; }
        .success-box p { color: #cbd5e1; font-size: 14px; margin-bottom: 20px; }
        
        .social-buttons { display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; margin-top: 15px; }
        .btn-whatsapp { background: #22c55e; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: 600; display: inline-flex; align-items: center; gap: 8px; text-decoration: none; box-shadow: 0 0 15px rgba(34,197,94,0.4); }
        .btn-whatsapp:hover { background: #16a34a; }
        .btn-discord { background: #5865F2; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: 600; display: inline-flex; align-items: center; gap: 8px; text-decoration: none; box-shadow: 0 0 15px rgba(88,101,242,0.4); }
        .btn-discord:hover { background: #4752C4; }

        /* Estilos Comuns de Abas de Listas (Feedback e Sugestões) */
        .section-container { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; align-items: start; }
        @media(max-width: 768px) { .section-container { grid-template-columns: 1fr; } }
        
        .box-panel { background: #130b22; border: 1px solid #2b174a; padding: 30px; border-radius: 12px; box-shadow: 0 0 20px rgba(147,51,234,0.1); }
        .form-group { margin-bottom: 20px; text-align: left; }
        .form-group label { display: block; color: #c084fc; font-weight: 600; margin-bottom: 8px; font-size: 14px; }
        .form-control { width: 100%; background: #0b0713; border: 1px solid #2b174a; padding: 12px; border-radius: 6px; color: #fff; font-size: 14px; outline: none; transition: 0.3s; }
        .form-control:focus { border-color: #9333ea; box-shadow: 0 0 10px rgba(147,51,234,0.3); }
        textarea.form-control { resize: vertical; min-height: 100px; }
        
        .list-box { background: #130b22; border: 1px solid #2b174a; padding: 30px; border-radius: 12px; box-shadow: 0 0 20px rgba(147,51,234,0.1); max-height: 550px; overflow-y: auto; }
        .card-item { background: #0b0713; border: 1px solid #2b174a; padding: 15px; border-radius: 8px; margin-bottom: 15px; text-align: left; }
        .card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
        .card-user { color: #c084fc; font-weight: 600; font-size: 14px; }
        .card-meta { color: #facc15; font-size: 13px; }
        .card-msg { color: #94a3b8; font-size: 13px; word-break: break-all; margin-bottom: 12px; }
        
        .vote-buttons { display: flex; gap: 10px; align-items: center; }
        .btn-vote { background: #1f1435; border: 1px solid #2b174a; color: #cbd5e1; padding: 5px 12px; border-radius: 6px; cursor: pointer; font-size: 12px; font-weight: 600; display: inline-flex; align-items: center; gap: 5px; transition: 0.3s; }
        .btn-vote.approve:hover, .btn-vote.approve.voted { background: rgba(34, 197, 94, 0.2); border-color: #22c55e; color: #22c55e; }
        .btn-vote.reject:hover, .btn-vote.reject.voted { background: rgba(239, 68, 68, 0.2); border-color: #ef4444; color: #ef4444; }

        footer { text-align: center; padding: 25px; color: #64748b; font-size: 13px; border-top: 1px solid #2b174a; background: #130b22; margin-top: 50px; }

        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
    <header>
        <div class="logo" onclick="switchTab('home', this)">🏠 <span>Página Principal</span></div>
        <div class="nav-links">
            <a onclick="switchTab('home', this)" id="link-home" class="active">🏠 Início</a>
            <a onclick="switchTab('quem-somos', this)" id="link-quem-somos">ℹ️ Quem Somos</a>
            <a onclick="switchTab('produtos', this)" id="link-produtos">📦 Produtos</a>
            <a onclick="switchTab('feedback', this)" id="link-feedback">💬 Feedback</a>
            <a onclick="switchTab('sugestoes', this)" id="link-sugestoes">💡 Sugestões</a>
        </div>
    </header>

    <div class="hero">
        <h1>CYBER_CORE // <span>Official Hub</span></h1>
        <p>Selecione seu produto, conheça nossa estrutura ou envie sua avaliação e sugestões.</p>
    </div>

    <div class="container">
        <!-- ABA INÍCIO -->
        <div id="home" class="tab-content active">
            <h2 class="section-title">⚡ Painel de Navegação Oficial</h2>
            <div class="home-grid">
                <div class="home-card" onclick="switchTab('produtos', document.getElementById('link-produtos'))">
                    <div class="home-icon">📦</div>
                    <h3>Produtos</h3>
                    <p>Explore nosso painel profissional.</p>
                    <button class="home-btn">Loja →</button>
                </div>
                <div class="home-card" onclick="switchTab('quem-somos', document.getElementById('link-quem-somos'))">
                    <div class="home-icon">ℹ️</div>
                    <h3>Sobre</h3>
                    <p>Conheça nossa missão.</p>
                    <button class="home-btn">Detalhes →</button>
                </div>
                <div class="home-card" onclick="switchTab('feedback', document.getElementById('link-feedback'))">
                    <div class="home-icon">💬</div>
                    <h3>Feedback</h3>
                    <p>Deixe sua opinião.</p>
                    <button class="home-btn">Avaliar →</button>
                </div>
                <div class="home-card" onclick="switchTab('sugestoes', document.getElementById('link-sugestoes'))">
                    <div class="home-icon">💡</div>
                    <h3>Sugestões</h3>
                    <p>Envie ideias e vote.</p>
                    <button class="home-btn">Sugerir →</button>
                </div>
            </div>
        </div>

        <!-- ABA QUEM SOMOS -->
        <div id="quem-somos" class="tab-content">
            <div class="about-box">
                <h3>ℹ️ Quem Somos & Nossa Missão</h3>
                <p>A <strong>CYBER_CORE</strong> é uma organização especializada no desenvolvimento de soluções de software de alta performance, automação de sistemas e ferramentas avançadas de monitoramento digital. Nosso foco principal é entregar interfaces robustas, seguras e com design moderno para atender projetos de grande exigência técnica.</p>
                <p>Fundada com o objetivo de otimizar processos e criar ecossistemas digitais eficientes, nossa equipe combina engenharia de software de ponta com um layout inspirado em estética cyberpunk e futurista.</p>
                
                <div class="about-features">
                    <div class="feature-item">
                        <h4>⚡ Alta Performance</h4>
                        <p>Sistemas otimizados para rodar sem travar, garantindo resposta imediata em qualquer operação.</p>
                    </div>
                    <div class="feature-item">
                        <h4>🔒 Segurança Avançada</h4>
                        <p>Arquitetura estruturada para proteger dados e manter a integridade dos ambientes gerenciados.</p>
                    </div>
                    <div class="feature-item">
                        <h4>🛠️ Suporte Direto</h4>
                        <p>Atendimento ágil e especializado via Discord e WhatsApp para auxiliar em qualquer configuração.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- ABA PRODUTOS -->
        <div id="produtos" class="tab-content">
            <h2 class="section-title">📦 Escolha sua Ferramenta</h2>
            <div class="products-grid">
                <div class="product-card" onclick="mostrarDetalhesPainel()">
                    <div>
                        <h3>⚡ Painel de Monitoramento v1.0</h3>
                        <p>Acesso completo ao sistema de rastreamento em tempo real com interface camuflada.</p>
                    </div>
                    <div>
                        <div class="product-price">R$ 25,00</div>
                        <span class="btn-action" style="display:block; text-align:center; padding: 8px;">VER DETALHES & COMPRAR</span>
                    </div>
                </div>

                <div class="product-card" onclick="mostrarDetalhesXit()">
                    <div>
                        <h3>🚀 XIT de SAMP (Em Breve)</h3>
                        <p>A ferramenta definitiva para San Andreas Multiplayer com recursos avançados.</p>
                    </div>
                    <div>
                        <div class="product-price" style="color: #94a3b8; font-size: 18px;">EM BREVE</div>
                        <span class="btn-action" style="display:block; text-align:center; padding: 8px; background: #2b174a; color: #c084fc;">SABER MAIS</span>
                    </div>
                </div>
            </div>

            <div id="painel-detail" class="product-detail-view">
                <h2>⚡ Detalhes do Painel de Monitoramento v1.0</h2>
                <p>O <strong>Painel de Monitoramento</strong> foi desenvolvido com foco em alta eficiência e discrição. Ele permite o acompanhamento detalhado de dados e métricas em tempo real, contando com uma interface limpa, moderna e otimizada para uso profissional.</p>
                
                <div class="tutorial-box">
                    <h4>🛠️ Tutorial de Instruções e Uso:</h4>
                    <ol>
                        <li>Realize o pagamento via Pix utilizando o QR Code ou a chave abaixo.</li>
                        <li>Clique no botão "Já pagou?" para liberar o envio do comprovante para nossa equipe.</li>
                        <li>Após a confirmação, você receberá o arquivo executável e a chave de ativação diretamente no seu WhatsApp ou Discord.</li>
                        <li>Extraia o arquivo baixado para uma pasta de sua preferência, execute como Administrador e insira sua chave de acesso.</li>
                    </ol>
                </div>

                <div style="text-align: center; margin-top: 25px;">
                    <button class="btn-action" onclick="mostrarCheckout()">REALIZAR PAGAMENTO (R$ 25,00)</button>
                </div>

                <div id="checkout-section" class="checkout-box">
                    <h3 style="color: #fff; margin-bottom: 10px;">💳 Pagamento via Pix</h3>
                    <p style="color: #94a3b8; font-size: 13px; margin-bottom: 15px;">Escaneie o QR Code ou copie a chave abaixo:</p>
                    
                    <div class="qrcode-placeholder">
                        <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=00020126580014BR.GOV.BCB.PIX0136300108b6-bf51-4a92-bb5f-bcceb7bf1c99520400005303986540525.005802BR5925Alvaro Gabriel de Freitas6009SAO PAULO62140510Qe33xCiBEh630438DA" alt="QR Code Pix">
                    </div>
                    
                    <div class="order-key" id="pixKey">300108b6-bf51-4a92-bb5f-bcceb7bf1c99</div>
                    <button class="btn-copy" onclick="copyPix()">📋 Copiar Chave Pix</button>

                    <button class="btn-ja-pagou" onclick="liberarTelaSucesso()">Já pagou? Clique aqui para ver as opções</button>

                    <div id="success-box" class="success-box">
                        <h3>✅ Pagamento Confirmado!</h3>
                        <p>Agora escolha onde deseja enviar o comprovante com a nossa equipe:</p>
                        <div class="social-buttons">
                            <a href="https://wa.me/5538998661085?text=Ol%C3%A1!%20Paguei%20o%20Painel%20de%20Monitoramento.%20Segue%20o%20comprovante:" target="_blank" class="btn-whatsapp">
                                💬 WhatsApp da Equipe
                            </a>
                            <a href="https://discord.com/users/alvaro._.kk" target="_blank" class="btn-discord">
                                🎮 Discord Oficial
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <div id="xit-detail" class="product-detail-view">
                <h2>🚀 XIT de SAMP (Em Breve)</h2>
                <p>O aguardado <strong>XIT de SAMP</strong> está em fase avançada de testes e desenvolvimento pela nossa equipe. O projeto trará recursos exclusivos de otimização, ferramentas de assistência de mira e bypass atualizado para os principais servidores.</p>
                
                <div class="tutorial-box">
                    <h4>📌 O que esperar do lançamento:</h4>
                    <ol>
                        <li>Interface totalmente integrada ao cliente do jogo.</li>
                        <li>Configurações personalizadas salvas diretamente em nuvem/perfil.</li>
                        <li>Atualizações frequentes focadas em estabilidade e segurança contra detecções.</li>
                    </ol>
                </div>
                <p style="color: #c084fc; font-weight: 600; text-align: center; margin-top: 15px;">Fique atento ao nosso Discord e redes oficiais para o anúncio da data de lançamento!</p>
            </div>
        </div>

        <!-- ABA FEEDBACK -->
        <div id="feedback" class="tab-content">
            <h2 class="section-title">💬 Central de Feedback</h2>
            <div class="section-container">
                <div class="box-panel">
                    <h3 style="color: #c084fc; margin-bottom: 15px; font-size: 20px;">Deixe sua Opinião</h3>
                    <p style="color: #94a3b8; font-size: 13px; margin-bottom: 20px;">Sua avaliação fica salva publicamente para todos os visitantes do site.</p>
                    
                    <form onsubmit="enviarFeedback(event)">
                        <div class="form-group">
                            <label for="fb-nome">Seu Nome / Apelido:</label>
                            <input type="text" id="fb-nome" class="form-control" placeholder="Ex: Player_X" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="fb-nota">Avaliação Geral:</label>
                            <select id="fb-nota" class="form-control" required>
                                <option value="" disabled selected>Selecione uma nota</option>
                                <option value="5">⭐⭐⭐⭐⭐ Excelente</option>
                                <option value="4">⭐⭐⭐⭐ Muito Bom</option>
                                <option value="3">⭐⭐⭐ Bom</option>
                                <option value="2">⭐⭐ Regular</option>
                                <option value="1">⭐ Ruim</option>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="fb-mensagem">Comentário:</label>
                            <textarea id="fb-mensagem" class="form-control" placeholder="O que achou do sistema..." required></textarea>
                        </div>

                        <button type="submit" class="btn-action" style="width: 100%;">Enviar Feedback 🚀</button>
                    </form>
                </div>

                <div class="list-box">
                    <h3 style="color: #c084fc; margin-bottom: 15px; font-size: 20px; text-align: center;">Mural da Comunidade</h3>
                    <div id="lista-feedbacks"></div>
                </div>
            </div>
        </div>

        <!-- ABA SUGESTÕES E MELHORIAS -->
        <div id="sugestoes" class="tab-content">
            <h2 class="section-title">💡 Sugestões e Melhorias</h2>
            <div class="section-container">
                <div class="box-panel">
                    <h3 style="color: #c084fc; margin-bottom: 15px; font-size: 20px;">Envie sua Ideia</h3>
                    <p style="color: #94a3b8; font-size: 13px; margin-bottom: 20px;">Fale o que você sugere para lancarmos ou melhorar em nossos produtos já lançados.</p>
                    
                    <form onsubmit="enviarSugestao(event)">
                        <div class="form-group">
                            <label for="sug-nome">Seu Nome / Apelido:</label>
                            <input type="text" id="sug-nome" class="form-control" placeholder="Ex: Dev_Master" required>
                        </div>

                        <div class="form-group">
                            <label for="sug-mensagem">Sua Sugestão / Melhoria:</label>
                            <textarea id="sug-mensagem" class="form-control" placeholder="Descreva o que gostaria de ver no sistema..." required></textarea>
                        </div>

                        <button type="submit" class="btn-action" style="width: 100%;">Enviar Sugestão 💡</button>
                    </form>
                </div>

                <div class="list-box">
                    <h3 style="color: #c084fc; margin-bottom: 15px; font-size: 20px; text-align: center;">Mural de Sugestões</h3>
                    <div id="lista-sugestoes"></div>
                </div>
            </div>
        </div>
    </div>

    <footer>CYBER_CORE SYSTEM © 2026</footer>

    <script>
        function switchTab(tabId, element) {
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            document.querySelectorAll('.nav-links a').forEach(l => l.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            if(element) element.classList.add('active');
            window.scrollTo({ top: 0, behavior: 'smooth' });
            if(tabId === 'feedback') carregarFeedbacks();
            if(tabId === 'sugestoes') carregarSugestoes();
        }

        function mostrarDetalhesPainel() {
            document.getElementById("painel-detail").style.display = "block";
            document.getElementById("xit-detail").style.display = "none";
            document.getElementById("painel-detail").scrollIntoView({ behavior: 'smooth' });
        }

        function mostrarDetalhesXit() {
            document.getElementById("xit-detail").style.display = "block";
            document.getElementById("painel-detail").style.display = "none";
            document.getElementById("xit-detail").scrollIntoView({ behavior: 'smooth' });
        }

        function mostrarCheckout() {
            var box = document.getElementById("checkout-section");
            box.style.display = "block";
            box.scrollIntoView({ behavior: 'smooth' });
        }

        function copyPix() {
            navigator.clipboard.writeText(document.getElementById("pixKey").innerText);
            alert("Chave Pix copiada!");
        }

        function liberarTelaSucesso() {
            document.getElementById("success-box").style.display = "block";
            document.getElementById("success-box").scrollIntoView({ behavior: 'smooth' });
        }

        // --- FEEDBACKS ---
        function enviarFeedback(event) {
            event.preventDefault();
            const nome = document.getElementById("fb-nome").value;
            const nota = document.getElementById("fb-nota").value;
            const mensagem = document.getElementById("fb-mensagem").value;

            fetch('/api/feedback', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ nome, nota, mensagem })
            })
            .then(response => response.json())
            .then(data => {
                if(data.sucesso) {
                    alert("Feedback enviado com sucesso!");
                    event.target.reset();
                    carregarFeedbacks();
                }
            });
        }

        function carregarFeedbacks() {
            fetch('/api/feedback')
            .then(response => response.json())
            .then(data => {
                const container = document.getElementById("lista-feedbacks");
                container.innerHTML = "";
                if(data.length === 0) {
                    container.innerHTML = '<p style="color: #64748b; text-align: center; font-size: 13px;">Nenhum feedback enviado ainda.</p>';
                    return;
                }
                data.forEach(item => {
                    let estrelas = "⭐".repeat(parseInt(item.nota));
                    container.innerHTML += `
                        <div class="card-item">
                            <div class="card-header">
                                <span class="card-user">${item.nome}</span>
                                <span class="card-meta">${estrelas}</span>
                            </div>
                            <div class="card-msg">${item.mensagem}</div>
                        </div>
                    `;
                });
            });
        }

        // --- SUGESTÕES ---
        function enviarSugestao(event) {
            event.preventDefault();
            const nome = document.getElementById("sug-nome").value;
            const mensagem = document.getElementById("sug-mensagem").value;

            fetch('/api/sugestoes', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ nome, mensagem })
            })
            .then(response => response.json())
            .then(data => {
                if(data.sucesso) {
                    alert("Sugestão enviada com sucesso!");
                    event.target.reset();
                    carregarSugestoes();
                }
            });
        }

        function votarSugestao(id, tipo) {
            fetch('/api/sugestoes/votar', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id, tipo })
            })
            .then(response => response.json())
            .then(data => {
                if(data.sucesso) {
                    carregarSugestoes();
                }
            });
        }

        function carregarSugestoes() {
            fetch('/api/sugestoes')
            .then(response => response.json())
            .then(data => {
                const container = document.getElementById("lista-sugestoes");
                container.innerHTML = "";
                if(data.length === 0) {
                    container.innerHTML = '<p style="color: #64748b; text-align: center; font-size: 13px;">Nenhuma sugestão enviada ainda. Seja o primeiro!</p>';
                    return;
                }
                data.forEach(item => {
                    let aprovado = item.aprovados || 0;
                    let rejeitado = item.rejeitados || 0;
                    container.innerHTML += `
                        <div class="card-item">
                            <div class="card-header">
                                <span class="card-user">${item.nome}</span>
                            </div>
                            <div class="card-msg">${item.mensagem}</div>
                            <div class="vote-buttons">
                                <button class="btn-vote approve" onclick="votarSugestao(${item.id}, 'aprovar')">✅ Aprovar (${aprovado})</button>
                                <button class="btn-vote reject" onclick="votarSugestao(${item.id}, 'rejeitar')">❌ Não Aprovar (${rejeitado})</button>
                            </div>
                        </div>
                    `;
                });
            });
        }

        window.onload = function() {
            carregarFeedbacks();
            carregarSugestoes();
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_code)

@app.route('/api/feedback', methods=['GET', 'POST'])
def api_feedback():
    if request.method == 'POST':
        dados = request.get_json()
        if dados:
            feedbacks = carregar_dados(FEEDBACK_FILE)
            feedbacks.insert(0, dados)
            salvar_dados(FEEDBACK_FILE, feedbacks)
            return jsonify({"sucesso": True})
        return jsonify({"sucesso": False})
    else:
        return jsonify(carregar_dados(FEEDBACK_FILE))

@app.route('/api/sugestoes', methods=['GET', 'POST'])
def api_sugestoes():
    if request.method == 'POST':
        dados = request.get_json()
        if dados:
            sugestoes = carregar_dados(SUGESTOES_FILE)
            dados['id'] = len(sugestoes) + 1
            dados['aprovados'] = 0
            dados['rejeitados'] = 0
            sugestoes.insert(0, dados)
            salvar_dados(SUGESTOES_FILE, sugestoes)
            return jsonify({"sucesso": True})
        return jsonify({"sucesso": False})
    else:
        return jsonify(carregar_dados(SUGESTOES_FILE))

@app.route('/api/sugestoes/votar', methods=['POST'])
def api_votar_sugestao():
    dados = request.get_json()
    if dados:
        sugestoes = carregar_dados(SUGESTOES_FILE)
        for item in sugestoes:
            if item['id'] == dados['id']:
                if dados['tipo'] == 'aprovar':
                    item['aprovados'] = item.get('aprovados', 0) + 1
                elif dados['tipo'] == 'rejeitar':
                    item['rejeitados'] = item.get('rejeitados', 0) + 1
                break
        salvar_dados(SUGESTOES_FILE, sugestoes)
        return jsonify({"sucesso": True})
    return jsonify({"sucesso": False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
