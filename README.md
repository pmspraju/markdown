## markdown
try MCP to connect to git

## Hugging face space 

1. Create a new Space on Hugging Face:
   - Go to huggingface.co/spaces
   - Click "Create new Space"
   - Choose "Gradio" as the SDK
   - Name your space (e.g., "mcp-sentiment")

2. Cone the hf space repository using 
```
git clone https://huggingface.co/spaces/pmspraju/mcp-sentiment
```

3. Hugging face spaces needs an app.py file to build the space. So the name of the python file has to be app.py  

4. Create a `requirements.txt` file:
```txt
gradio[mcp]
textblob
```

5. Files can be commited to hf spac repo using
    - https - While commiting, when prompted, use huggingface key with write access.
    - ssh   - Create keys and add it to hf profile.

6. SSH steps - In our local terminal
    - Create a ssh key
        - Enter file in which to save the key (/home/madhu/.ssh/id_ed25519):
        - If you just hit Enter, it defaults to ~/.ssh/id_ed25519. But you can override that and save it anywhere—like:
            ```
            ssh-keygen -t ed25519 -C "hugging face email@example.com"
            ```
    - setup ssh key path. You're explicitly telling the agent: “Here’s the path to my private key.” If you saved it elsewhere, you'd need to use that custom path instead
        ```
        ssh-add ~/.ssh/id_ed25519
        ```
    - Copy the created ssh key and add to the huggingface profile under settings/SSH and GPG keys

7. Commit the local code to the hf space repo
    - Check the remote urls. Set https or ssh accordingly.
        ```
        git remote -v
        origin  https://huggingface.co/spaces/pmspraju/mcp-sentiment.git (fetch)
        origin  https://huggingface.co/spaces/pmspraju/mcp-sentiment.git (push)
        ```
    - If https and need to set to ssh, then,
        ```
        git remote set-url origin git@hf.co:spaces/pmspraju/mcp-sentiment
        git remote -v
        origin  git@hf.co:spaces/pmspraju/mcp-sentiment (fetch)
        origin  git@hf.co:spaces/pmspraju/mcp-sentiment (push)
        ```
8. Push your code to the Space:
```bash
git init
git add app.py requirements.txt
git commit -m "Initial commit"
git remote add origin https://huggingface.co/spaces/pmspraju/mcp-sentiment
git push -u origin main
```

9. Your MCP server will now be available at:
```
https://YOUR_USERNAME-mcp-sentiment.hf.space/gradio_api/mcp/sse
https://pmspraju-mcp-sentiment.hf.space/gradio_api/mcp/sse
```

## MCP Server url 
---
### 🧭 MCP Endpoint Comparison Table

| **Server Type**         | **Tool Hosting Method**                          | **Typical Endpoint**                            | **When to Use**                                                                 |
|-------------------------|--------------------------------------------------|--------------------------------------------------|----------------------------------------------------------------------------------|
| **Gradio (native MCP)** | `demo.launch(mcp_server=True)`                  | `/proxy/mcp/sse` *(on HF Spaces)*               | ✅ Use when deploying a Gradio app with built-in MCP on Hugging Face Spaces     |
|                         |                                                  | `/mcp/sse` *(sometimes exposed directly)*        | ✅ Use if Space exposes MCP directly without proxy routing                      |
|                         |                                                  | `/gradio_api/mcp/sse` *(rare)*                  | ❌ Avoid unless explicitly configured—often leads to timeouts                   |
| **smoltools.mcp**       | `MCPServer(...).serve()`                        | `/gradio_api/mcp/sse` *(default)*               | ✅ Use when using `smoltools.mcp.MCPServer` locally or on Spaces               |
|                         |                                                  | `/proxy/mcp/sse` *(on HF Spaces)*               | ✅ Use if deploying smoltools-based server on Hugging Face Spaces              |
| **Claude Code Pro / Gemini CLI** | CLI-based tool registration via MCP config | Local subprocess or CLI invocation              | ✅ Use when invoking tools locally via CLI or subprocess (not via SSE)         |
| **Local Dev (custom)**  | Custom FastAPI/Flask MCP server                 | `http://localhost:8000/mcp/sse`                 | ✅ Use for local testing or custom tool orchestration                          |

---

### 🧠 Quick Rules of Thumb

- ✅ **Use `/proxy/mcp/sse`** for Gradio-based Hugging Face Spaces with `mcp_server=True`
- ✅ **Use `/gradio_api/mcp/sse`** only if you're using `smoltools.mcp.MCPServer` and it's configured to expose that path
- ❌ **Avoid guessing endpoints**—test with `curl` or `requests.get()` to confirm they respond with `200 OK`
- ✅ **Use `MCPClient.from_space("user/space")`** when possible—it auto-resolves the correct endpoint

---