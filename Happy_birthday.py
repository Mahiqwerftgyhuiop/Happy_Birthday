import streamlit as st
import time

st.set_page_config(page_title="Happy Birthday 🎂", page_icon="🎈", layout="centered")

st.title("🎉 Happy Birthday Sravas🎉")

name = "Sravs"

# Custom birthday caption
st.markdown(f"""
<div style='text-align: center; font-size: 20px; margin-top: 20px;'>
    🌟 <b>Wishing {name} a day full of love, laughter, and cake! 🍰</b> 🌟<br>
    May your year ahead sparkle with happiness. ✨
</div>
""", unsafe_allow_html=True)

# Pre-load the audio file path
audio_file_path = "happy_birthday_song.mp3"

# Button to celebrate
if st.button("🎂 Celebrate!"):
    # Inject custom HTML to autoplay audio
    st.markdown(f"""
    <audio autoplay hidden>
        <source src="{audio_file_path}" type="audio/mpeg">
    </audio>
    """, unsafe_allow_html=True)

    st.write("🎶 Singing your birthday song... 🎶")
    placeholder = st.empty()

    lyrics = [
        "Happy Birthday to You 🎵",
        "Happy Birthday to You 🎶",
        f"Happy Birthday dear {name} 🎂",
        "Happy Birthday to You! 🎉"
    ]

    for line in lyrics:
        placeholder.markdown(f"<h3 style='text-align: center;'>{line}</h3>", unsafe_allow_html=True)
        time.sleep(1)

    st.balloons()
    st.success(f"🎊 Let's party, {name}! 🎊")
