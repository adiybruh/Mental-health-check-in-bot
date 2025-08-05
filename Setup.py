from langchain_google_genai import ChatGoogleGenerativeAl

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import Pydantic OutputParser from tools import tools

from schema import MoodResponse

Ilm ChatGoogleGenerativeAl (model="gemini-2.5-flash", temperature=0.3) parser = Pydantic OutputParser (pydantic_object=MoodResponse)

prompt ChatPromptTemplate.from_messages([ ("system", """

You are a caring mental health check-in assistant.

Your responsibilities:

1. Ask how the user is feeling.

2. Acknowledge with empathy and encouragement.

3. Call the tool suggest_activity with the user's mood.

4. Call log_mood_entry to save what the user shared.

5. Respond only with JSON:

- mood_summary
- suggestion
- log_status

(format instructions)

("placeholder", "(chat_history)"),

("human", "{query}"),

("placeholder", "(agent_scratchpad}")

]).partial(format_instructions=parser.get_format_instructions())
