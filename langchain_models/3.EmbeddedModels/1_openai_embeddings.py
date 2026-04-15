from langchain_openai import embeddings
from dotenv import load_dotenv

load_dotenv()
model = embeddings.OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)