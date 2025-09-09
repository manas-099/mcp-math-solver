
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import asyncio
import getpass
import os
load_dotenv()


os.environ["GOOGLE_API_KEY"]=os.getenv('GOOGLE_API_KEY')

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

async def main():
    client=MultiServerMCPClient(
        {
            "MathServer":{
                "command":"python",
                "args":["MathServer.py"],
                "transport":"stdio"
            }
        }
    )
    tools=await client.get_tools()
    
    
    llm=ChatGoogleGenerativeAI(
        model="gemini-1.5-flash"
    )
    agent=create_react_agent(
        llm,tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is 20 + 100 -10?"}]}
    )
    print(math_response)

    print("Math response:", math_response['messages'][-1].content)

if __name__=="__main__":
    asyncio.run(main())