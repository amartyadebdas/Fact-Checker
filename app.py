# app.py
import streamlit as st
from src.pipeline_2 import main as run_pipeline_with_multi_claims  # Import the main function from pipeline.py

def main():
    st.title("Simple Claim Verification App")
    st.markdown("Enter one or more claims to verify.")

    user_input = st.text_area("Enter Claim(s):", height=200)

    if st.button("Verify"):
        if user_input:
            with st.spinner("Processing claims..."):
                results = run_pipeline_with_multi_claims(user_input, st.session_state.llm)

            st.subheader("Verification Results:")
            for claim, evidence in results.items():
                st.markdown(f"**Claim:** {claim}")
                st.markdown(f"<div style='border: 1px solid #e0e0e0; padding: 10px; border-radius: 5px; background-color: #f9f9f9;'>{evidence}</div>", unsafe_allow_html=True)
                st.markdown("---")
        else:
            st.warning("Please enter a claim.")

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    from langchain_openai.chat_models import ChatOpenAI

    if 'llm' not in st.session_state:
        st.session_state.llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

    main()