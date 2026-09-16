import { useEffect, useRef, useState } from "react";
import { Mic, MicOff, Sparkles, Volume2 } from "lucide-react";
import "./App.css";

function App() {
  const [isListening, setIsListening] = useState(false);
  const [status, setStatus] = useState("Ready");
  const [userMessage, setUserMessage] = useState("");
  const [niviMessage, setNiviMessage] = useState(
    "Hi, I'm NIVI. How can I help you?"
  );

  const recognitionRef = useRef(null);

  useEffect(() => {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
      setStatus("Speech recognition is not supported");
      return;
    }

    const recognition = new SpeechRecognition();

    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onstart = () => {
      setIsListening(true);
      setStatus("Listening...");
    };

    recognition.onresult = (event) => {
      const text = event.results[0][0].transcript;

      setUserMessage(text);
      setIsListening(false);
      setStatus("Thinking...");

      processCommand(text);
    };

    recognition.onerror = (event) => {
      console.log("Speech recognition error:", event.error);

      setIsListening(false);
      setStatus("Ready");
    };

    recognition.onend = () => {
      setIsListening(false);

      if (status === "Listening...") {
        setStatus("Ready");
      }
    };

    recognitionRef.current = recognition;

    return () => {
      recognition.stop();
    };
  }, []);

  const speak = (text) => {
    if (!window.speechSynthesis) {
      return;
    }

    window.speechSynthesis.cancel();

    const speech = new SpeechSynthesisUtterance(text);

    speech.lang = "en-US";
    speech.rate = 1;
    speech.pitch = 1;

    speech.onstart = () => {
      setStatus("Speaking...");
    };

    speech.onend = () => {
      setStatus("Ready");
    };

    window.speechSynthesis.speak(speech);
  };

  const processCommand = async (text) => {
  setStatus("Thinking...");

  try {
    const response = await fetch("http://127.0.0.1:8000/test");

    if (!response.ok) {
      throw new Error("Backend error");
    }

    const data = await response.json();

    const answer = `${data.message}. You said: ${text}`;

    setNiviMessage(answer);

    speak(answer);
  } catch (error) {
    console.error("Backend connection error:", error);

    const answer =
      "I couldn't connect to my Python backend.";

    setNiviMessage(answer);

    speak(answer);
  }
};

  const startListening = () => {
    if (!recognitionRef.current) {
      setStatus("Microphone is not available");
      return;
    }

    setUserMessage("");
    setStatus("Starting...");

    try {
      recognitionRef.current.start();
    } catch (error) {
      console.log("Microphone error:", error);
    }
  };

  return (
    <div className="app">

      {/* Header */}

      <header className="header">

        <div className="logo-section">

          <div className="logo-icon">
            <Sparkles size={20} />
          </div>

          <div>
            <h1>NIVI</h1>
            <p>AI Virtual Assistant</p>
          </div>

        </div>

        <div className="online-status">
          <span></span>
          Online
        </div>

      </header>


      {/* Main */}

      <main className="main">

        <div className="assistant">

          <p className="subtitle">
            YOUR PERSONAL AI ASSISTANT
          </p>

          <h2>
            Hello, I'm <span>NIVI</span>
          </h2>

          <p className="description">
            Talk naturally. I'll listen, understand and help you.
          </p>


          {/* Microphone */}

          <div
            className={`microphone-container ${
              isListening ? "listening" : ""
            }`}
          >

            <div className="pulse pulse-1"></div>
            <div className="pulse pulse-2"></div>

            <button
              className="microphone"
              onClick={startListening}
            >

              {isListening ? (
                <MicOff size={38} />
              ) : (
                <Mic size={38} />
              )}

            </button>

          </div>


          {/* Status */}

          <div className="status">

            <span
              className={`status-dot ${
                isListening ? "active" : ""
              }`}
            ></span>

            {status}

          </div>

          <p className="mic-help">
            {isListening
              ? "I'm listening... speak now"
              : "Click the microphone to speak"}
          </p>


          {/* Conversation */}

          <div className="conversation">

            <div className="message">

              <div className="message-title">
                YOU
              </div>

              <p>
                {userMessage ||
                  "Your voice command will appear here..."}
              </p>

            </div>


            <div className="message nivi-response">

              <div className="message-title">

                <Volume2 size={15} />

                NIVI

              </div>

              <p>{niviMessage}</p>

            </div>

          </div>

        </div>

      </main>


      {/* Footer */}

      <footer>

        <span>Powered by NIVI AI</span>

        <span>
          Voice • AI • Automation
        </span>

      </footer>

    </div>
  );
}

export default App;