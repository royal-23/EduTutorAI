import streamlit as st
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials

# IBM Watsonx Credentials
api_key = "your_ibm_api_key"
project_id = "your_project_id"
credentials = Credentials(api_key=api_key, url="https://us-south.ml.cloud.ibm.com")

model = ModelInference(
    model_id="google/flan-t5-xl",
    params={"decoding_method": "greedy", "max_new_tokens": 600},
    project_id=project_id,
    credentials=credentials
)

st.title("📘 EduTutor AI - Explain & Quiz")

topic = st.text_input("Enter a topic (e.g., Photosynthesis):")

mode = st.radio("Choose Mode", ["Topic Explanation", "MCQ Generator"])

if st.button("Generate") and topic.strip():
    if mode == "Topic Explanation":
        prompt = f"Explain the topic {topic} in a simple and clear way."
    else:
        prompt = f"Generate 5 multiple choice questions on the topic {topic}.\nEach question must have 4 options (A, B, C, D) and provide the correct answer."

    result = model.generate(prompt)
    
    st.subheader("📄 Generated Output")
    st.text_area("Output", result, height=400)
