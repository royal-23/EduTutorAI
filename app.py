import streamlit as st
from ibm_watsonx_ai.foundation_models import ModelInference

# IBM Watsonx model credentials
model_id = "ibm/granite-3-8b-instruct"
project_id = "e148ca84-35e1-433d-9d5e-a71c64c3def8"
credentials = {
    "url": "https://eu-de.ml.cloud.ibm.com",
    "apikey": "bCDB66qGQ4GEdDAu6o6kQ-BM4iLenxHfXZDZCrwtMwKf"
}

# Streamlit App UI
st.set_page_config(page_title="EduTutor AI - MCQ Generator", layout="centered")
st.title("📘 EduTutor AI - MCQ Generator")
st.markdown("Generate multiple choice questions for any topic using AI.")

topic = st.text_input("Enter a topic (e.g., Gravity, Photosynthesis, etc.)")

if st.button("Generate MCQs") and topic.strip():
    prompt = (
        f"Generate 5 multiple choice questions on the topic '{topic}'. "
        f"Each question should have 4 options (A, B, C, D) and indicate the correct answer at the end."
    )

    model = ModelInference(
        model_id=model_id,
        params={"decoding_method": "greedy", "max_new_tokens": 500},
        project_id=project_id,
        credentials=credentials
    )

    with st.spinner("Generating MCQs..."):
        response = model.generate(prompt)
        mcqs = response["results"][0]["generated_text"]

    st.markdown("### 📄 Generated MCQs")
    st.markdown(mcqs)