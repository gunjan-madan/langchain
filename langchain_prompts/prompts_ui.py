from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatOpenAI()

st.header('CBSE Worksheet Generator')

grade_input = st.selectbox("Select Grade", ["6", "7", "8", "9", "10", "11", "12"])
subject_input = st.selectbox("Select Subject", ["Mathematics", "Science", "English", "Social Studies", "Hindi", "History", "Geography"])
topic_input = st.text_input("Enter Chapter/Topic Name")
difficulty_input = st.selectbox("Select Difficulty Level", ["Easy", "Medium", "Hard", "Mixed"])
num_questions_input = st.number_input("Number of Questions", min_value=5, max_value=50, value=15)
objective_input = st.text_area("Learning Objective (Optional)")

template = load_prompt('template.json')


if st.button('Generate Worksheet'):
    chain = template | model
    result = chain.invoke({
        'GRADE': grade_input,
        'SUBJECT': subject_input,
        'TOPIC': topic_input,
        'DIFFICULTY': difficulty_input,
        'NUMBER_OF_QUESTIONS': str(num_questions_input),
        'OBJECTIVE': objective_input
    })
    st.write(result.content)