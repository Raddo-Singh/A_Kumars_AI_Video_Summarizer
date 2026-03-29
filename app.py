import streamlit as st
import tempfile
import os
from main import video_to_summary

def main():
    st.title("A Kumar's Video Summarizer AI")

    uploaded_file = st.file_uploader(
        "Upload a video file", type=["mp4", "mov", "avi", "mkv"]
    )

    if uploaded_file is not None:
        st.write("Transcribing and summarizing. This may take a few moments...")

        # Use temporary file for uploaded video
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
            temp_video.write(uploaded_file.read())
            temp_video_path = temp_video.name

        # Run the video summarizer
        summary_result = video_to_summary(
            video_path=temp_video_path,
            model_size="base",
            summarizer_model_name="facebook/bart-large-cnn",
            use_chunking=True
        )

        st.subheader("Summary")
        st.write(summary_result)

        # Clean up temporary file
        if os.path.exists(temp_video_path):
            os.remove(temp_video_path)

if __name__ == "__main__":
    main()
