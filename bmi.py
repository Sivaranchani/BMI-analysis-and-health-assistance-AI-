import streamlit as st
import google.generativeai as genai 
import os 
import pandas as pd 
from dotenv import load_dotenv 
load_dotenv() 
# configure the google generative ai api key
key_variable = os.getenv("GOOGLE_API_key") 
genai.configure(api_key=key_variable)
#set up page
st.title("Health Assistant AI 🚀")
st.header("this page will help you with your health and fitness journey📝")
st.subheader("Streamlit is working...__")

st.sidebar.title("BMI Calculator")
st.sidebar.subheader("height")
height = st.sidebar.text_input('Enter your height in meters :')

st.sidebar.subheader("weight")
weight = st.sidebar.text_input('Enter your weight in kgs :')
try:
    height = pd.to_numeric(height)
    weight = pd.to_numeric(weight) 
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.sidebar.success(f"Your BMI is: {bmi:.2f}")
    else:
        st.sidebar.write('Please enter valid positive numbers for height and weight.')
except :
    st.sidebar.info("Please enter positive values for height and weight.")
input = st.text_input('Ask me your question !')
submit = st.button('click here')
model = genai.GenerativeModel("gemini-1.5-flash")
def generate_result(bmi,input):
    if input is not None:
        
        prompt = f''' act as an health assisatant and fitness mentor here and give me a detailed answer to my question suggest
        me indepth diet and lifestyle and exercise using {bmi} if any medications or medicine related question are asked always mention that
        'check with your medical advisor' disclamier should be displayed '''
         
        result = model.generate_content(input+prompt)
    return result.text 
if submit:
   with st.spinner('Generating response...'):
       response = generate_result(bmi,input)
       st.markdown(':green[Result]')
       st.write(response)