from fastmcp import FastMCP
from config import load_config


config = load_config()
mcp = FastMCP(config.server.name)

if __name__ == "__main__":
    mcp.run(transport="http", 
            host=config.server.host,
            port=config.server.port,
            stateless_http=True)
