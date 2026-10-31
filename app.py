import os
import pandas as pd
import streamlit as st

# Page settings
st.set_page_config(page_title="AI Stress Detector", layout="wide")

st.title("🧠 AI Stress Detection System")

DATASET_PATH = "archive/test"

# Stress mapping
def get_stress(emotion):
    if emotion == "happy":
        return "Low"
    elif emotion in ["neutral", "surprise"]:
        return "Medium"
    else:
        return "High"

# Suggestion mapping
def get_suggestion(stress):
    if stress == "High":
        return "Take a break, practice deep breathing, or talk to someone."
    elif stress == "Medium":
        return "Try relaxation techniques or short walks."
    else:
        return "Keep maintaining your positive mindset!"

# Process dataset
def process_dataset():
    results = []

    for folder in os.listdir(DATASET_PATH):
        folder_path = os.path.join(DATASET_PATH, folder)

        if not os.path.isdir(folder_path):
            continue

        for img in os.listdir(folder_path)[:10]:
            stress = get_stress(folder)
            suggestion = get_suggestion(stress)

            results.append({
                "Image": img,
                "Emotion": folder,
                "Stress Level": stress,
                "Suggestion": suggestion
            })

    return results

# Button
if st.button("Run Stress Analysis on Dataset"):

    with st.spinner("Analyzing dataset..."):

        data = process_dataset()
        df = pd.DataFrame(data)

        st.success("Analysis Completed ✅")

        st.subheader("📊 Results Table")
        st.dataframe(df)

        st.subheader("📈 Stress Summary")
        st.bar_chart(df["Stress Level"].value_counts())

        st.subheader("📉 Emotion Distribution")
        st.bar_chart(df["Emotion"].value_counts())