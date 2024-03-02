from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st
import os


def set_api_key():
    """Sets the OpenAI API key from Streamlit secrets."""
    os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]


def create_openai_instance(creativity):
    """Creates an OpenAI instance with a given creativity."""
    llm = OpenAI(temperature=creativity)
    return llm

def create_title_search_chain(creativity):
    """Creates a chain for generating a title for a YouTube video."""
    return PromptTemplate(
        input_variables=['subject'],
        template='Please come up for a title for a Youtube video on {subject}.'
    )


def create_script_chain(creativity):
    """Creates a chain for generating a script for a YouTube video."""
    return PromptTemplate(
        input_variables=['title', 'duration'],
        template='Create a script for a YouTube video about {title} of {duration}. The video should be $duration minutes long. The script should be creative and engaging.'
    )


def generate_script(prompt, video_length, creativity):
  """Generates a title and script for a YouTube video based on the given prompt, 
     video length, and creativity level.
  """
  set_api_key()
  title_search = create_title_search_chain(creativity)
  script_template = create_script_chain(creativity)

  llm = OpenAI(temperature=creativity)
  title_chain = LLMChain(llm=llm, prompt=title_search, verbose=True)
  script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True)

  title = title_chain.run(prompt)

  script = script_chain.run(title=title, duration=video_length)

  return title,script