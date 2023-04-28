import openai
import plotly.io as pio
from io import StringIO
import streamlit as st
import pdfplumber

from config import CONFIG
from setup import setup

setup("Profile Summarizer | GPT3")
pio.templates.default = "plotly"


st.header("Generative AI: Profile Summarizer")
openai.api_key = CONFIG.API_KEY
# uploaded_files = st.file_uploader("", accept_multiple_files=False)
uploaded_file = st.file_uploader("Upload your CV or Profile in PDF format.", type="pdf")

prof = 'professional'
exciting = 'exciting'
sad = 'sad'

tone = st.radio(":orange[Select the tone 👇]",
                     (prof, exciting, sad))


def extract_data(feed):
    data = []
    with pdfplumber.open(feed) as pdf:
        all_text = []
        for each_page in pdf.pages:
            all_text.append(each_page.extract_text(x_tolerance=3,
                                                   y_tolerance=3,
                                                   layout=False,
                                                   x_density=7.25,
                                                   y_density=13).replace('\n', ' '))
        return " ".join(all_text)


profile = None

if uploaded_file is not None:
    try:
        profile = extract_data(uploaded_file)
        # st.write(profile)
    except:
        st.error('Unable to parse the uploaded file', icon="😞")

generate = st.button('Generate Summary')
if generate:
    prompt = "Write a {} profile summary of {}".format(tone, profile)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    output = response["choices"][0]["text"]
    st.write(output)