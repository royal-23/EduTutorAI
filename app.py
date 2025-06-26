import streamlit as st
from ibm_watsonx_ai.foundation_models import ModelInference
import re

# Watsonx credentials
model_id = "ibm/granite-3-8b-instruct"
project_id = "d87960d2-d01f-44ba-81ef-a16ad656ad73"
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "lvdUcs_gbbGG-ltm33r7akvMn9EpCQYuI_z7YInwDK_C"
}

st.set_page_config(page_title="EduTutor AI - Bilingual", layout="centered")
st.title("🌐 EduTutor AI - Explain & Quiz (Hindi/English)")

language = st.radio("Choose Language / भाषा चुनें", ["English", "Hindi"])
topic = st.text_input("Enter a topic / विषय दर्ज करें (e.g., Photosynthesis, पाचन तंत्र):")

st.subheader("📄 Generated MCQs")
st.text_area("MCQs", result, height=400)

if st.button("Generate Explanation and MCQs") and topic.strip():
    try:
        model = ModelInference(
            model_id=model_id,
            params={"decoding_method": "greedy", "max_new_tokens": 800},
            project_id=project_id,
            credentials=credentials
        )

        lang = "in Hindi" if language == "Hindi" else "in English"

        with st.spinner("Explaining the topic... / विषय को समझाया जा रहा है..."):
            exp_prompt = f"Explain the concept of '{topic}' {lang}."
            explanation = model.generate(exp_prompt)["results"][0]["generated_text"]
            st.subheader("📖 Explanation / व्याख्या")
            st.write(explanation)

        with st.spinner("Generating questions... / प्रश्न तैयार किए जा रहे हैं..."):
            mcq_prompt = f"""Generate 5 multiple choice questions {lang} on the topic '{topic}'.
Each question should be numbered (1., 2., etc)
Each should have 4 options labeled A., B., C., D.
Also include the correct answer like: Correct Answer: B"""
            quiz_response = model.generate(mcq_prompt)["results"][0]["generated_text"]

            mcqs = parse_mcqs(quiz_response)

        st.subheader("📝 Practice Questions / अभ्यास प्रश्न")
        if mcqs:
            for i, q in enumerate(mcqs):
                st.markdown(f"**Q{i+1}: {q['question']}**")
                for key, val in q["options"].items():
                    st.markdown(f"{key}. {val}")
                st.success(f"✅ Correct Answer: {q['answer']}")
        else:
            st.warning("⚠️ No valid MCQs generated. Try another topic. / मान्य प्रश्न नहीं मिले। कृपया दूसरा विषय आज़माएँ।")

    except Exception as e:
        st.error(f"Something went wrong: {e}")
