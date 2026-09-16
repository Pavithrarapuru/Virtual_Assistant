from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>NIVI | AI Voice Agent</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            background:
                radial-gradient(circle at 50% 20%, rgba(89, 66, 180, 0.18), transparent 35%),
                radial-gradient(circle at 10% 90%, rgba(0, 210, 255, 0.08), transparent 30%),
                #070910;

            color: #f5f7ff;
            font-family: Inter, -apple-system, BlinkMacSystemFont,
                         "Segoe UI", sans-serif;

            overflow-x: hidden;
        }

        /* ---------- BACKGROUND ---------- */

        .grid {
            position: fixed;
            inset: 0;

            background-image:
                linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);

            background-size: 45px 45px;

            mask-image: linear-gradient(
                to bottom,
                black,
                transparent 90%
            );

            pointer-events: none;
        }

        /* ---------- NAVBAR ---------- */

        nav {
            height: 75px;

            display: flex;
            align-items: center;
            justify-content: space-between;

            padding: 0 7%;

            border-bottom: 1px solid rgba(255,255,255,0.07);

            backdrop-filter: blur(15px);
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .brand-icon {
            width: 38px;
            height: 38px;

            border-radius: 12px;

            display: flex;
            align-items: center;
            justify-content: center;

            background: linear-gradient(
                135deg,
                #8b5cf6,
                #06b6d4
            );

            font-weight: 800;
        }

        .brand-name {
            font-size: 21px;
            font-weight: 700;
            letter-spacing: 1px;
        }

        .status {
            display: flex;
            align-items: center;
            gap: 8px;

            font-size: 13px;
            color: #a9b0c3;
        }

        .status-dot {
            width: 8px;
            height: 8px;

            border-radius: 50%;

            background: #39e58c;

            box-shadow: 0 0 12px #39e58c;
        }

        /* ---------- HERO ---------- */

        .hero {
            min-height: calc(100vh - 75px);

            display: flex;
            flex-direction: column;
            align-items: center;

            text-align: center;

            padding: 70px 20px 50px;

            position: relative;
        }

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 8px;

            padding: 8px 14px;

            border: 1px solid rgba(139,92,246,0.35);

            border-radius: 999px;

            color: #bca9ff;

            background: rgba(139,92,246,0.08);

            font-size: 12px;

            letter-spacing: 1.5px;

            text-transform: uppercase;
        }

        h1 {
            margin-top: 25px;

            font-size: clamp(42px, 7vw, 82px);

            line-height: 1;

            letter-spacing: -4px;
        }

        .gradient-text {
            background: linear-gradient(
                90deg,
                #ffffff,
                #b9a5ff,
                #67e8f9
            );

            -webkit-background-clip: text;
            color: transparent;
        }

        .subtitle {
            max-width: 700px;

            margin-top: 22px;

            color: #9da5bb;

            font-size: 17px;

            line-height: 1.7;
        }

        /* ---------- AI ORB ---------- */

        .orb-container {
            position: relative;

            width: 250px;
            height: 250px;

            margin: 55px auto 30px;

            display: flex;
            align-items: center;
            justify-content: center;
        }

        .orb-ring {
            position: absolute;

            border-radius: 50%;

            border: 1px solid rgba(139,92,246,0.35);

            animation: rotate 8s linear infinite;
        }

        .ring-one {
            width: 245px;
            height: 245px;
        }

        .ring-two {
            width: 210px;
            height: 210px;

            border-color: rgba(34,211,238,0.35);

            animation-direction: reverse;

            animation-duration: 6s;
        }

        .orb {
            width: 145px;
            height: 145px;

            border-radius: 50%;

            background:
                radial-gradient(
                    circle at 35% 30%,
                    #ffffff,
                    #b99aff 10%,
                    #714cff 35%,
                    #16102f 70%
                );

            box-shadow:
                0 0 35px rgba(139,92,246,0.7),
                0 0 100px rgba(99,102,241,0.35),
                inset 0 0 30px rgba(255,255,255,0.25);

            animation: breathe 3s ease-in-out infinite;
        }

        @keyframes breathe {
            0%,100% {
                transform: scale(1);
            }

            50% {
                transform: scale(1.08);
            }
        }

        @keyframes rotate {
            from {
                transform: rotate(0deg);
            }

            to {
                transform: rotate(360deg);
            }
        }

        /* ---------- VOICE BUTTON ---------- */

        .voice-button {
            border: none;

            width: 70px;
            height: 70px;

            border-radius: 50%;

            background: linear-gradient(
                135deg,
                #8b5cf6,
                #6366f1
            );

            color: white;

            font-size: 25px;

            cursor: pointer;

            box-shadow: 0 15px 40px rgba(99,102,241,0.3);

            transition: 0.25s;
        }

        .voice-button:hover {
            transform: translateY(-4px) scale(1.05);

            box-shadow:
                0 20px 50px rgba(99,102,241,0.45);
        }

        .voice-label {
            margin-top: 13px;

            color: #8991a8;

            font-size: 13px;
        }

        /* ---------- CAPABILITIES ---------- */

        .capabilities {
            width: min(950px, 100%);

            display: grid;

            grid-template-columns:
                repeat(4, 1fr);

            gap: 14px;

            margin-top: 65px;
        }

        .card {
            padding: 22px;

            text-align: left;

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.055),
                    rgba(255,255,255,0.018)
                );

            border: 1px solid rgba(255,255,255,0.08);

            border-radius: 18px;

            backdrop-filter: blur(20px);

            transition: 0.25s;
        }

        .card:hover {
            transform: translateY(-5px);

            border-color:
                rgba(139,92,246,0.45);

            background:
                rgba(139,92,246,0.08);
        }

        .card-icon {
            font-size: 23px;

            margin-bottom: 15px;
        }

        .card h3 {
            font-size: 14px;

            margin-bottom: 8px;
        }

        .card p {
            color: #858da4;

            font-size: 12px;

            line-height: 1.6;
        }

        /* ---------- AGENT PIPELINE ---------- */

        .architecture {
            width: min(950px, 100%);

            margin-top: 45px;

            padding: 22px;

            border-radius: 18px;

            border: 1px solid rgba(255,255,255,0.07);

            background: rgba(255,255,255,0.025);

            color: #858da4;

            font-size: 12px;

            letter-spacing: 0.5px;
        }

        .architecture span {
            color: #c4b5fd;
        }

        /* ---------- FOOTER ---------- */

        footer {
            margin-top: 55px;

            color: #626a80;

            font-size: 11px;

            letter-spacing: 1px;
        }

        /* ---------- RESPONSIVE ---------- */

        @media(max-width: 750px) {

            h1 {
                letter-spacing: -2px;
            }

            .capabilities {
                grid-template-columns:
                    repeat(2, 1fr);
            }

            .orb-container {
                margin-top: 40px;
            }
        }

        @media(max-width: 450px) {

            .capabilities {
                grid-template-columns: 1fr;
            }

            nav {
                padding: 0 5%;
            }

            .subtitle {
                font-size: 15px;
            }
        }

    </style>
