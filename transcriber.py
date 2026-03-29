import whisper
import os
import ffmpeg  # use ffmpeg-python instead of subprocess

def extract_audio(video_path, audio_path: str = "temp_audio.wav") -> str:
    """Extract audio from video using ffmpeg-python (works on Streamlit Cloud)"""
    if os.path.exists(audio_path):
        os.remove(audio_path)

    try:
        (
            ffmpeg
            .input(video_path)
            .output(audio_path, **{'q:a': 0, 'map': 'a'})
            .run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as e:
        print("FFmpeg error:", e.stderr.decode())
        raise e

    return audio_path

def transcribe_audio(audio_path: str, model_size: str = "base") -> str:
    """Transcribe audio using Whisper (CPU for Streamlit Cloud)"""
    model = whisper.load_model(model_size, device="cpu")
    result = model.transcribe(audio_path)
    return result["text"]
