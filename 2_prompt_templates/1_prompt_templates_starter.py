from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

# template = "Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength. Keep it to 4 lines max."

# prompt_template = ChatPromptTemplate.from_template(template)
# prompt = prompt_template.invoke(
#     {
#         "tone": "energetic",
#         "company": "Samsung",
#         "position": "AI Engineer",
#         "skill": "AI",
#     }
# )

# result = llm.invoke(prompt)

# print(result.content)
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke(
    {
        "topic": "lawyers",
        "joke_count": 3,
    }
)
print("\n----- Prompt with System and Human Messages (Tuple) -----\n")
print(prompt)
