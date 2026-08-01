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
        .nav-links { display: flex; gap: 25px; align-items: center; }
        .nav-links a { color: #cbd5e1; text-decoration: none; font-weight: 600; font-size: 14px; transition: 0.3s; cursor: pointer; display: flex; align-items: center; gap: 6px; }
        .nav-links a:hover, .nav-links a.active { color: #c084fc; text-shadow: 0 0 8px rgba(192,132,252,0.4); }
        
        .hero { text-align: center; padding: 70px 20px; background: radial-gradient(circle at center, #231245 0%, #0b0713 70%); }
        .hero h1 { font-size: 40px; color: #fff; margin-bottom: 15px; }
        .hero h1 span { color: #c084fc; }
        .hero p { font-size: 15px; color: #94a3b8; max-width: 600px; margin: 0 auto 25px auto; }
        
        .container { max-width: 1000px; margin: 0 auto; padding: 40px 20px; }
        .section-title { font-size: 24px; color: #fff; margin-bottom: 25px; text-align: center; border-bottom: 2px solid #2b174a; padding-bottom: 10px; display: flex; align-items: center; justify-content: center; gap: 10px; }
        
        /* Abas (Tabs) Conteúdo */
        .tab-content { display: none; }
        .tab-content.active { display: block; }

        /* Janelas da Página Principal (Home) */
        .home-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; margin-top: 20px; }
        .home-card { background: #130b22; border: 1px solid #2b174a; border-radius: 12px; padding: 35px 25px; text-align: center; cursor: pointer; transition: 0.3s; display: flex; flex-direction: column; align-items: center; justify-content: space-between; box-shadow: 0 0 15px rgba(147,51,234,0.05); }
        .home-card:hover { border-color: #9333ea; transform: translateY(-5px); box-shadow: 0 0 25px rgba(147,51,234,0.25); background: #180e2b; }
        .home-icon { font-size: 45px; margin-bottom: 20px; color: #c084fc; }
        .home-card h3 { color: #fff; font-size: 20px; margin-bottom: 12px; }
        .home-card p { color: #94a3b8; font-size: 14px; margin-bottom: 25px; }
        .home-btn { background: #2b174a; color: #c084fc; border: 1px solid #9333ea; padding: 10px 20px; border-radius: 6px; font-weight: 600; font-size: 13px; transition: 0.3s; width: 100%; }
        .home-card:hover .home-btn { background: #9333ea; color: #fff; box-shadow: 0 0 15px rgba(147,51,234,0.4); }

        /* Quem Somos */
        .about-box { background: #130b22; border: 1px solid #2b174a; padding: 35px; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 0 20px rgba(147,51,234,0.1); }
        .about-box h3 { color: #c084fc; margin-bottom: 15px; font-size: 22px; display: flex; align-items: center; gap: 10px; }
        .about-box p { color: #94a3b8; margin-bottom: 15px; font-size: 15px; }

        /* Grid de Produtos */
        .products-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px; margin-bottom: 30px; }
        .product-card { background: #130b22; border: 1px solid #2b174a; padding: 25px; border-radius: 10px; display: flex; flex-direction: column; justify-content: space-between; transition: 0.3s; cursor: pointer; }
        .product-card:hover { border-color: #9333ea; box-shadow: 0 0 20px rgba(147,51,234,0.15); }
        .product-card h3 { color: #c084fc; margin-bottom: 10px; font-size: 20px; }
        .product-card p { color: #94a3b8; font-size: 14px; margin-bottom: 20px; }
        .product-price { font-size: 22px; color: #fff; font-weight: 700; margin-bottom: 20px; }
        .badge-coming { background: #2b174a; color: #c084fc; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 600; display: inline-block; margin-bottom: 15px; }

        /* Detalhes do Produto / Checkout */
        .product-detail-view { background: #130b22; border: 1px solid #2b174a; border-radius: 12px; padding: 35px; margin-top: 30px; display: none; }
        .product-detail-view h2 { color: #fff; margin-bottom: 15px; font-size: 24px; color: #c084fc; }
        .product-detail-view p { color: #94a3b8; margin-bottom: 20px; font-size: 15px; }
        
        .btn-action { background: #9333ea; color: #fff; padding: 12px 25px; font-size: 14px; font-weight: 600; border-radius: 6px; text-decoration: none; text-align: center; box-shadow: 0 0 15px rgba(147,51,234,0.4); transition: 0.3s; display: inline-block; border: none; cursor: pointer; }
        .btn-action:hover { background: #a855f7; box-shadow: 0 0 25px rgba(168,85,247,0.7); }

        .tutorial-container { background: #0b0713; border: 1px dashed #4c1d95; padding: 20px; border-radius: 8px; margin-bottom: 25px; }
        .tutorial-container h4 { color: #fff; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
        .tutorial-container a { color: #c084fc; text-decoration: underline; font-weight: 600; display: inline-flex; align-items: center; gap: 6px; }

        /* Área de Pagamento Pix */
        .checkout-box { background: #0b0713; border: 2px solid #9333ea; border-radius: 12px; padding: 25px; text-align: center; margin-top: 25px; display: none; box-shadow: 0 0 25px rgba(147,51,234,0.2); }
        .order-key { background: #130b22; border: 1px dashed #9333ea; padding: 12px; font-family: monospace; font-size: 14px; color: #fff; margin-bottom: 20px; border-radius: 6px; word-break: break-all; }
        .qrcode-placeholder { background: #fff; width: 180px; height: 180px; margin: 0 auto 20px auto; border-radius: 8px; display: flex; align-items: center; justify-content: center; padding: 10px; }
        .qrcode-placeholder img { width: 100%; height: 100%; }
        .btn-copy { background: #3b82f6; color: white; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-weight: 600; margin-top: 10px; display: inline-flex; align-items: center; gap: 6px; }
        .btn-copy:hover { background: #2563eb; }

        /* Feedbacks */
        .reviews-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 40px; }
        .review-card { background: #130b22; border: 1px solid #2b174a; padding: 20px; border-radius: 10px; }
        .review-author { color: #c084fc; font-weight: 600; margin-bottom: 5px; font-size: 14px; display: flex; justify-content: space-between; align-items: center; }
        .stars { color: #fbbf24; font-size: 14px; }
        .review-text { color: #cbd5e1; font-size: 13px; margin-top: 10px; }

        .feedback-form-box { background: #130b22; border: 1px solid #2b174a; padding: 30px; border-radius: 12px; max-width: 600px; margin: 0 auto; }
        .feedback-form-box h3 { color: #fff; margin-bottom: 20px; font-size: 20px; text-align: center; display: flex; align-items: center; justify-content: center; gap: 8px; }
        .form-group { margin-bottom: 15px; }
        .form-group label { display: block; color: #94a3b8; font-size: 13px; margin-bottom: 5px; }
        .form-group input, .form-group select, .form-group textarea { width: 100%; padding: 10px; background: #0b0713; border: 1px solid #2b174a; color: #fff; border-radius: 6px; font-family: 'Poppins', sans-serif; font-size: 14px; }
        .form-group input:focus, .form-group select:focus, .form-group textarea:focus { border-color: #9333ea; outline: none; }

        footer { text-align: center; padding: 25px; color: #64748b; font-size: 13px; border-top: 1px solid #2b174a; background: #130b22; margin-top: 50px; }
    </style>
</head>
<body>
    <header>
        <div class="logo" onclick="switchTab('home', this)">
            🏠 <span>Página Principal</span>
        </div>
        <div class="nav-links">
            <a onclick="switchTab('home', this)" id="link-home" class="active">🏠 Início</a>
            <a onclick="switchTab('quem-somos', this)" id="link-quem-somos">ℹ️ Quem Somos</a>
            <a onclick="switchTab('produtos', this)" id="link-produtos">📦 Produtos</a>
            <a onclick="switchTab('feedback', this)" id="link-feedback">💬 Avaliações</a>
        </div>
    </header>

    <div class="hero">
        <h1 id="hero-title">CYBER_CORE // <span>Official Hub</span></h1>
        <p id="hero-desc">Selecione uma das opções abaixo ou navegue pelo menu superior para explorar nossos sistemas.</p>
    </div>

    <div class="container">
        <!-- ABA: PÁGINA PRINCIPAL (Janelas Iniciais) -->
        <div id="home" class="tab-content active">
            <h2 class="section-title">⚡ Painel de Navegação Oficial</h2>
            <div class="home-grid">
                <div class="home-card" onclick="switchTab('quem-somos', document.getElementById('link-quem-somos'))">
                    <div class="home-icon">ℹ️</div>
                    <h3>Quem Somos</h3>
                    <p>Conheça nossa história, equipe, missão e os pilares tecnológicos por trás dos nossos sistemas avançados.</p>
                    <button class="home-btn">Acessar Seção →</button>
                </div>

                <div class="home-card" onclick="switchTab('produtos', document.getElementById('link-produtos'))">
                    <div class="home-icon">📦</div>
                    <h3>Produtos & Ferramentas</h3>
                    <p>Explore nossos painéis de monitoramento profissional, tutoriais passo a passo e lançamentos futuros.</p>
                    <button class="home-btn">Acessar Loja →</button>
                </div>

                <div class="home-card" onclick="switchTab('feedback', document.getElementById('link-feedback'))">
                    <div class="home-icon">💬</div>
                    <h3>Avaliações & Feedback</h3>
                    <p>Veja comentários reais de nossa comunidade de usuários e compartilhe sua própria experiência com notas e estrelas.</p>
                    <button class="home-btn">Acessar Avaliações →</button>
                </div>
            </div>
        </div>

        <!-- ABA: QUEM SOMOS -->
        <div id="quem-somos" class="tab-content">
            <div class="about-box">
                <h3>ℹ️ O que é a Cyber Core?</h3>
                <p>A <strong>Cyber Core</strong> é uma organização de desenvolvimento de software e automação de alta performance focada em criar ferramentas robustas, seguras e eficientes para o ecossistema gamer e de monitoramento digital.</p>
                <p>Nossa missão é entregar soluções de ponta com interfaces camufladas, alta estabilidade, atualizações constantes e suporte dedicado para garantir a melhor experiência e performance para nossos usuários.</p>
            </div>
            <div class="about-box">
                <h3>🚀 Nossos Pilares Tecnológicos</h3>
                <p>⚡ <strong>Performance Extrema:</strong> Códigos otimizados para rodar sem travamentos ou sobrecarga no sistema operacional.</p>
                <p>🛡️ <strong>Segurança e Discrição:</strong> Sistemas camuflados com protocolos avançados para total privacidade e estabilidade.</p>
                <p>🤝 <strong>Suporte Vitalício:</strong> Comunidade ativa e atualizações constantes para todas as nossas ferramentas oficiais.</p>
            </div>
        </div>

        <!-- ABA: PRODUTOS -->
        <div id="produtos" class="tab-content">
            <h2 class="section-title">📦 Escolha sua Ferramenta</h2>
            <div class="products-grid">
                <!-- Produto 1: Painel de Monitoramento -->
                <div class="product-card" onclick="selectProduct('monitoramento')">
                    <div>
                        <h3>⚡ Painel de Monitoramento v1.0</h3>
                        <p>Acesso completo ao sistema de rastreamento em tempo real com interface camuflada, radar e atualizações vitalícias.</p>
                    </div>
                    <div>
                        <div class="product-price">R$ 25,00</div>
                        <span class="btn-action" style="display:block; text-align:center; padding: 8px;">VER DETALHES & TUTORIAL</span>
                    </div>
                </div>

                <!-- Produto 2: Painel Xit SAMP -->
                <div class="product-card" onclick="selectProduct('samp')">
                    <div>
                        <span class="badge-coming">🚧 AINDA POR VIR...</span>
                        <h3>🎮 Painel Xit SAMP</h3>
                        <p>A próxima evolução para San Andreas Multiplayer. Ferramenta avançada em desenvolvimento com recursos exclusivos.</p>
                    </div>
                    <div>
                        <div class="product-price" style="color: #64748b; font-size: 18px;">Em Breve</div>
                        <span class="btn-action" style="display:block; text-align:center; padding: 8px; background: #2b174a;">VER MAIS</span>
                    </div>
                </div>
            </div>

            <!-- DETALHES DO PRODUTO 1 (Monitoramento) -->
            <div id="detail-monitoramento" class="product-detail-view">
                <h2>⚡ Painel de Monitoramento v1.0</h2>
                <p>Ferramenta profissional desenvolvida para rastreamento avançado em tempo real com alta precisão e painel camuflado.</p>
                
                <div class="tutorial-container">
                    <h4>📘 Tutorial & Explicação de Uso</h4>
                    <p style="color: #94a3b8; font-size: 14px; margin-bottom: 10px;">Assista ao guia completo em vídeo para configurar e operar o sistema em menos de 5 minutos:</p>
                    <a href="https://www.youtube.com/watch?v=_Nlb0CzPxF8" target="_blank">▶ ACESSAR VÍDEO TUTORIAL NO YOUTUBE</a>
                </div>

                <div style="text-align: center; margin-top: 20px;">
                    <div style="font-size: 24px; color: #fff; font-weight: 700; margin-bottom: 15px;">Valor: R$ 25,00</div>
                    <button class="btn-action" onclick="mostrarCheckout()">🛒 COMPRAR AGORA</button>
                </div>

                <!-- Área de Pagamento Pix -->
                <div id="checkout-section" class="checkout-box">
                    <h3 style="color: #fff; margin-bottom: 10px;">💳 Área de Pagamento Seguro (Pix)</h3>
                    <p style="color: #94a3b8; margin-bottom: 15px; font-size: 14px;">Escaneie o QR Code abaixo para pagar o valor exato de R$ 25,00:</p>
                    <div class="qrcode-placeholder">
                        <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=00020126580014BR.GOV.BCB.PIX0136300108b6-bf51-4a92-bb5f-bcceb7bf1c99520400005303986540525.005802BR5925Alvaro Gabriel de Freitas6009SAO PAULO62140510Qe33xCiBEh630438DA" alt="QR Code Pix">
                    </div>
                    <p style="color: #94a3b8; margin-bottom: 10px; font-size: 14px;">Ou copie a sua chave Pix:</p>
                    <div class="order-key" id="pixKey">300108b6-bf51-4a92-bb5f-bcceb7bf1c99</div>
                    <button class="btn-copy" onclick="copyPix()">📋 Copiar Chave Pix</button>
                    <p style="font-size: 13px; color: #94a3b8; margin-top: 15px;">Após realizar o pagamento, envie o comprovante no suporte oficial.</p>
                </div>
            </div>

            <!-- DETALHES DO PRODUTO 2 (SAMP) -->
            <div id="detail-samp" class="product-detail-view">
                <h2>🎮 Painel Xit SAMP</h2>
                <div class="tutorial-container" style="text-align: center; padding: 30px;">
                    <h3 style="color: #c084fc; margin-bottom: 10px;">🚧 Projeto em Desenvolvimento 🚧</h3>
                    <p style="color: #94a3b8; font-size: 16px;">Este produto está <strong>ainda por vir...</strong> Fique atento às nossas atualizações e anúncios no servidor oficial!</p>
                </div>
            </div>
        </div>

        <!-- ABA: FEEDBACK -->
        <div id="feedback" class="tab-content">
            <h2 class="section-title">💬 Avaliações da Comunidade</h2>
            <div class="reviews-grid" id="reviews-container">
                <div class="review-card">
                    <div class="review-author">
                        <span>@marcos_dev</span>
                        <span class="stars">★★★★★</span>
                    </div>
                    <div class="review-text">"Simplesmente perfeito! O painel atualiza muito rápido e a interface é impecável. Vale cada centavo."</div>
                </div>
                <div class="review-card">
                    <div class="review-author">
                        <span>@luiz_mm</span>
                        <span class="stars">★★★★★</span>
                    </div>
                    <div class="review-text">"Ferramenta braba demais, suporte super atencioso e o sistema nunca cai. Recomendo muito!"</div>
                </div>
                <div class="review-card">
                    <div class="review-author">
                        <span>@VitorH</span>
                        <span class="stars">★★★★☆</span>
                    </div>
                    <div class="review-text">"Melhor painel que já utilizei. Muito fácil de configurar e usar no dia a dia."</div>
                </div>
            </div>

            <div class="feedback-form-box">
                <h3>⭐ Deixe o seu Feedback</h3>
                <form id="feedbackForm" onsubmit="enviarFeedback(event)">
                    <div class="form-group">
                        <label for="nomeUser">Seu Nome / Apelido:</label>
                        <input type="text" id="nomeUser" placeholder="Ex: @joao_gamer" required>
                    </div>
                    <div class="form-group">
                        <label for="estrelasUser">Quantidade de Estrelas:</label>
                        <select id="estrelasUser" required>
                            <option value="★★★★★">5 Estrelas (★★★★★)</option>
                            <option value="★★★★☆">4 Estrelas (★★★★☆)</option>
                            <option value="★★★☆☆">3 Estrelas (★★★☆☆)</option>
                            <option value="★★☆☆☆">2 Estrelas (★★☆☆☆)</option>
                            <option value="★☆☆☆☆">1 Estrela (★☆☆☆☆)</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="comentarioUser">Seu Comentário:</label>
                        <textarea id="comentarioUser" rows="4" placeholder="Escreva o que achou da ferramenta..." required></textarea>
                    </div>
                    <button type="submit" class="btn-action" style="width: 100%;">🚀 Enviar Feedback</button>
                </form>
            </div>
        </div>
    </div>

    <footer>
        CYBER_CORE SYSTEM © 2026 - Todos os direitos reservados.
    </footer>

    <script>
        function switchTab(tabId, element) {
            var contents = document.getElementsByClassName('tab-content');
            for (let c of contents) {
                c.classList.remove('active');
            }
            
            var links = document.querySelectorAll('.nav-links a');
            for (let l of links) {
                l.classList.remove('active');
            }
            
            document.getElementById(tabId).classList.add('active');
            if (element && element.classList) {
                element.classList.add('active');
            }

            var heroTitle = document.getElementById('hero-title');
            var heroDesc = document.getElementById('hero-desc');
            if (tabId === 'home') {
                heroTitle.innerHTML = "CYBER_CORE // <span>Official Hub</span>";
                heroDesc.innerHTML = "Selecione uma das opções abaixo ou navegue pelo menu superior para explorar nossos sistemas.";
            } else if (tabId === 'quem-somos') {
                heroTitle.innerHTML = "Quem Somos // <span>Cyber Core</span>";
                heroDesc.innerHTML = "Conheça a tecnologia de ponta e a equipe por trás dos sistemas mais avançados de alta performance.";
            } else if (tabId === 'produtos') {
                heroTitle.innerHTML = "Nossos Produtos // <span>Cyber Core</span>";
                heroDesc.innerHTML = "Ferramentas profissionais de alta performance com entrega imediata e suporte dedicado.";
            } else if (tabId === 'feedback') {
                heroTitle.innerHTML = "Avaliações // <span>Cyber Core</span>";
                heroDesc.innerHTML = "Veja o que nossa comunidade está dizendo e deixe sua avaliação sobre nossos sistemas.";
            }

            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function selectProduct(type) {
            document.getElementById('detail-monitoramento').style.display = 'none';
            document.getElementById('detail-samp').style.display = 'none';
            
            if (type === 'monitoramento') {
                document.getElementById('detail-monitoramento').style.display = 'block';
                document.getElementById('detail-monitoramento').scrollIntoView({ behavior: 'smooth' });
            } else if (type === 'samp') {
                document.getElementById('detail-samp').style.display = 'block';
                document.getElementById('detail-samp').scrollIntoView({ behavior: 'smooth' });
            }
        }

        function mostrarCheckout() {
            var checkoutSection = document.getElementById("checkout-section");
            checkoutSection.style.display = "block";
            checkoutSection.scrollIntoView({ behavior: 'smooth' });
        }

        function copyPix() {
            var text = document.getElementById("pixKey").innerText;
            navigator.clipboard.writeText(text);
            alert("Chave Pix copiada com sucesso!");
        }

        function enviarFeedback(event) {
            event.preventDefault();
            
            var nome = document.getElementById('nomeUser').value;
            var estrelas = document.getElementById('estrelasUser').value;
            var comentario = document.getElementById('comentarioUser').value;
            
            var container = document.getElementById('reviews-container');
            
            var card = document.createElement('div');
            card.className = 'review-card';
            card.innerHTML = `
                <div class="review-author">
                    <span>${nome}</span>
                    <span class="stars">${estrelas}</span>
                </div>
                <div class="review-text">"${comentario}"</div>
            `;
            
            container.insertBefore(card, container.firstChild);
            
            document.getElementById('feedbackForm').reset();
            alert("Feedback enviado com sucesso! Obrigado pela sua avaliação.");
            
            container.scrollIntoView({ behavior: 'smooth' });
        }
    </script>
</body>
</html>
