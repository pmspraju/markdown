import gradio as gr
import os

from smolagents import InferenceClientModel, CodeAgent, MCPClient

# from sseclient import SSEClient

# messages = SSEClient("https://pmspraju-mcp-sentiment.hf.space/proxy/mcp/sse")
# for msg in messages:
#     print(msg.data)

import requests
urls = [
    "https://pmspraju-mcp-sentiment.hf.space/proxy/mcp/sse",
    "https://pmspraju-mcp-sentiment.hf.space/mcp/sse",
    "https://pmspraju-mcp-sentiment.hf.space/gradio_api/mcp/sse"
]

for url in urls:
    try:
        r = requests.get(url, timeout=10)
        print(f"{url} → {r.status_code}")
    except Exception as e:
        print(f"{url} → Failed: {e}")

#https://pmspraju-mcp-sentiment.hf.space/proxy/mcp/sse → 200
#https://pmspraju-mcp-sentiment.hf.space/mcp/sse → 200
#https://pmspraju-mcp-sentiment.hf.space/gradio_api/mcp/sse → Failed: HTTPSConnectionPool(host='pmspraju-mcp-sentiment.hf.space', port=443): Read timed out.

# with MCPClient(
#     {"url": "https://pmspraju-mcp-sentiment.hf.space/proxy/mcp/sse"}
# ) as tools:
#     # Tools from the remote server are available
#     print("\n".join(f"{t.name}: {t.description}" for t in tools))

# mcp_client = MCPClient(
#         {"url": "https://pmspraju-mcp-sentiment.hf.space/gradio_api/mcp/sse"}
#     )

# try:
    
#     tools = mcp_client.get_tools()

#     model = InferenceClientModel(token=os.getenv("HF_TOKEN"))
#     agent = CodeAgent(tools=[*tools], model=model, additional_authorized_imports=["json", "ast", "urllib", "base64"])

#     demo = gr.ChatInterface(
#         fn=lambda message, history: str(agent.run(message)),
#         type="messages",
#         examples=["Watching this movies was good"],
#         title="Agent with MCP Tools",
#         description="This is a simple agent that uses MCP tools to answer questions."
#     )

#     # demo = gr.ChatInterface(
#     #     fn=lambda message, history: str(agent.run(message)),
#     #     type="messages",
#     #     examples=["Analyze the sentiment of the following text 'This is awesome'"],
#     #     title="Agent with MCP Tools",
#     #     description="This is a simple agent that uses MCP tools to answer questions.",
#     # )

#     demo.launch()
# finally:
#     mcp_client.disconnect()