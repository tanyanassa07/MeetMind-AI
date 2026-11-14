# 🎙️ MeetMind AI
### AI-Powered Meeting Assistant

MeetMind AI is a Python-based project that converts meeting audio and video into meaningful transcripts, summaries, and actionable insights using AI.

## 🚀 Features
- YouTube audio and local audio/video processing
- Speech-to-text using **Whisper** and **Sarvam AI**
- AI-powered meeting summarization
- Action items and key decision extraction
- Open questions identification
- Automatic meeting title generation

## 🛠️ Tech Stack
**Python | Whisper | Sarvam AI | Mistral AI | LangChain | FFmpeg | Pydub | yt-dlp**

## ⚙️ Setup
**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Create a `.env` file with your own API keys**
```dotenv
MISTRAL_API_KEY=your_mistral_api_key
SARVAM_API_KEY=your_sarvam_api_key
```

**3.** Configure FFmpeg for your system and run the local test script.

> 🔒 Never upload your real API keys or `.env` file to GitHub.

## 🔮 Future Enhancements
- Streamlit-based user interface
- RAG chatbot using LangChain and ChromaDB
- PDF/TXT report generation
- Cloud deployment

## 📌 Project Status
🚧 Backend prototype under development.