# Imports
from agents import (
    Runner, 
    set_default_openai_client, 
    set_default_openai_api,
    set_tracing_disabled,
    RunResultStreaming
)
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
from triage_agent import triage_agent
import chainlit as cl
from openai.types.responses import ResponseTextDeltaEvent

# Loading Environment Variable
load_dotenv()

# Setting Default Open AI Client
set_default_openai_client(
    client=AsyncOpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=os.getenv("GEMINI_API_KEY")
    ),
    use_for_tracing=False
)

# Setting Default API Type
set_default_openai_api(
    api="chat_completions"
)

# Setting Tracing Disabled
set_tracing_disabled(
    disabled=True
)

# Chat Start 
@cl.on_chat_start
async def start_chat():
    cl.user_session.set("chat_history",[])
    msg : cl.Message = cl.Message(content="")
    for _ in " Welcome to Agentic Developers Chatbot! I'm here to supercharge your web, mobile, and agentic AI development.":
        await msg.stream_token(_)


# Message Sent
@cl.on_message
async def handle_message(message:cl.Message):

    chat_history = cl.user_session.get("chat_history")
    chat_history.append(
        {
            "role":"user",
            "content":message.content
        }
    )

    result : RunResultStreaming = Runner.run_streamed(
        starting_agent=triage_agent,
        input = chat_history
    )

    msg : cl.Message = cl.Message(content="")
    await msg.stream_token(f"Working On Query...\n")

    async for event in result.stream_events():
        if(
            event.type == "raw_response_event"
            and hasattr(event.data, "delta")
            and isinstance(event.data, ResponseTextDeltaEvent)
        ):
            # Response Sending
            await msg.stream_token(event.data.delta)
    await msg.stream_token(f"\nAgent Used: {result.last_agent.name}")

    chat_history.append(
        {
            "role":"assistant",
            "content":msg.content
        }
    )

    cl.user_session.set("chat_history",chat_history)
