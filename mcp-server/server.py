from fastmcp import FastMCP
from config import load_config
from tools import file_mcp, data_mcp, network_mcp, system_mcp


config = load_config()
mcp = FastMCP(config.server.name)

mcp.mount(file_mcp)
mcp.mount(data_mcp)
mcp.mount(network_mcp)
mcp.mount(system_mcp)

if __name__ == "__main__":
    mcp.run(transport="http", 
            host=config.server.host,
            port=config.server.port,
            stateless_http=True)
