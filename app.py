import streamlit as st
from afm_tools import read_afm_csv, plot_afm_surface, compute_stats
from chat_engine import ask_afm_question 


st.set_page_config(page_title="AFM-GPT", layout="wide")
st.title("🧠 AFM-GPT: AI Assistant for Surface Analysis")

api_key = None
try:
    api_key = st.secrets["openrouter_api_key"]
    st.success(" yay !!! API Key loaded from Streamlit secrets! 🎉")
except KeyError:

    st.warning("Gemini API Key not found in Streamlit secrets. "
               "Please enter it below or configure `secrets.toml`.")
    api_key = st.text_input("🔑 Enter your OpenRouter API Key:", type="password")



# Upload AFM CSV file
uploaded_file = st.file_uploader("📤 Upload AFM .CSV File", type="csv")

if uploaded_file:
    # Read and display raw data
    data = read_afm_csv(uploaded_file)
    st.subheader("📊 Surface Preview")
    st.dataframe(data.head())

    # Show 3D surface plot
    st.subheader("🗻 3D Surface Plot")
    fig = plot_afm_surface(data)
    st.pyplot(fig)

    # Compute surface stats
    avg, rough = compute_stats(data)
    st.markdown(f"- **Average height:** `{avg:.4f}`")
    st.markdown(f"- **Surface roughness (RMS):** `{rough:.4f}`")

    # GPT-based question-answering
    if api_key: # Check if the API key is available (either from secrets or input)
        user_question = st.text_input("💬 Ask a question about this surface:")
        if user_question:
            context = f"Average height = {avg:.4f}, Roughness = {rough:.4f}"
            
            # Call the ask_afm_question function (which now uses Gemini)
            response = ask_afm_question(user_question, context, api_key)
            
            st.markdown("### 🤖 AI Answer")
            st.write(response)
    else:
        st.error("⚠️ A Google Gemini API key is required to ask questions.")










# cd E:\AFM
# .\.venv\Scripts\activate  # If not already active
# streamlit run app.py
# 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

# https://openrouter.ai/ i used this for APi