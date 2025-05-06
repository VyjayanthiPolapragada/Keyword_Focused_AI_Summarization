from langchain.agents import initialize_agent, Tool, AgentType
from langchain.llms import OpenAI
from backend.llm_summary import summarize_text
from backend.keyword import extract_keywords_from_text

# Define tools
def summarize_tool(text):
    return summarize_text(text)

def extract_keywords_tool(text, keyword):
    return extract_keywords_from_text(text, keyword)

tools = [
    Tool(
        name="Summarize Text",
        func=summarize_tool,
        description="Summarizes the provided text."
    ),
    Tool(
        name="Extract Keywords",
        func=extract_keywords_tool,
        description="Extracts keywords from the provided text."
    ),
]

# Initialize agent
llm = OpenAI(temperature=0)
agent = initialize_agent(tools, llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

def agentic_decision_maker(text, action="summarize", keyword=None):
    if action == "summarize":
        return agent.run(f"Summarize the following text: {text}")
    elif action == "extract":
        return agent.run(f"Extract key information from the following text: {text}")
    else:
        return "Invalid action."
