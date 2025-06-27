import streamlit as st
from ibm_watsonx_ai.foundation_models import ModelInference

# IBM Watsonx model credentials
model_id = "ibm/granite-3-8b-instruct"
project_id = "d87960d2-d01f-44ba-81ef-a16ad656ad73"
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": st.secrets["IBM_API_KEY"]
}

# Streamlit UI
st.set_page_config(page_title="EduTutor AI - Explain & MCQ", layout="centered")
st.title("📘 EduTutor AI - Explain & Quiz (English / हिंदी)")
st.markdown("Get an explanation or generate MCQs for any topic using AI.")

# Language selection
language = st.radio("Choose Language / भाषा चुनें:", ["English", "Hindi"])
topic = st.text_input("Enter a topic (e.g., Photosynthesis) / विषय दर्ज करें:")
mode = st.radio("Choose what to generate / क्या जनरेट करना है:", ["Topic Explanation", "MCQ Generator"])

if st.button("Generate") and topic.strip():
    # Prompt creation based on language and mode
    if language == "English":
        if mode == "Topic Explanation":
            prompt = f"Explain the topic '{topic}' in detail as if teaching a student."
        else:
            prompt = (
                f"Generate 5 multiple choice questions on the topic '{topic}'. "
                f"Each question should have 4 options (A, B, C, D) and indicate the correct answer at the end."
            )
    else:
        if mode == "Topic Explanation":
            prompt = f"विषय '{topic}' को एक छात्र को पढ़ाते समय विस्तार से समझाएं।"
        else:
            prompt = (
                f"विषय '{topic}' पर 5 बहुविकल्पीय प्रश्न (MCQs) बनाएं। "
                f"प्रत्येक प्रश्न में 4 विकल्प (A, B, C, D) हों और उत्तर भी शामिल करें।"
            )

    # Model inference
    model = ModelInference(
        model_id=model_id,
        params={"decoding_method": "greedy", "max_new_tokens": 600},
        project_id=project_id,
        credentials=credentials
    )

    # Display results
    with st.spinner("Generating response..."):
        response = model.generate(prompt)
        result_text = response["results"][0]["generated_text"]

    st.markdown("### 📄 Generated Output / उत्पन्न उत्तर")
    st.markdown(result_text)
