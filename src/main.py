from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from dotenv import load_dotenv
from prompt import system_prompt    
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
)

server_params = StdioServerParameters(
    command="python",
    args=[r".\src\server.py"],
)

import asyncio

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent(model, tools, prompt=system_prompt) 
            query =input("Enter your question: ")
            inputs= {"messages": [("user", query)]}
            # Run the agent with the provided inputs
            response = await agent.ainvoke(inputs)
            final_answer = response['messages'][-1].content  
            print(final_answer)

# Run the main async function
asyncio.run(main())
