# NIVI - A Virtual Assistant with AI

## Introduction

Welcome to the NIVI repository! NIVI is an advanced virtual assistant powered by Artificial Intelligence (AI) that enables users to interact with their devices using only voice commands. Our aim is to provide a seamless, hands-free user experience, eliminating the need for keyboards or touch inputs.

## Overview 

NIVI leverages cutting-edge AI technologies, including natural language processing (NLP) and machine learning algorithms, to offer personalized assistance, task automation, and intuitive interaction. This repository contains the source code, documentation, and resources for the NIVI virtual assistant.

## Features 

- **Voice Interaction**: Interact with the assistant using voice commands for hands-free operation and accessibility across devices.
- **Integration**: Seamlessly integrates with various applications and services, including project management tools and chatbots.
- **Timestamp**: Provides the current time on request.
- **Internet Surfing**: Access information, websites, and online content through voice commands.
- **Accessing Applications**: Launch and interact with applications via voice commands.
- **Browser Navigation**: Navigate the web intuitively using voice commands.
- **Media Playback**: Stream music, videos, and podcasts with natural language commands.
- **Email Creation**: Compose and send emails using voice commands.
- **Code Automation**: Automate writing, testing, and deploying software code.
- **News Updates**: Receive personalized news updates tailored to your interests.

## Future Developments

- **Object Detection**: Integrate object detection to identify and locate objects within images or video streams.
- **Language Translation**: Implement language translation for global communication and collaboration.
- **Weather Detection**: Add advanced weather detection for accurate atmospheric tracking and forecasts.

## 🚀 Recent Updates

### Web-Based NIVI Interface

NIVI has been updated with a modern web-based interface to provide a more interactive and user-friendly experience.

#### Frontend
- Built a responsive UI using React and Vite.
- Added a dedicated NIVI assistant screen.
- Added an animated microphone interaction for voice input.
- Added status indicators to show when NIVI is ready and listening.
- Added a conversational area to display user input and NIVI responses.
- Designed the interface with a modern dark AI-assistant theme.

#### Backend
- Added a FastAPI backend to provide API endpoints for the NIVI web application.
- Added a health-check endpoint to verify that the backend is running.
- Added a test endpoint to verify frontend-backend connectivity.
- Prepared the backend structure for integrating NIVI's existing Python functionalities.

#### Voice Interaction
- Integrated browser microphone access for voice input.
- Added speech recognition handling on the frontend.
- Added microphone animation states for a more interactive experience.
- Tested microphone access and SpeechRecognition integration with the existing Python assistant.

#### Existing NIVI Functionality
The existing Python-based NIVI assistant has been preserved, including:
- Voice commands
- Application launching
- Application/window closing
- Tab switching
- YouTube music playback
- Time queries
- Email functionality
- AI-powered conversational responses
- Browser automation using Selenium
- Text-to-speech using Edge TTS
- Speech recognition
- PyAutoGUI automation

### 📁 Updated Project Structure

```text
Virtual_Assistant/
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── public/
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── python/
│   ├── api.py
│   ├── nivi.py
│   ├── test.py
│   ├── gpt4.py
│   ├── emailnivi.py
│   ├── mailbot.py
│   ├── news.py
│   │
│   ├── head/
│   │   ├── listen.py
│   │   ├── speak.py
│   │   └── ucookie.py
│   │
│   └── test/
│       ├── gpt.py
│       ├── emailbot.py
│       ├── bingimage.py
│       └── ...
│
├── .gitignore
└── README.md

## Getting Started

To get started with NIVI, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Pavithrarapuru/nivi.git

   
