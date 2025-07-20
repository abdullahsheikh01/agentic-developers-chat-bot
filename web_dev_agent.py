# imports 
from agents import Agent
import chainlit

# Instructions
web_dev_agent_instructions : str = "You are a Web Development Master Agent, an expert AI assistant specializing in all aspects of web development, including front-end, back-end, full-stack development, and related technologies. Your primary goal is to assist users in designing, building, debugging, and optimizing web applications with precise, practical, and up-to-date solutions."

# Agent
web_dev_agent : Agent = Agent(
    name = "Web Development Agent",
    instructions = web_dev_agent_instructions,
    model="gemini-2.5-flash",
    handoff_description="Activate when a user query involves web development topics, such as coding (HTML, CSS, JavaScript, etc.), frameworks (React, Angular, Node.js, etc.), databases, APIs, or web performance, or when a user uploads relevant files (e.g., code, wireframes) requiring analysis or implementation.  "
)


print(type(chainlit.Message.content))