import importlib
import pkgutil
from mcp_server import mcp, config
import tools

for _, module_name, _ in pkgutil.iter_modules(tools.__path__):
    importlib.import_module(f"tools.{module_name}")


if __name__ == "__main__":
    mcp.run(transport="http", 
            host=config.server.host,
            port=config.server.port,
            stateless_http=True)
