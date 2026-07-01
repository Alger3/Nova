import os
import platform
from mcp_server import mcp


@mcp.tool(
    name="get_env",
    description="获取当前mcp的环境变量",
)
async def get_env(key: str) -> str:
    """获取当前mcp的环境变量"""
    return os.environ.get(key, "")


@mcp.tool(
    name="get_system_info",
    description="获取mcp的系统信息",
)
async def get_system_info() -> dict:
    """获取mcp的系统信息"""
    return {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }
