from flask import Flask, render_template_string

app = Flask(__name__)

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
        .nav-links { display: flex; gap: 25px; align-items: center; }
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

        .products-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px; margin-bottom: 30px; }
        .product-card { background: #130b22; border: 1px solid #2b174a; padding: 25px; border-radius: 10px; display: flex; flex-direction: column; justify-content: space-between; transition: 0.3s; cursor: pointer; }
        .product-card:hover { border-color: #9333ea; box-shadow: 0 0 20px rgba(147,51,234,0.15); }
        .product-card h3 { color: #c084fc; margin-bottom: 10px; font-size: 20px; }
        .product-card p { color: #94a3b8; font-size: 14px; margin-bottom: 20px; }
        .product-price { font-size: 22px; color: #fff; font-weight: 700; margin-bottom: 20px; }

        .product-detail-view { background: #130b22; border: 1px solid #2b174a; border-radius: 12px; padding: 35px; margin-top: 30px; display: none; }
        .product-detail-view h2 { color: #fff; margin-bottom: 15px; font-size: 24px; color: #c084fc; }
        
        .btn-action { background: #9333ea; color: #fff; padding: 12px 25px; font-size: 14px; font-weight: 600; border-radius: 6px; text-decoration: none; text-align: center; box-shadow: 0 0 15px rgba(147,51,234,0.4); transition: 0.3s; display: inline-block; border: none; cursor: pointer; }
        .btn-action:hover { background: #a855f7; box-shadow: 0 0 25px rgba(168,85,247,0.7); }

        .checkout-box { background: #0b0713; border: 2px solid #9333ea; border-radius: 12px; padding: 25px; text-align: center; margin-top: 25px; display: none; box-shadow: 0 0 25px rgba(147,51,234,0.2); }
        .order-key { background: #130b22; border: 1px dashed #9333ea; padding: 12px; font-family: monospace; font-size: 13px; color: #fff; margin-bottom: 15px; border-radius: 6px; word-break: break-all; }
        .qrcode-placeholder { background: #fff; width: 180px; height: 180px; margin: 0 auto 15px auto; border-radius: 8px; display: flex; align-items: center; justify-content: center; padding: 10px; }
        .qrcode-placeholder img { width: 100%; height: 100%; }
        .btn-copy { background: #3b82f6; color: white; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-weight: 600; margin-bottom: 15px; display: inline-flex; align-items: center; gap: 6px; }
        .btn-copy:hover { background: #2563eb; }

        /* Botão discreto para o cliente avisar que já pagou */
        .btn-ja-pagou { background: none; border: none; color: #94a3b8; font-size: 13px; text-decoration: underline; cursor: pointer; margin-top: 20px; display: block; width: 100%; transition: 0.3s; }
        .btn-ja-pagou:hover { color: #c084fc; }

        /* Tela de sucesso que aparece ao clicar */
        .success-box { display: none; background: rgba(34, 197, 94, 0.1); border: 2px solid #22c55e; border-radius: 12px; padding: 25px; text-align: center; margin-top: 25px; box-shadow: 0 0 30px rgba(34, 197, 94, 0.25); animation: fadeIn 0.5s ease-in-out; }
        .success-box h3 { color: #22c55e; font-size: 22px; margin-bottom: 10px; display: flex; align-items: center; justify-content: center; gap: 10px; }
        .success-box p { color: #cbd5e1; font-size: 14px; margin-bottom: 20px; }
        
        .social-buttons { display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; margin-top: 15px; }
        .btn-whatsapp { background: #22c55e; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: 600; display: inline-flex; align-items: center; gap: 8px; text-decoration: none; box-shadow: 0 0 15px rgba(34,197,94,0.4); }
        .btn-whatsapp:hover { background: #16a34a; }
        .btn-discord { background: #5865F2; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: 600; display: inline-flex; align-items: center; gap: 8px; text-decoration: none; box-shadow: 0 0 15px rgba(88,101,242,0.4); }
        .btn-discord:hover { background: #4752C4; }

        footer { text-align: center; padding: 25px; color: #64748b; font-size: 13px; border-top: 1px solid #2b174a; background: #130b22; margin-top: 50px; }

        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
    <header>
        <div class="logo" onclick="switchTab('home', this)">🏠 <span>Página Principal</span></div>
        <div class="nav-links">
            <a onclick="switchTab('home', this)" id="link-home" class="active">🏠 Início</a>
            <a onclick="switchTab('produtos', this)" id="link-produtos">📦 Produtos</a>
        </div>
    </header>

    <div class="hero">
        <h1>CYBER_CORE // <span>Official Hub</span></h1>
        <p>Selecione seu produto e realize o pagamento via Pix.</p>
    </div>

    <div class="container">
        <div id="home" class="tab-content active">
            <h2 class="section-title">⚡ Painel de Navegação Oficial</h2>
            <div class="products-grid">
                <div class="product-card" onclick="switchTab('produtos', document.getElementById('link-produtos'))">
                    <div>
                        <h3>📦 Ir para Loja</h3>
                        <p>Acesse o painel de monitoramento.</p>
                    </div>
                    <button class="btn-action" style="width:100%;">Acessar Loja →</button>
                </div>
            </div>
        </div>

        <div id="produtos" class="tab-content">
            <h2 class="section-title">📦 Escolha sua Ferramenta</h2>
            <div class="products-grid">
                <div class="product-card" onclick="mostrarCheckout()">
                    <div>
                        <h3>⚡ Painel de Monitoramento v1.0</h3>
                        <p>Acesso completo ao sistema de rastreamento em tempo real.</p>
                    </div>
                    <div>
                        <div class="product-price">R$ 25,00</div>
                        <span class="btn-action" style="display:block; text-align:center; padding: 8px;">COMPRAR AGORA</span>
                    </div>
                </div>
            </div>

            <div id="checkout-section" class="checkout-box">
                <h3 style="color: #fff; margin-bottom: 10px;">💳 Pagamento via Pix</h3>
                <p style="color: #94a3b8; font-size: 13px; margin-bottom: 15px;">Escaneie o QR Code ou copie a chave abaixo:</p>
                
                <div class="qrcode-placeholder">
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=00020126580014BR.GOV.BCB.PIX0136300108b6-bf51-4a92-bb5f-bcceb7bf1c99520400005303986540525.005802BR5925Alvaro Gabriel de Freitas6009SAO PAULO62140510Qe33xCiBEh630438DA" alt="QR Code Pix">
                </div>
                
                <div class="order-key" id="pixKey">300108b6-bf51-4a92-bb5f-bcceb7bf1c99</div>
                <button class="btn-copy" onclick="copyPix()">📋 Copiar Chave Pix</button>

                <!-- Botão discreto embaixo para o usuário clicar quando pagar -->
                <button class="btn-ja-pagou" onclick="liberarTelaSucesso()">Já pagou? Clique aqui para ver as opções</button>

                <!-- Tela verde que aparece instantaneamente ao clicar -->
                <div id="success-box" class="success-box">
                    <h3>✅ Pagamento Confirmado!</h3>
                    <p>Agora escolha onde deseja receber ou enviar o comprovante com a nossa equipe:</p>
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
    </div>

    <footer>CYBER_CORE SYSTEM © 2026</footer>

    <script>
        function switchTab(tabId, element) {
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            document.querySelectorAll('.nav-links a').forEach(l => l.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            if(element) element.classList.add('active');
            window.scrollTo({ top: 0, behavior: 'smooth' });
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
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
