from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

embedding_model = MistralAIEmbeddings(
    model="mistral-embed"
)

vectorstore = Chroma(
    persist_directory= "chroma-db",
    embedding_function = embedding_model
)

retriever = vectorstore.as_retriever(
    search_type = "mmr",
    search_kwargs = {
        "k" : 4,
        "fetch_k" : 10,
        "lambda_mult" : 0.5
    }
)

llm = ChatMistralAI(model= "mistral-small-2506")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI Assistant. Use only  provided context to answer the question. If the answer is not present in the conntext, say: I could not find the answer in the document."),
        ("human", "Context: {context}  Question: {question}")
    ]
)

print("Rag system created")
print("press 0 to exit")

def ask_question(query):

    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    final_prompt = prompt.invoke(
        {
            "context": context,
            "question": query
        }
    )

    response = llm.invoke(final_prompt)

    return response.content