</head>

<body>

<div class="grid"></div>

<nav>

    <div class="brand">

        <div class="brand-icon">
            N
        </div>

        <div class="brand-name">
            NIVI
        </div>

    </div>

    <div class="status">

        <div class="status-dot"></div>

        AI AGENT ONLINE

    </div>

</nav>


<section class="hero">

    <div class="eyebrow">
        ◉ Autonomous Voice Intelligence
    </div>


    <h1>

        Meet <span class="gradient-text">NIVI</span>

    </h1>


    <p class="subtitle">

        A voice-first AI agent designed to understand natural language,
        reason with LLMs, interact with tools, and assist users through
        intelligent conversations.

    </p>


    <div class="orb-container">

        <div class="orb-ring ring-one"></div>

        <div class="orb-ring ring-two"></div>

        <div class="orb"></div>

    </div>


    <button
        class="voice-button"
        onclick="startListening()"
        title="Talk to NIVI"
    >

        🎙

    </button>


    <div class="voice-label" id="voiceStatus">

        Tap to talk with NIVI

    </div>


    <div class="capabilities">

        <div class="card">

            <div class="card-icon">🧠</div>

            <h3>LLM Reasoning</h3>

            <p>
                Understands context and generates
                intelligent responses using large
                language models.
            </p>

        </div>


        <div class="card">

            <div class="card-icon">🎙</div>

            <h3>Voice Interaction</h3>

            <p>
                Designed for natural voice-based
                interaction instead of traditional
                text-only interfaces.
            </p>

        </div>


        <div class="card">

            <div class="card-icon">⚡</div>

            <h3>AI Agent</h3>

            <p>
                Connects reasoning with tools and
                actions to perform useful tasks.
            </p>

        </div>


        <div class="card">

            <div class="card-icon">🔗</div>

            <h3>Tool Integration</h3>

            <p>
                Built to connect external services,
                automation workflows and APIs.
            </p>

        </div>

    </div>


    <div class="architecture">

        <span>VOICE</span>
        &nbsp;→&nbsp;
        <span>UNDERSTANDING</span>
        &nbsp;→&nbsp;
        <span>LLM</span>
        &nbsp;→&nbsp;
        <span>AGENT</span>
        &nbsp;→&nbsp;
        <span>TOOLS</span>
        &nbsp;→&nbsp;
        <span>RESPONSE</span>

    </div>


    <footer>

        NIVI • AI Voice Agent • FastAPI Backend

    </footer>

</section>


<script>

function startListening() {

    const status =
        document.getElementById("voiceStatus");

    status.innerText =
        "Listening... speak to NIVI";

    setTimeout(() => {

        status.innerText =
            "Voice interface ready";

    }, 3000);

}

</script>

</body>
</html>
"""


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "NIVI AI Voice Agent"
    }
