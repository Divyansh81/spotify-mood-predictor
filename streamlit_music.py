import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model_predicted.pkl")

st.title("🎵 Spotify Song Mood Predictor")
st.write("""
Adjust the audio features of a song, then click **Predict Mood**.  
The model will predict if the song mood is **Happy** or **Sad** based on valence.
""")

# Feature sliders with typical Spotify ranges
acousticness = st.slider("Acousticness", 0.0, 1.0, 0.5)
danceability = st.slider("Danceability", 0.0, 1.0, 0.5)
energy = st.slider("Energy", 0.0, 1.0, 0.5)
instrumentalness = st.slider("Instrumentalness", 0.0, 1.0, 0.0)
liveness = st.slider("Liveness", 0.0, 1.0, 0.2)
loudness = st.slider("Loudness (dB)", -60.0, 0.0, -20.0)
speechiness = st.slider("Speechiness", 0.0, 1.0, 0.05)
tempo = st.slider("Tempo (BPM)", 50.0, 200.0, 120.0)

# Prepare feature vector
features = np.array([[acousticness, danceability, energy, instrumentalness, liveness,
                      loudness, speechiness, tempo]])

if st.button("Predict Mood"):
    prediction = model.predict(features)[0]
    if prediction == 1:
        mood = "😊 Happy"
        st.balloons()
    else:
        mood = "😢 Sad"
        st.error("Oh no! The song sounds sad.")
        # Or use snow animation instead
        # st.snow()

    st.success(f"Predicted Mood: **{mood}**")
