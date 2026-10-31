# AI Worker Stress Detection System

## Project Overview
The AI Worker Stress Detection System is an experimental project designed to explore worker stress analysis using facial emotion classification and a Streamlit dashboard.

The project includes a Google Colab notebook for model experimentation and a Python-based Streamlit application for displaying stress analysis results.

## Features
- Facial emotion categories: Angry, Disgust, Fear, Happy, Neutral, Sad, and Surprise.
- Three stress levels: Low, Medium, and High.
- Personalized suggestions based on the assigned stress level.
- Dataset analysis and results table.
- Stress summary and emotion distribution charts.
- Interactive Streamlit dashboard.

## Technologies Used
- Python
- Streamlit
- Pandas
- Google Colab
- Jupyter Notebook
- Hugging Face Transformers / PyTorch (Colab model experimentation)

## Project Structure

```text
AI-Worker-Stress-Detection/
│
├── app.py
├── Untitled12_ipynb_detector_project.ipynb
├── archive/
│   └── test/
│       ├── angry/
│       ├── disgust/
│       ├── fear/
│       ├── happy/
│       ├── neutral/
│       ├── sad/
│       └── surprise/
│
└── README.md
```

## How to Run the Application

1. Install Python on your computer.
2. Install the required libraries:

```bash
pip install streamlit pandas
```

3. Open the project folder in Command Prompt.
4. Run the application:

```bash
streamlit run app.py
```

5. Open the local URL displayed in the terminal.

## Stress Level Mapping

| Emotion | Stress Level |
|---|---|
| Happy | Low |
| Neutral | Medium |
| Surprise | Medium |
| Angry | High |
| Disgust | High |
| Fear | High |
| Sad | High |

## Future Enhancements
- Integrate real-time facial emotion detection.
- Improve stress classification accuracy.
- Integrate sensors for continuous worker monitoring.
- Develop an IoT-based worker safety monitoring system.

## Disclaimer
This is an experimental academic project. The current Streamlit dashboard assigns stress levels using predefined emotion-to-stress mappings from dataset folder labels. These results are not a medical or psychological diagnosis.

## Author
Addula Siri

Electronics and Communication Engineering (ECE)
