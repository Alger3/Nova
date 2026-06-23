import os
import platform
from fastmcp import FastMCP

mcp = FastMCP("system-tools")


@mcp.tool()
async def get_env(key: str) -> str:
    """获取环境变量"""
    return os.environ.get(key, "")


@mcp.tool()
async def get_system_info() -> dict:
    """获取系统信息"""
    return {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }
