import streamlit as st
from ibm_watsonx_ai.foundation_models import ModelInference
import re

# IBM Watsonx credentials (hardcoded)
model_id = "ibm/granite-3-8b-instruct"
project_id = "d87960d2-d01f-44ba-81ef-a16ad656ad73"
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "lvdUcs_gbbGG-ltm33r7akvMn9EpCQYuI_z7YInwDK_C"
}

st.set_page_config(page_title="EduTutor AI Quiz", layout="centered")
st.title("🎓 EduTutor AI - Interactive MCQ Quiz")

language = st.radio("Choose language:", ("English", "Hindi"))
topic = st.text_input("Enter a topic (e.g., Photosynthesis, पाचन तंत्र):")

if "mcq_data" not in st.session_state:
    st.session_state.mcq_data = []

def parse_mcqs(text):
    questions = []
    blocks = re.split(r"\n\d+\.", text.strip())[1:]
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 5:
            continue
        q_text = lines[0].strip()
        options = {}
        correct = None
        for line in lines[1:]:
            match = re.match(r"([A-D])\. (.+)", line.strip())
            if match:
                options[match.group(1)] = match.group(2)
            elif "Correct Answer" in line:
                correct = line.split(":")[-1].strip().upper()
        if q_text and len(options) == 4 and correct in options:
            questions.append({
                "question": q_text,
                "options": options,
                "answer": correct
            })
    return questions

if st.button("Generate Quiz") and topic.strip():
    lang = "in Hindi" if language == "Hindi" else "in English"
    prompt = (
        f"Generate 5 multiple choice questions {lang} on the topic '{topic}'. "
        "Each question should have 4 options (A, B, C, D) and mention the correct answer at the end."
    )
    model = ModelInference(
        model_id=model_id,
        params={"decoding_method": "greedy", "max_new_tokens": 600},
        project_id=project_id,
        credentials=credentials
    )
    with st.spinner("Generating your quiz..."):
        response = model.generate(prompt)
        text = response["results"][0]["generated_text"]
        parsed = parse_mcqs(text)
        if not parsed:
            st.error("⚠️ No complete MCQs found. Please try a different topic.")
        else:
            st.session_state.mcq_data = parsed

if st.session_state.mcq_data:
    st.subheader("📝 Take the Quiz")
    responses = []
    for i, q in enumerate(st.session_state.mcq_data):
        st.markdown(f"**Q{i+1}: {q['question']}**")
        selected = st.radio(f"Select your answer:", list(q["options"].keys()), key=f"q{i}")
        responses.append((selected, q["answer"]))
        st.write("")

    if st.button("Submit Answers"):
        score = sum(1 for user_ans, correct in responses if user_ans == correct)
        st.success(f"✅ You scored {score} out of {len(responses)}")
        for i, (user_ans, correct) in enumerate(responses):
            if user_ans != correct:
                st.error(f"❌ Q{i+1}: Correct answer was {correct}")
