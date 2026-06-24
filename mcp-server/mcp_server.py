from fastmcp import FastMCP
from config import load_config

config = load_config()
mcp = FastMCP(config.server.name)
