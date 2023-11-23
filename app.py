import streamlit as st
from langchain.llms import CTransformers
from langchain.chains import LLMChain
from langchain import PromptTemplate

llm = CTransformers(model = "model\llama-2-7b-chat.ggmlv3.q2_K.bin",
                    model_type = "llama",
                    config={'max_new_tokens':2000, "temperature":0.5, 'context_length' : 2048})

def main():
    primary_color = "#2E3F4F"  # Dark Blue
    secondary_color = "#FF6B6B"  # Coral Pink
    accent_color = "#6AB187"  # Muted Green

    custom_styles = f"""
        <style>
            /* Body styles */
            body {{
                color: white;
                background-color: {primary_color};
                font-family: Arial, sans-serif;
            }}

            /* Sidebar styles */
            .sidebar {{
                width: 180px !important;
            }}

            .sidebar-content {{
                background-color: {secondary_color} !important;
                width: 160px !important;
                color: white !important;
            }}

            .sidebar .sidebar-content .block-container {{
                color: white !important;
                background-color: {secondary_color} !important;
            }}

            /* Button styles */
            .stButton > button {{
                color: white !important;
                background-color: {accent_color} !important;
                border-color: white !important;
            }}

            /* Text input styles */
            .stTextInput > div > div > input, .stTextArea > div > div > textarea {{
                background-color: white !important;
                color: {primary_color} !important;
                border-color: {secondary_color} !important;
            }}

            /* Expander styles */
            .streamlit-expanderHeader {{
                color: white !important;
                background-color: {secondary_color} !important;
            }}

            .streamlit-expanderContent {{
                color: white !important;
                background-color: {primary_color} !important;
            }}

    """
    
    st.markdown(custom_styles, unsafe_allow_html=True)

    page_options = ["Model Interface", "User Guide", "Solution Overview", "FAQs"]
    page_selection = st.sidebar.selectbox("Choose Page", page_options)

    if page_selection == "Model Interface":
        st.image('img/Contentify.png', use_column_width=True)

        Niche = st.selectbox("Select your marketing niche", ("Financial Services", "Telco", "Waterwaste Disposal", "Academy Partnerships", "Retail Services", "Others"))

        if Niche == "Others":
            other_niche = st.text_input(
            "Enter Marketing Niche", "Example: Banking Services",)

        else:
            other_niche = None 

        st.markdown("""
            <h2 style='color: #FF6B6B; font-size: 18px'>Persona Demographics</h2>
            """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            position = st.text_input("Role/Position", "Example: Chief Technological Officer")
            age = st.slider('Age Range', 0, 100, (30, 40))
            
        with col2:   
            Industry = st.text_input("Industry", "Example: Marketing")
            Location = st.text_input("Location", "Example: USA")

        st.markdown(
            """
            <style>
            .st-bw {
            background-color: white;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("""
            <h2 style='color: #FF6B6B; font-size: 18px'>Persona Pain Point</h2>
            """, unsafe_allow_html=True)
        
        Persona_Pain = st.text_area("Input text", "Example: Navigating legacy system modernization amidst evolving technological landscapes.", key='text_area')

        st.markdown("""
            <h2 style='color: #FF6B6B; font-size: 18px'>Marketing Content</h2>
            """, unsafe_allow_html=True)
        
        content_check = st.text_area("Input Content", "Type or Paste Your Marketing Content Here")
        st.write("(Note: You can increase the height of the text area by dragging it through the bottom right corner of the box)")

        Persona = {"position": position, "Industry": Industry, "Location":Location, "age":age, "Persona_Pain": Persona_Pain}
        

        prompt_template = """
            As a {Niche} expert, perform a persona-based evaluation for this persona: {Persona}. 
            Evaluate the tone, language, cultural sensitivity, content clarity, and coherence to ensure it aligns 
            with the chosen persona preferences and norm. Then, provide a detailed and actionable feedback and 
            recommendations citing a spefic example from the content on how to better align the content to avoid a 
            potential pitfalls. Here is the content: {content_check}

            You just return helpful answer and nothing else

            Helpful Answer: 
            """
        prompt = PromptTemplate(template=prompt_template, input_variables=['Niche', 'Persona',  'content_check'])

        llm_chain = LLMChain(prompt=prompt, llm=llm)
        

        if st.button("Analyze"):
            try:
                with st.spinner("Making your content better! Wait for it..."):
                    improved_content = llm_chain.run({"content_check": content_check, "Niche": Niche, "Persona":Persona})
                st.title("Result")
                st.markdown(improved_content, unsafe_allow_html = True)
            except:
                st.error("Something is wrong")

    if page_selection == "User Guide":
        st.image('img/user guide.jpg', use_column_width=True)

        st.markdown("""

            <div style='color: #FF6B6B; font-size: 18px; margin-bottom: 20px'>
                <strong>Getting Started</strong><br>
                <span style='color: #2E3F4F;'>To begin using the app, select the <strong>Model Interface</strong> from the sidebar. This is where you'll input your persona details and marketing content for analysis.</span>
            </div>
                    
            <div style='color: #FF6B6B; font-size: 18px; margin-bottom: 20px'>
                <strong>Model Interface</strong><br>
                <span style='color: #2E3F4F;'>The Model Interface provides a simple form to enter your persona details such as Role/Position, Age range, Industry, Location, Pain Points, and Marketing Content.</span>
            </div>
                    
            <div style='color: #FF6B6B; font-size: 18px; margin-bottom: 20px'>
                <strong>Analyze</strong><br>
                <span style='color: #2E3F4F;'>Once you've filled in the necessary information, click the <strong>Analyze</strong> button to evaluate the alignment of your marketing content with the provided persona details.</span>
            </div>
                    
            <div style='color: #FF6B6B; font-size: 18px; margin-bottom: 20px'>
                <strong>Results</strong><br>
                <span style='color: #2E3F4F;'>The app will display the evaluated content, suggesting improvements if applicable.</span>
            </div>
                    
            <div style='color: #FF6B6B; font-size: 18px; margin-bottom: 20px'>
                <strong>Explore</strong><br>
                <span style='color: #2E3F4F;'>Feel free to navigate between different pages in the sidebar for more information about the solution and frequently asked questions.</span>
            </div>
                    
            For additional assistance, please reach out to our support team.
            """, unsafe_allow_html=True)

    if page_selection == "FAQs":
        st.image('img/FAQs.jpg', use_column_width=True)

        st.markdown("""
            <h2 style='color: #6AB187;'>Frequently Asked Questions</h2>

            <div style='color: #FF6B6B; margin-bottom: 20px;'>
                <strong>Q:</strong>
                <span style='color: #2E3F4F; font-weight:bold;'> Is the entered data stored?</span><br>
                <strong>A:</strong>
                <span style='color: #2E3F4F;'> No, the app doesn't store any entered data once the analysis is complete. Your information remains confidential and isn't used for any purposes beyond analysis.
            </div>

            <div style='color: #FF6B6B; margin-bottom: 20px;'>
                <strong>Q:</strong>
                <span style='color: #2E3F4F; font-weight:bold;'> Can I use my own language model?</span><br>
                <strong>A:</strong>
                <span style='color: #2E3F4F;'> Currently, the app supports the Llama 2 and OpenAI models. Custom model integrations might be available in the future updates.
            </div>

            <div style='color: #FF6B6B; margin-bottom: 20px;'>
                <strong>Q:</strong>
                <span style='color: #2E3F4F; font-weight:bold;'> What types of marketing content can be evaluated?</span><br>
                <strong>A:</strong>
                <span style='color: #2E3F4F;'> The app can analyze various types of marketing content, including but not limited to, advertisements, blog posts, social media content, and email campaigns.
            </div>

            <div style='color: #FF6B6B;'>
                <strong>Q:</strong>
                <span style='color: #2E3F4F; font-weight:bold;'>Can Contentify analyze video content?</span><br>
                <strong>A:</strong>
                <span style='color: #2E3F4F;'> Contentify primarily focuses on textual content analysis. While it doesn't directly analyze video content, it can process associated text data such as video captions, transcripts, or textual descriptions linked to the video, enabling insights into the textual aspects of video-based marketing content.
            </div>
        """, unsafe_allow_html=True)
        

    if page_selection == "Solution Overview":
        st.markdown("<h2 style='color: #FF6B6B; text-align: center;'>Solution Overview</h2>", unsafe_allow_html=True)
        
        st.image('img/Solution Overview.png', caption='Architectural Diagram', output_format='auto', use_column_width=True)

        st.markdown("<span style='color: #6AB187; font-weight: bold;'>Contentify</span> is an innovative platform designed to revolutionize content alignment for marketing teams. Leveraging a powerful large language model, Contentify empowers marketers to seamlessly assess, optimize, and tailor content to specific personas. By integrating robust accountability and visibility features, comprehensive prompt engineering, and rigorous testing, Contentify ensures precise content alignment, fostering enhanced brand perception, boosting audience engagement, and delivering measurable ROI.", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
