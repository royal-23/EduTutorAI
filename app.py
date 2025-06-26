
import streamlit as st
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials

# IBM Credentials
api_key = "your_ibm_api_key"
project_id = "your_project_id"
credentials = Credentials(api_key=api_key, url="https://us-south.ml.cloud.ibm.com")

model = ModelInference(
    model_id="google/flan-ul2",
    params={"decoding_method": "greedy", "max_new_tokens": 800},
    project_id=project_id,
    credentials=credentials,
)

st.title("🎓 EduTutor AI - Explain & Quiz (Hindi/English)")

language = st.radio("Choose Language / भाषा चुनें:", ["English", "Hindi"])
topic = st.text_input("Enter a topic / विषय दर्ज करें (e.g., Photosynthesis, प्रकाश संश्लेषण):")
mode = st.radio("Choose Mode:", ["Topic Explanation", "MCQ Generator"])

if st.button("Generate") and topic.strip():
    if language == "Hindi":
        topic_lang = "हिंदी में"
        explain_prompt = f""{topic}" विषय को विस्तार से समझाइए।"
        mcq_prompt = f"{topic} विषय पर 5 बहुविकल्पीय प्रश्न हिंदी में तैयार करें। हर प्रश्न के चार विकल्प (A, B, C, D) और उत्तर सहित।"
    else:
        topic_lang = "in English"
        explain_prompt = f"Explain the topic "{topic}" in detail in simple English."
        mcq_prompt = f"Generate 5 multiple choice questions {topic_lang} on the topic "{topic}" with four options (A, B, C, D) and mention the correct answer."

    if mode == "Topic Explanation":
        with st.spinner("Generating explanation..."):
            response = model.generate(prompt=explain_prompt)
            st.subheader("📘 Topic Explanation / विषय व्याख्या")
            st.write(response)
    else:
        with st.spinner("Generating MCQs..."):
            response = model.generate(prompt=mcq_prompt)
            st.subheader("📝 Generated MCQs / अभ्यास प्रश्न")
            st.text_area("MCQs", response, height=400)
