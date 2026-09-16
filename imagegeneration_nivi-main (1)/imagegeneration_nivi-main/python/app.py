from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>NIVI AI Assistant</title>
            <style>
                body {
                    background: #0b1020;
                    color: white;
                    text-align: center;
                    font-family: Arial;
                }

                h1 {
                    margin-top: 100px;
                }

                .orb {
                    width: 150px;
                    height: 150px;
                    border-radius: 50%;
                    margin: 50px auto;
                    background: radial-gradient(circle, #7c3aed, #111827);
                    box-shadow: 0 0 50px #7c3aed;
                }
            </style>
        </head>

        <body>
            <h1>Welcome to NIVI</h1>
            <p>AI Voice Assistant</p>

            <div class="orb"></div>

            <button>🎙️ Talk to NIVI</button>
        </body>
    </html>
    """
