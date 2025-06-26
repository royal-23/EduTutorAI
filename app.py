import streamlit as st
from ibm_watsonx_ai.foundation_models import ModelInference

# IBM Watsonx model credentials
model_id = "ibm/granite-3-8b-instruct"
project_id = "d87960d2-d01f-44ba-81ef-a16ad656ad73"
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "lvdUcs_gbbGG-ltm33r7akvMn9EpCQYuI_z7YInwDK_C"
}

# UI
st.set_page_config(page_title="EduTutor AI - Explain & MCQ", layout="centered")
st.title("📘 EduTutor AI - Explain & Quiz")
st.markdown("Get an explanation or generate MCQs for any topic using AI.")

# Topic and mode
topic = st.text_input("Enter a topic (e.g., Photosynthesis, Gravity, etc.)")
mode = st.radio("Choose what to generate:", ["Topic Explanation", "MCQ Generator"])

if st.button("Generate") and topic.strip():
    # Construct prompt based on mode
    if mode == "Topic Explanation":
        prompt = f"Explain the topic '{topic}' in detail as if teaching a student."
    else:
        prompt = (
            f"Generate 5 multiple choice questions on the topic '{topic}'. "
            f"Each question should have 4 options (A, B, C, D) and indicate the correct answer at the end."
        )

    # Model inference
    model = ModelInference(
        model_id=model_id,
        params={"decoding_method": "greedy", "max_new_tokens": 600},
        project_id=project_id,
        credentials=credentials
    )

    # Display result
    with st.spinner("Generating response..."):
        response = model.generate(prompt)
        result_text = response["results"][0]["generated_text"]

    st.markdown("### 📄 Generated Output")
    st.markdown(result_text)
