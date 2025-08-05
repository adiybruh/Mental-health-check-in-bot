from dotenv import load_dotenv; load_dotenv()

from langchain_core.messages import Human Message, AIMessage

from langchain.agents import create_tool_calling_agent, AgentExecutor

from tools import tools

from schema import MoodResponse

from prompt import prompt, parser, Ilm # if separated

agent = create_tool_calling_agent(Ilm=lim, prompt=prompt, tools=tools)

executor AgentExecutor (agent agent, tools-tools, verbose=True)

chat_history=[]

print(" Welcome to the Mental Health Check-in Bot (type 'exit' to quit)")

while True:

q = input("\nYou: ")

if q.lower() == "exit": 
break
chat_history.append(HumanMessage(content=q))

response = executor.invoke({"query": q, "chat_history": chat_history})

try:

output = parser.parse(response["output"])

print("\n How You're Feeling:", output.mood_summary)

print(" Suggested Activity:", output.suggestion)

print(" Log:", output.log_status)

chat_history.append(AIMessage(content=output.mood_summary))

except Exception as e:

print(" Could not parse response:", e)

print("Raw output:", response.get("output"))
