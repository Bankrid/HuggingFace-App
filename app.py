import streamlit as st
import torch

from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='openai-gpt')


# App Declaration

def main():
    # Header
    st.set_page_config(layout="centered", page_title="LLM for marketing")
    st.write("# LLM For Marketing")
    st.write("### A Solution Achitecture For Targeted Marketing")

    # Create different Pages
    page = ["Enter Persona Details", "Input Your Marketing Content", "Select The Model Role"]
    page_options = ["Model Interface","User Guide", "Solution Overview", "FAQs"]
    page_selection = st.sidebar.selectbox("Choose Page", page_options)

    # Design the Model Interface
    if page_selection == "Model Interface":
        # Header
        st.title("Model Interface")
        st.write("Insito: An Ideal Solution for targeted Marketing")
        # st.image('img/llm.jpg', use_column_width = True)

        # LLM selection
        sys = st.radio("Choose model of choice",
                ("Llama 2", "OpenAI"))

        # Build the interfaces
        Role = st.selectbox("Select the Model Role",
        ("Business Advisor", "Tech Guru", "Expert Waterwaste Disposal"))
        st.markdown("""
            ### Personal Demographics
            """)
        st.markdown("""
        <style>
            div[data-test-id="column"]:nth-of-type(1)
            {
                border:1px solid red;
            }
            div[data-test-id="column"]:nth-of-type(2)
            {
                border:1px solid blue;
                text-align: end;
            }
        </style>

        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            st.text_input("Role / Postion", """Example: Chief Technological Officer""")
            # st.selectbox("Sex",("Both","Male", "Female"))
            # st.select_slider("Age", (1,50))
            age = st.slider('Age / Age range',0, 100, (30,40))
            # st.write('Age:', age)
            # print(type(age))

        with col2:
            st.text_input("Industry", """Example: Marketing""")
            # st.selectbox("Marital Status",("Single", "Married","Divorced","Widowed"))
            st.text_input("Location", """Example: USA""")

        Persona = st.text_area("Enter Pain Points", """Example; A tool to automate everyday tasks.
        """)

        Content = st.text_area("Marketing Content", "Type or Paste Your Marketing Content Here")
        st.write("(Note: You can increase the height of the text area by dragging it through the bottom right corner of the box)")

        Content_text = [Role, Persona, Content]

        # Evaluate the content
        if sys == "Llama 2":
            if st.button("Analyze"):

                try:
                    with st.spinner("Making your content better! Wait for it..."):
                       # improved_content = model(Content_text[0], Content_text[1], Content_text[2])
                       improved_content = generator(Content)
                    st.title("Result")
                    st.write(improved_content[0]['generated_text']
)
                except:
                    st.error("Something is wrong")

        if sys == "OpenAI":
            if st.button("Analyze"):

                try:
                    with st.spinner("Making your content better! Wait for it..."):
                        improved_content = model(Content_text[0], Content_text[1], Content_text[2])
                    st.title("Result")
                    st.write(improved_content)
                except:
                    st.error("Something is wrong")

if __name__ == '__main__':
    main()
