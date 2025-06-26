# EduTutor AI – Explain & MCQ Generator

EduTutor AI is a smart educational assistant that helps generate topic explanations and multiple choice questions using IBM Watsonx's Granite foundation model. It uses a clean Streamlit interface to let users toggle between two modes: explanation and quiz generation.

---

## 💡 Project Overview

This version allows users to:
- 🧠 Get a detailed explanation of any concept
- 📝 Generate 5 MCQs for a given topic
- 📋 View clean formatted output 

---

## 🛠️ Tech Stack

- **Python** – backend logic
- **Streamlit** – interactive UI
- **IBM Watsonx.ai** – AI-powered responses
- **Granite 3-8b Instruct Model**

---

## 🧪 Sample Prompts

**Mode:** Topic Explanation  
**Input:** `Photosynthesis`  
**Output:** A paragraph explaining the process of photosynthesis clearly

**Mode:** MCQ Generator  
**Input:** `Photosynthesis`  
**Output:**  
```
1. What is photosynthesis?  
A. A process of breathing  
B. Converting light to energy  
C. Reproduction  
D. Fermentation  
Correct Answer: B  
```

---
## 🔗 Live Demo
[▶ Run on Streamlit Cloud](https://edututorai-byute7kcrnvz3563dpscrm.streamlit.app/)
## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open your browser at `http://localhost:8501`

Make sure to update your Watsonx credentials (`apikey`, `project_id`) in `app.py`

---

## 🔗 Important Links

- [IBM Watsonx](https://www.ibm.com/watsonx)
- [IBM Granite Models](https://www.ibm.com/blog/ibm-granite-models)

---

## 👥 Team Info

✍ Team ID -   LTVIP2025TMID32976
Team Size - 2
Team Member -  A Varsha
Team Member -  Achukatla Nazima
