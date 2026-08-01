from flask import Flask, render_template_string

app = Flask(__name__)

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
        
        /* Grid de Produtos */
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
        .order-key { background: #0b0713; border: 1px dashed #9333ea; padding: 12px; font-family: monospace; font-size: 14px; color: #fff; margin-bottom: 20px; border-radius: 6px; word-break: break-all; }
        .qrcode-placeholder { background: #fff; width: 180px; height: 180px; margin: 0 auto 20px auto; border-radius: 8px; display: flex; align-items: center; justify-content: center; padding: 10px; }
        .qrcode-placeholder img { width: 100%; height: 100%; }
        .btn-copy { background: #3b82f6; color: white; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-weight: 600; margin-top: 10px; }
        .btn-copy:hover { background: #2563eb; }

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
        <h2 id="produtos" class="section-title">Nossos Produtos</h2>
        <div class="products-grid">
            <div class="product-card">
                <div>
                    <h3>Painel de Monitoramento v1.0</h3>
                    <p>Acesso completo ao sistema de rastreamento em tempo real com interface camuflada, radar e atualizações vitalícias.</p>
                </div>
                <div>
                    <div class="product-price">R$ 25,00</div>
                    <a href="#checkout" class="btn-buy">COMPRAR AGORA</a>
                </div>
            </div>
        </div>

        <div id="checkout" class="checkout-box">
            <h2>Área de Pagamento Seguro (Pix)</h2>
            <p style="color: #94a3b8; margin-bottom: 15px; font-size: 14px;">Escaneie o QR Code abaixo para pagar o valor exato:</p>
            <div class="qrcode-placeholder">
                <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=00020126580014BR.GOV.BCB.PIX0136300108b6-bf51-4a92-bb5f-bcceb7bf1c99520400005303986540525.005802BR5925Alvaro Gabriel de Freitas6009SAO PAULO62140510Qe33xCiBEh630438DA" alt="QR Code Pix">
            </div>
            <p style="color: #94a3b8; margin-bottom: 10px; font-size: 14px;">Ou copie o código Pix Copia e Cola:</p>
            <div class="order-key" id="pixKey">00020126580014BR.GOV.BCB.PIX0136300108b6-bf51-4a92-bb5f-bcceb7bf1c99520400005303986540525.005802BR5925Alvaro Gabriel de Freitas6009SAO PAULO62140510Qe33xCiBEh630438DA</div>
            <button class="btn-copy" onclick="copyPix()">Copiar Código Pix</button>
            <p style="font-size: 13px; color: #94a3b8; margin-top: 15px;">Após realizar o pagamento, envie o comprovante no suporte.</p>
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
            <p style="color: #94a3b8; margin-bottom: 20px; font-size: 14px;">Preparamos um guia passo a passo em vídeo para você começar a operar em menos de 5 minutos.</p>
            <a href="https://www.youtube.com/watch?v=_Nlb0CzPxF8" target="_blank" class="btn-tutorial">ACESSAR TUTORIAL COMPLETO</a>
        </div>
    </div>

    <footer>
        CYBER_CORE SYSTEM © 2026 - Todos os direitos reservados.
    </footer>

    <script>
        function copyPix() {
            var text = document.getElementById("pixKey").innerText;
            navigator.clipboard.writeText(text);
            alert("Código Pix copiado com sucesso!");
        }
    </script>
</body>
</html>
"""

@app.route('/')
def store():
    return render_template_string(STORE_HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
