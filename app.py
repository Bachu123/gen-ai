


import openai
from gtts import gTTS
import streamlit as st
import os

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

def generate_song(prompt):
    response = openai.Completion.create(
        model="sk-proj-gSnP87WFO0m12LfAYsT2T3BlbkFJIBD0XuGTFV4ahen5MiAj",  # Use the latest available model
        prompt=prompt,
        max_tokens=150,  # Adjust the number of tokens as needed
        n=1,
        stop=None,
        temperature=0.7,  # Adjust the temperature for creativity
    )

    song = response.choices[0].text.strip()
    return song

def lyrics_to_audio(lyrics, filename="song.mp3"):
    tts = gTTS(text=lyrics, lang='en')
    tts.save(filename)
    print(f"Audio saved as {filename}")

# Streamlit App
st.title("Song Lyrics Generator and Audio Converter")

# Input prompt from the user
prompt = st.text_input("Enter a prompt for the song lyrics:")

if st.button("Generate Song"):
    if prompt:
        song_lyrics = generate_song(prompt)
        st.subheader("Generated Song Lyrics")
        st.write(song_lyrics)

        # Convert lyrics to audio
        lyrics_to_audio(song_lyrics, "song.mp3")

        # Display audio player
        audio_file = open("song.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
    else:
        st.warning("Please enter a prompt for the song lyrics.")