import streamlit as st
from groq import Groq

client = Groq(api_key="GROQ_API_KEY")

st.title("Grammar & Tone Fixer")

text = st.text_area("Paste your text here", height=200)

tone = st.selectbox("Choose a tone", [
    "Formal", "Casual", "Professional", "Friendly", "Persuasive"
])

if st.button("Fix it!"):
    if text.strip():
        prompt = f"""
        Rewrite the following text in a {tone} tone.
        Fix all grammar and spelling errors.
        Keep the core meaning intact.

        Text: {text}
        """
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        st.subheader("Rewritten Text")
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter some text!")
