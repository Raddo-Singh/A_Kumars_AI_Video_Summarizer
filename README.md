## **Project Overview**

This project is a simple web application that allows users to upload a video and get a short summary of its content. It uses AI models to first convert the video’s speech into text and then summarize that text into a shorter version. This helps users quickly understand the main points of a video without watching the whole thing.

## **How It Works**

The application follows these steps:

First, the user uploads a video file using the web interface.
Then, the audio is extracted from the video using FFmpeg.
After that, the audio is converted into text using a speech recognition model (Whisper).
If the text is very long, it is divided into smaller parts to make processing easier.
Finally, the text is summarized using a transformer-based model (BART), and the result is shown to the user.

## **Features**

* Upload video files (MP4, MOV, AVI, MKV)
* Automatic speech-to-text conversion
* AI-based text summarization
* Handles long videos using chunking
* Simple and clean user interface using Streamlit

## **Technologies Used**

* Python
* Streamlit (for web app)
* Whisper (for speech-to-text)
* Transformers (for summarization)
* FFmpeg (for audio extraction)


## **Project Structure**

* `app.py` – Streamlit web interface
* `main.py` – Main workflow (video to summary)
* `transcriber.py` – Extracts audio and transcribes it
* `summarizer.py` – Summarizes the text
* `util.py` – Handles text chunking for long inputs

## **How to Run the Project**

1. Install all required libraries using pip.
2. Make sure FFmpeg is installed on your system.
3. Open terminal in the project folder.
4. Run the command:

   ```
   streamlit run app.py
   ```
5. Open the link shown in the terminal and upload a video.

## **Conclusion**

This project shows how AI can be used to save time by automatically summarizing video content. It combines speech recognition and natural language processing into a simple and useful application.
