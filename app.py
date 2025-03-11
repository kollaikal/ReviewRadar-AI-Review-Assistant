import streamlit as st
from openai import OpenAI

# Function to integrate with NVIDIA API
def generate_response(query):
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key="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"
    )
    
    completion = client.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",
        messages=[{"role":"user","content":query}],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024,
        stream=True
    )
    
    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content
    return response

# Streamlit UI for input and output
st.title("Review Radar - AI Review Assistant")

# Styling customizations
st.markdown("""
    <style>
    .stButton>button {
        background-color: #1e1e1e;
        color: white;
        border-radius: 12px;
        padding: 10px;
        font-size: 16px;
        width: 100%;
        height: 50px;
    }
    .stTextArea>textarea {
        background-color: #1e1e1e;
        color: white;
        border-radius: 12px;
        padding: 10px;
        font-size: 16px;
        width: 100%;
        height: 150px;
    }
    </style>
""", unsafe_allow_html=True)

# File upload feature (no file content extraction)
uploaded_file = st.file_uploader("Choose a file (e.g., CSV, TXT, PDF)", type=["csv", "txt", "pdf"])

# Custom prompt for the AI
custom_prompt = st.text_area("Enter a custom prompt for the AI", "Type your prompt here")

# Handling file upload (no extraction, just acknowledgment)
if uploaded_file is not None:
    st.write(f"File '{uploaded_file.name}' uploaded successfully. No content extraction will be done.")

# Generate response when the button is clicked
if uploaded_file is not None and custom_prompt:
    prompt = f"File uploaded: {uploaded_file.name}\n\nCustom prompt: {custom_prompt}"

    if st.button("Generate Response"):
        with st.spinner('Generating response...'):
            result = generate_response(prompt)
        st.write("Response from Model:")
        st.write(result)
else:
    st.write("Please upload a file to get started.")
