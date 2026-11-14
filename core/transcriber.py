import whisper
import os
import requests

WHISPER_MODEL = os.getenv("WHISPER_MODEL", "small")

_model = None
from dotenv import load_dotenv
load_dotenv()
SARVAM_API_KEY=os.getenv("SARVAM_API_KEY") 
SARVAM_STT_TRANSLATE_URL = "https://api.sarvam.ai/speech-to-text-translate"
SARVAM_MODEL = os.getenv("SARVAM_MODEL", "saaras:v2.5")

def load_model():
    global _model

    if _model is None:
        print("loading model ...")
        _model = whisper.load_model(WHISPER_MODEL)
        print("whisper model loaded successfully")

    return _model


def transcribe_chunk_whisper(chunk_path: str, translate: bool = False) -> str:
    model = load_model()

    result = model.transcribe(chunk_path, task="transcribe")

    return result["text"]




def transcribe_chunk_sarvam(chunk_path: str) -> str:
    if not SARVAM_API_KEY:
        raise RuntimeError("SARVAM_API_KEY is not set in environment / .env")

    headers = {"api-subscription-key": SARVAM_API_KEY}

    with open(chunk_path, "rb") as f:
        files = { "file": (os.path.basename(chunk_path), f, "audio/wav")}

        data = { "model": SARVAM_MODEL, "with_diarization": "false"
                 }

        response = requests.post(
            SARVAM_STT_TRANSLATE_URL,
            headers=headers,
            files=files,
            data=data
        )
    if not response.ok:
       print("Sarvam Error Response:", response.text)
    print("Sarvam response:", response.text)
    response.raise_for_status()

    return response.json().get("transcript","")


def transcribe_chunk(chunk_path: str, language: str = "english") -> str:
    """
    Route one chunk to Whisper or Sarvam depending on language choice.
    - english  -> Whisper (local model)
    - hinglish -> Sarvam (translates to English while transcribing)
    """

    if language.lower() == "hinglish":
        return transcribe_chunk_sarvam(chunk_path)

    return transcribe_chunk_whisper(chunk_path)

def transcribe_all(chunks: list, language: str = "english") -> str:

    full_transcript = ""

    engine = "Sarvam AI" if language.lower() == "hinglish" else "Whisper"
    print(f"Using {engine} for transcription.")

    for i, chunk in enumerate(chunks):

        print(f"Transcribing chunk {i + 1}/{len(chunks)}...")

        text = transcribe_chunk(chunk, language=language)

        full_transcript += text + " "

    print("Transcription complete.")

    return full_transcript.strip()

