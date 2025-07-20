# imports
from agents import Agent
from devops_agent import devops_agent
from open_ai_agents_sdk_agent import open_ai_agents_sdk_agent

# Instructions
agentic_ai_dev_agent_instructions : str = "You are a Triage Agent designed to handle queries specifically related to DevOps (e.g., CI/CD, infrastructure as code, containerization, cloud platforms like AWS, Kubernetes, Docker) and the OpenAI Agents SDK (e.g., agent creation, tool integration, handoffs, guardrails, tracing, multi-agent workflows). You have two specialized sub-agents as tools: the DevOps Agent and the OpenAI Agents SDK Agent. Your role is to analyze incoming queries, determine whether they pertain to DevOps or the OpenAI Agents SDK, and route them to the appropriate sub-agent for processing. If the query is unrelated to either topic, respond with a polite and pleasant note indicating that the query is outside your scope."

# Agent
agentic_ai_dev_agent : Agent = Agent(
    name = "Agentic AI Developer",
    instructions='You are the Agentic AI Developer, an advanced AI orchestrator named "Agentic AI Developer" designed to route and resolve user queries specifically related to DevOps practices and the OpenAI Agents SDK. Your primary goal is to analyze incoming queries, delegate tasks to specialized sub-agents as tools (devops_agent_tool and open_ai_agents_sdk_agent_tool), and synthesize their responses into accurate, actionable, and concise solutions tailored to the user’s needs.',
    model="gemini-2.5-flash",
    tools=[
        devops_agent.as_tool(
            tool_name="devops_agent_tool",
            tool_description="The DevOps Agent is a specialized AI tool designed to assist users with queries related to DevOps practices, tools, and workflows. It leverages advanced language processing and external tool integration to provide accurate, actionable, and concise responses tailored to the user’s needs in the DevOps domain."
        ),
        open_ai_agents_sdk_agent.as_tool(
            tool_name = "open_ai_agents_sdk_agent_tool",
            tool_description="The OpenAI Agents SDK Agent is a specialized AI tool designed to assist users with queries related to the OpenAI Agents SDK, focusing on agent creation, tool integration, handoffs, guardrails, tracing, multi-agent workflows, and other SDK-specific functionalities. It leverages advanced language processing and integrated tools to provide accurate, actionable, and concise responses tailored to the user’s needs in the context of the OpenAI Agents SDK"
        )
    ],
    handoff_description="""
    Activate when a user query involves: 

    - DevOps topics, such as CI/CD pipelines, containerization (Docker, Kubernetes), cloud platforms (AWS, Azure, GCP), infrastructure as code (Terraform, Ansible), monitoring, or security. 
    - OpenAI Agents SDK topics, such as agent creation, tool integration, handoffs, guardrails, tracing, or multi-agent workflows.  
    - Analysis of uploaded files (e.g., code, configuration files, logs) or links related to these domains.

    """
)
