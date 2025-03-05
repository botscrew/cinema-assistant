import json

from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageToolCall
from openai.types.chat.chat_completion_message_tool_call import Function

from config import OPENAI_API_KEY
from constants import PROMPT
from supabaseClient import get_movies, get_sessions
from tools import GET_MOVIES_TOOL, GET_MOVIE_SESSIONS_TOOL

client = OpenAI(
    api_key=OPENAI_API_KEY,  # This is the default and can be omitted
)

def completion(messages):
    return client.chat.completions.create(
        messages=messages,
        model="gpt-4o",
        tools=[GET_MOVIES_TOOL, GET_MOVIE_SESSIONS_TOOL]
    )


def initMessages():
    return [
        {
            "role":"developer",
            "content": PROMPT
        }]

def appendMessage(messages, content, role):
    messages.append({
        "role": role,
        "content": content
    })

def appendUserMessage(messages, content):
    appendMessage(messages, content, "user")

def appendAssistantMessage(messages, content):
    appendMessage(messages, content, "assistant")

def appendToolCallResultMessage(messages, content, tool_call_id):
    messages.append({
        "role": 'tool',
        "content": content,
        "tool_call_id": tool_call_id
    })
def appendToolCall(messages, tool_call_message):
    messages.append(tool_call_message)


def isToolCall(completion:ChatCompletion):
    if completion.choices[0].message.tool_calls:
        return True
    return False

def get_tool_details(completion:ChatCompletion)->Function:
    return completion.choices[0].message.tool_calls[0].function

def execute_tool(messages, tool_details:Function, tool_call_id):
    function_name = tool_details.name
    arguments = json.loads( tool_details.arguments)
    if function_name == "get_movies":
        result = get_movies()
    elif function_name == "get_movie_sessions":
        result = get_sessions(arguments['selected_movie_id'])
    else:
        result = "Unknown function"
    appendToolCallResultMessage(messages, str(result), tool_call_id)
    processCompletion(messages, completion(messages))


def processCompletion(messages, completion:ChatCompletion):
    if (isToolCall(completion)):
        appendToolCall(messages, completion.choices[0].message)
        execute_tool(messages, get_tool_details(completion), completion.choices[0].message.tool_calls[0].id)
    else:
        assistant_response = completion.choices[0].message.content
        appendAssistantMessage(messages, assistant_response)
        print(assistant_response)



