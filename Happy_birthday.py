import streamlit as st
import time

st.set_page_config(page_title="Happy Birthday 🎂", page_icon="🎈", layout="centered")

st.title("🎉 Happy Birthday App 🎉")

# Name input
name = st.text_input("Enter the birthday person's name:", "Friend")

# Birthday caption
st.markdown(f"""
<div style='text-align: center; font-size: 20px; margin-top: 20px;'>
    🌟 <b>Wishing {name} a day full of love, laughter, and joy! 🎁</b> 🌟<br>
    May your year ahead be as sweet as cake. 🍰
</div>
""", unsafe_allow_html=True)

# Load & play the birthday song
try:
    audio_file = open("happy_birthday_song.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")
except FileNotFoundError:
    st.warning("🎵 Birthday song file not found. Please add 'happy_birthday_song.mp3' to your repo.")

# Celebrate button
if st.button("🎂 Celebrate!"):
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
