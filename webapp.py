import streamlit as st
from helper import *
import openai
from openai_helper import get_response

st.set_page_config(layout="wide", page_title="Content Generation")
st.header(":orange[PyCon Demo: Content Generation using ChatGPT]")
st.markdown("""---""")

# PART 1
with st.form("form1"):
    uploaded_file = st.file_uploader(":orange[Upload Your CV to Generate Profile Summary:]")
    if uploaded_file is not None:
        try:
            profile = extract_data(uploaded_file)
            # st.write(profile)
        except:
            st.error('Unable to parse the uploaded file', icon="😞")
    gen_sum = st.form_submit_button("Generate Summary")
    if gen_sum:
        # TODO: Add a tone.
        tone = None
        # TODO: Add target audience
        target = None
        # TODO: Add first/third person
        person = None
        prompt_builder = f"Generate a summary of the profile: --- {profile} --- "
        _summary = get_response(prompt=prompt_builder)
        st.write(_summary)

# PART 2
with st.form("form2"):
    job_desc = st.text_area(":orange[Enter a Job Description:]")
    ext_kwds = st.form_submit_button("Extract Keywords")
    if ext_kwds:
        prompt_builder = f"Extract keywords from this job description: {job_desc}"
        _keywords = get_response(prompt=prompt_builder)
        st.write("Extracted Keywords")
        st.write(_keywords)

# PART 3
with st.form("form3"):
    # COMBINE BOTH: Generate a summary using the keywords.
    given_content = st.text_area(":orange[Rewrite the following content:]")
    button_rewrite = st.form_submit_button("Rewrite")
    if button_rewrite:
        prompt_builder = f"Rewrite the following in a professional tone in five bullets: {given_content}"
        rewritten_content = get_response(prompt=prompt_builder)
        st.write(rewritten_content)
