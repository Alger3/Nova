from pathlib import Path
from mcp_server import mcp


@mcp.tool()
async def read_file(path: str) -> str:
    """读取文件内容"""
    return Path(path).read_text(encoding="utf-8")


@mcp.tool()
async def write_file(path: str, content: str) -> str:
    """写入文件内容"""
    Path(path).write_text(content, encoding="utf-8")
    return f"已写入: {path}"


@mcp.tool()
async def list_directory(path: str = ".") -> list[str]:
    """列出目录内容"""
    return [item.name for item in Path(path).iterdir()]
