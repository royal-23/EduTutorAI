import streamlit as st
from ibm_watsonx_ai.foundation_models import ModelInference

# IBM Watsonx model credentials
model_id = "ibm/granite-3-8b-instruct"
project_id = "d87960d2-d01f-44ba-81ef-a16ad656ad73"
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "lvdUcs_gbbGG-ltm33r7akvMn9EpCQYuI_z7YInwDK_C"
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
