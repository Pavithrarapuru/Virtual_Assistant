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

    <title>NIVI — Virtual Assistant</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            font-family: Inter, Arial, sans-serif;
            background: #08090d;
            color: #ffffff;
            overflow: hidden;
        }


        /* Background */

        .background {
            position: fixed;
            inset: 0;

            background:
                radial-gradient(
                    circle at 50% 42%,
                    rgba(111, 78, 255, 0.18),
                    transparent 28%
                );

            pointer-events: none;
        }


        /* Navigation */

        nav {
            height: 72px;

            display: flex;
            align-items: center;
            justify-content: space-between;

            padding: 0 6%;

            border-bottom: 1px solid rgba(255,255,255,0.06);
        }


        .logo {
            display: flex;
            align-items: center;
            gap: 10px;

            font-size: 20px;
            font-weight: 700;
            letter-spacing: 1px;
        }


        .logo-mark {
            width: 34px;
            height: 34px;

            border-radius: 10px;

            display: flex;
            align-items: center;
            justify-content: center;

            background: linear-gradient(
                135deg,
                #7657ff,
                #4e8cff
            );

            font-weight: 800;
        }


        .online {
            display: flex;
            align-items: center;
            gap: 8px;

            color: #8d94a8;

            font-size: 12px;
        }


        .dot {
            width: 7px;
            height: 7px;

            border-radius: 50%;

            background: #42e695;

            box-shadow: 0 0 10px #42e695;
        }


        /* Main */

        main {
            height: calc(100vh - 72px);

            display: flex;
            flex-direction: column;
            align-items: center;

            text-align: center;

            padding-top: 70px;
        }


        .welcome {
            font-size: 13px;

            color: #858ca0;

            letter-spacing: 2px;

            text-transform: uppercase;
        }


        h1 {
            margin-top: 15px;

            font-size: clamp(42px, 6vw, 72px);

            letter-spacing: -3px;

            font-weight: 700;
        }


        .description {
            margin-top: 16px;

            max-width: 520px;

            color: #858ca0;

            line-height: 1.7;

            font-size: 15px;
        }


        /* AI Core */

        .core-wrapper {
            position: relative;

            width: 250px;
            height: 250px;

            margin-top: 42px;

            display: flex;
            align-items: center;
            justify-content: center;
        }


        .circle {
            position: absolute;

            border-radius: 50%;

            border: 1px solid rgba(
                125,
                91,
                255,
                0.25
            );
        }


        .circle.one {
            width: 250px;
            height: 250px;

            animation: rotate 12s linear infinite;
        }


        .circle.two {
            width: 205px;
            height: 205px;

            border-color: rgba(
                75,
                140,
                255,
                0.25
            );

            animation: rotateReverse 9s linear infinite;
        }


        .core {
            width: 125px;
            height: 125px;

            border-radius: 50%;

            background:
                radial-gradient(
                    circle at 35% 30%,
                    #ffffff,
                    #a995ff 12%,
                    #7055ff 38%,
                    #18122e 72%
                );

            box-shadow:
                0 0 35px rgba(112,85,255,0.55),
                0 0 90px rgba(112,85,255,0.2);

            animation: pulse 3s ease-in-out infinite;
        }


        @keyframes pulse {

            0%,100% {
                transform: scale(1);
            }

            50% {
                transform: scale(1.07);
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


        @keyframes rotateReverse {

            from {
                transform: rotate(360deg);
            }

            to {
                transform: rotate(0deg);
            }

        }


        /* Microphone */

        .mic {
            position: absolute;

            bottom: -5px;

            width: 62px;
            height: 62px;

            border-radius: 50%;

            border: 1px solid rgba(
                255,
                255,
                255,
                0.12
            );

            background: rgba(
                255,
                255,
                255,
                0.06
            );

            color: white;

            font-size: 23px;

            cursor: pointer;

            backdrop-filter: blur(15px);

            transition: 0.25s;
        }


        .mic:hover {

            transform: scale(1.08);

            background: rgba(
                118,
                87,
                255,
                0.2
            );

            border-color: rgba(
                118,
                87,
                255,
                0.5
            );

        }


        .instruction {

            margin-top: 25px;

            color: #70778b;

            font-size: 12px;

            letter-spacing: 0.4px;
        }


        /* Features */

        .features {

            display: flex;

            gap: 10px;

            margin-top: 32px;
        }


        .feature {

            padding: 9px 15px;

            border-radius: 20px;

            border: 1px solid rgba(
                255,
                255,
                255,
                0.07
            );

            background: rgba(
                255,
                255,
                255,
                0.025
            );

            color: #858ca0;

            font-size: 11px;
        }


        /* Footer */

        footer {

            position: fixed;

            bottom: 22px;

            left: 0;
            right: 0;

            text-align: center;

            color: #454b5c;

            font-size: 10px;

            letter-spacing: 1px;
        }


        /* Mobile */

        @media(max-width: 600px) {

            main {
                padding: 55px 20px 0;
            }

            h1 {
                font-size: 46px;
            }

            .description {
                font-size: 14px;
            }

            .features {
                flex-wrap: wrap;
                justify-content: center;
            }

        }

    </style>

</head>


<body>


<div class="background"></div>


<nav>

    <div class="logo">

        <div class="logo-mark">
            N
        </div>

        NIVI

    </div>


    <div class="online">

        <span class="dot"></span>

        Online

    </div>

</nav>



<main>


    <div class="welcome">
        Your Personal Assistant
    </div>


    <h1>
        Hello, I'm NIVI.
    </h1>


    <p class="description">

        A voice-based virtual assistant designed to
        understand your requests, answer questions,
        and help you get things done.

    </p>



    <div class="core-wrapper">

        <div class="circle one"></div>

        <div class="circle two"></div>

        <div class="core"></div>


        <button
            class="mic"
            onclick="listen()"
            aria-label="Talk to NIVI"
        >

            🎙

        </button>

    </div>


    <div
        class="instruction"
        id="status"
    >

        Tap the microphone to talk

    </div>



    <div class="features">

        <div class="feature">
            Voice Interaction
        </div>

        <div class="feature">
            Smart Responses
        </div>

        <div class="feature">
            Task Assistance
        </div>

    </div>


</main>



<footer>

    NIVI • Virtual Assistant

</footer>



<script>

function listen() {

    const status =
        document.getElementById("status");

    status.innerText =
        "Listening...";

    setTimeout(function() {

        status.innerText =
            "I'm ready to help.";

    }, 2500);

}

</script>


</body>

</html>
"""


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "NIVI"
    }
