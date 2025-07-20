# imports
from agents import Agent
from web_dev_agent import web_dev_agent
from mobile_app_dev_agent import mobile_app_dev_agent
from agentic_ai_dev import agentic_ai_dev_agent

# Instructions
triage_agent_instructions : str = 'You are the Triage Agent, an advanced AI orchestrator named "Triage Agent" designed to analyze and route user queries to specialized sub-agents based on their domain expertise. Your primary goal is to determine the appropriate sub-agent—Web Development Agent, Mobile App Development Agent, or Agentic AI Developer Agent (for DevOps and OpenAI Agents SDK)—and delegate queries to ensure accurate, actionable, and context-aware solutions.'

# Agent
triage_agent : Agent = Agent(
    name="Triage Agent",
    instructions=triage_agent_instructions,
    model="gemini-2.5-flash",
    handoffs=[web_dev_agent,mobile_app_dev_agent,agentic_ai_dev_agent]
)
