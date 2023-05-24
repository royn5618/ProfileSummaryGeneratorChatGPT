import streamlit as st
from  helper import *

st.set_page_config(layout="wide",page_title="CV Assistant")
st.header(":orange[PyCon Demo: Resume Building Assistant]")
st.markdown("""---""")

# PART 1
with st.form("form1"):
    uploaded_file = st.file_uploader(":orange[Upload Your CV to Generate Profile Summary:]")
    if uploaded_file is not None:
        try:
            profile = extract_data(uploaded_file)
            st.write(profile)
        except:
            st.error('Unable to parse the uploaded file', icon="😞")
    gen_sum = st.form_submit_button("Generate Summary")
    if gen_sum:
        prompt_builder = "Generate a summary of the profile."
        """
        BASIC Additions
        1. Add word limit - Using max_tokens or specifying in the prompt.
        2. Set a Tone - Add to the prompt - "Professional"
        """
        st.write("Summary Generated")

# PART 2
with st.form("form2"):
    job_desc = st.text_area(":orange[Enter a Job Description:]")
    ext_kwds = st.form_submit_button("Extract Keywords")
    if ext_kwds:
        st.write("Extracted Keywords")

# PART 3
with st.form("form3"):
    # COMBINE BOTH: Generate a summary using the keywords.
    job_desc = st.text_area(":orange[Enter a Job Description:]")
    profile = None
    uploaded_file = st.file_uploader(":orange[Upload Your CV to Generate Profile Summary:]")
    if uploaded_file is not None:
        try:
            profile = extract_data(uploaded_file)
        except:
            st.error('Unable to parse the uploaded file', icon="😞")
    gen_sum_again = st.form_submit_button("Generate Summary")
    keywords = "Get Keywords"  # TODO
    if gen_sum_again:
        prompt_builder = f"Generate a summary of the profile using the following keywords: {keywords}"
        """
        BASIC Additions
        1. Add word limit - Using max_tokens or specifying in the prompt.
        2. Set a Tone - Add to the prompt - "Professional"
        """
        st.write("Summary Generated")