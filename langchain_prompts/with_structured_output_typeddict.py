from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, List

load_dotenv()

model = ChatOpenAI()

class StudentDetails(TypedDict):
    name: str
    school: str
    grade: str
    hobbies: List[str]


structured_model = model.with_structured_output(StudentDetails)

result = structured_model.invoke("""My name is Ananya Gupta. I am a student of Grade 7 at Sunrise International School. My hobbies include dancing and painting. I like participating in school competitions and learning new things.""")

print(result)