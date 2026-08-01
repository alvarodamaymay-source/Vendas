from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel IP - Loja Oficial</title>
    <style>
        body {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 500px;
            margin: 0 auto;
            background: #161b22;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }
        h1 {
            color: #58a6ff;
            font-size: 24px;
        }
        .price {
            font-size: 28px;
            color: #2ea043;
            margin: 15px 0;
            font-weight: bold;
        }
        .description {
            font-size: 16px;
            margin-bottom: 20px;
            color: #8b949e;
        }
        .btn-tutorial {
            display: inline-block;
            background-color: #238636;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .btn-tutorial:hover {
            background-color: #2ea043;
        }
        .pix-box {
            background: #21262d;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
            word-break: break-all;
        }
        input {
            width: 100%;
            padding: 10px;
            background: #0d1117;
            border: 1px solid #30363d;
            color: white;
            border-radius: 5px;
            text-align: center;
            margin-top: 10px;
            font-size: 14px;
        }
        button {
            background-color: #1f6feb;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
            font-weight: bold;
        }
        button:hover {
            background-color: #388bfd;
        }
        .qr-code {
            max-width: 200px;
            margin: 15px auto;
            border-radius: 8px;
            display: block;
            background: white;
            padding: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Painel IP Advanced</h1>
        <p class="description">Acesso completo ao painel de rastreamento e puxada de IP.</p>
        
        <div class="price">R$ 25,00</div>

        <!-- Link do tutorial do YouTube -->
        <a href="https://www.youtube.com/watch?v=_Nlb0CzPxF8" target="_blank" class="btn-tutorial">📺 Ver Tutorial em Vídeo</a>

        <hr style="border: 0; border-top: 1px solid #30363d; margin: 20px 0;">

        <h3>💳 Pagamento via PIX</h3>
        <p>Escaneie o QR Code para pagar direto no valor exato ou copie a chave:</p>

        <!-- QR Code gerado automaticamente com o payload Pix embutido -->
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=00020126580014br.gov.bcb.pix0136300108b6-bf51-4a92-bb5f-bcceb7bf1c99520400005303986540525.005802BR5925DAYANE G6009SAO PAULO62070503***63041D3D" alt="QR Code Pix" class="qr-code">

        <div class="pix-box">
            <strong>Chave Pix Aleatória:</strong>
            <input type="text" id="pixKey" value="300108b6-bf51-4a92-bb5f-bcceb7bf1c99" readonly>
            <button onclick="copyPix()">Copiar Chave Pix</button>
        </div>
    </div>

    <script>
        function copyPix() {
            var copyText = document.getElementById("pixKey");
            copyText.select();
            copyText.setSelectionRange(0, 99999);
            navigator.clipboard.writeText(copyText.value);
            alert("Chave Pix copiada com sucesso!");
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
