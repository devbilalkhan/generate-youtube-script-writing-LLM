import streamlit as st
import os
from utils import generate_script

def set_style():
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #FF0000;
        color: white;
    }
    div.stButton > button:first-child:hover {
        background-color: #FF8080;
        color: white;
    </style>
    """, unsafe_allow_html=True)

def set_columns():
    col1, col2 = st.columns([4,1])
    col1.title('Youtube Script Writing Tool')
    col2.image('static/image.png', width=100)

def get_user_input():
    prompt = st.text_input('Enter your prompt here', 'Write a script for a youtube video about...')
    video_length = st.text_input('Expected video length (in minutes)', '2')
    creativity = st.slider('Words limit', 0.0, 1.0, 0.1)
    return prompt, video_length, creativity

def generate_and_display_script(prompt, video_length, creativity):
    submit = st.button("Generate Script")
    if submit:
        with st.spinner('Generating script...'):
            title, script = generate_script(prompt, video_length, creativity)
     
        st.title(title)
        st.subheader('Here is your script:')
        st.text_area("Script:", value=script, height=500, max_chars=None, key=None)

def main():
    os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]
    set_style()
    set_columns()
    prompt, video_length, creativity = get_user_input()
    generate_and_display_script(prompt, video_length, creativity)

if __name__ == "__main__":
    main()

