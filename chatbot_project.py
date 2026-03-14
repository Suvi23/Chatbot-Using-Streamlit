#This is a chatbot project created using python and Streamlit. I have used Gemini Flash 1.5 pro model. The chatbot responds to dynamic user questions and answers them in concise and crisp manner. 
#gemini_chatbot.py


import google.generativeai as genai
import requests  # Gemini API will be accessed via HTTP requests
import streamlit as st

##added by me delete in case of problem below this line
import google.generativeai as genai
from google.generativeai.types import ContentType
from PIL import Image


#####


GOOGLE_API_KEY = 'AIzaSyClvG5P7RVSbLQH30s2pWFj9OHehjK8rxw'
genai.configure(api_key=GOOGLE_API_KEY)

#for listing alll the available free models of google
#for m in genai.list_models():
    #if 'generateContent' in m.supported_generation_methods:
        #print(m.name)


model = genai.GenerativeModel('gemini-1.5-pro-latest')





# Base URL for the Gemini API
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyClvG5P7RVSbLQH30s2pWFj9OHehjK8rxw"
if GOOGLE_API_KEY is None:
    raise ValueError("API key is not set in the environment variables.")



# Chat with Gemini API

# Define conversation function
# Predefined FAQ dictionary

# Check if user question is an FAQ
st.set_page_config(
    page_title="Chatbot",
    page_icon="D:\GEMINI_CHATBOT\images\icon1.png",  # Replace with your icon URL or use a local path
    )
st.markdown(
    """
    <style>
    .main{
       background-color: #ffdd6a;
       border-radius:10px;
       padding:20px;
    }
    .chat-icon{
        display:block;
        margin:0 auto;
        width:100px;
        margin-bottom:20px;
    }
    .message{
        display:flex;
        align-item:center;
        margin-bottom:10px;
        }
    .user{
       justify-content:flex-end;
    }
    .bot{
       justify-content:flex-start;
    }
    .message p{
        border-radius:5px;
        padding:10px;
        margin:0;
    }
    .user p {
      background-color: yellow;
      color:black;
    }

    .bot p{
     background-color: #edcbff;
      color:black;
    }

    </style>
""",
unsafe_allow_html=True)

# Build the Streamlit GUI
def main():
    
    #st.title("CyberTron AI Chatbot")
    st.markdown("<h1 style='color:blue;'>Cybertron AI CHATBOT</h1>",unsafe_allow_html=True)
    st.subheader("Ask any question and get instant answers from the AI-powered chatbot.")
    
    # Initialize a session state to store the conversation history
    if 'messages' not in st.session_state:
       st.session_state.messages = []

    #st.markdown("<img class='chat-icon' src='icon1.png' alt='Chat Icon'>",unsafe_allow_html=True)
    #st.markdown("<img class='chat-icon' src='chatbot_icon1.png' alt='Chatbot Icon'>",unsafe_allow_html=True)
    #st.markdown("<img class='chat-icon' src='user_icon.png' alt='User Icon'>",unsafe_allow_html=True)
    st.markdown("<p style='color:Red;'>Type your Question Below</p>",unsafe_allow_html=True)
    
    #create a place holder for messages
    msg_placeholder=st.empty()

    # Create a text input for the user
    
    user_input = st.text_input( "You: ", "")
    
    if st.button("Send"):
          

        if user_input:
            response = model.generate_content(user_input)
            

            if response.candidates:
                    first_candidate = response.candidates[0]  # Access the first candidate
                    if first_candidate.content.parts:
                        first_part = first_candidate.content.parts[0]  # Access the first part
                        text = first_part.text  # Extract the text

                        st.text_area("Bot:", value=text, height=200, max_chars=None)
                    else:
                        text = "No content found in parts."
            else:
                text = "No candidates found in the response."
        else:
         text="Please Enter The Question!!!! :("
         st.text_area("Bot:", value=text, height=200, max_chars=None)
            
   
        

if __name__ == "__main__":
    main()
