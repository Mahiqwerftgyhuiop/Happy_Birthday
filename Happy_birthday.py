import streamlit as st
import time

st.set_page_config(page_title="Happy Birthday 🎂", page_icon="🎈", layout="centered")

st.title("🎉 Happy Birthday Sravs🎉")

# Get user's input
name = "Sravs"

# Caption text
st.markdown(f"""
<div style='text-align: center; font-size: 20px; margin-top: 20px;'>
    🌟 <b>Wishing {name} a day full of love, laughter, and cake! 🍰</b> 🌟<br>
    May your year ahead sparkle with happiness and good health. ✨
</div>
""", unsafe_allow_html=True)

# Celebrate button
if st.button("🎂 Celebrate!"):
    # Play audio using custom HTML (autoplay + hidden)
    audio_url = "https://raw.githubusercontent.com/its-akashk/happy-birthday-audio/main/happy_birthday_song.mp3"  # Replace with your own hosted file if needed

    st.markdown(f"""
    <audio autoplay hidden>
        <source src="{audio_url}" type="audio/mpeg">
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
