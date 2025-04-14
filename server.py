# server.py
from mcp.server.fastmcp import FastMCP
from duckduckgo_search import DDGS

mcp = FastMCP("DDG")

@mcp.tool()
def search(query: str) -> str:
    """Searches the web using DuckDuckGo"""
    with DDGS() as ddgs:
        results = ddgs.text(query)
        if results:
            return "\n\n".join([r["body"] for r in results[:3]])
        return "No results found."

if __name__ == "__main__":
    mcp.run()
