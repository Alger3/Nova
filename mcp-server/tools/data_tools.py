import json
import yaml
from fastmcp import FastMCP

mcp = FastMCP("data-tools")


@mcp.tool()
async def parse_json(text: str) -> dict:
    """解析JSON字符串"""
    return json.loads(text)


@mcp.tool()
async def parse_yaml(text: str) -> dict:
    """解析YAML字符串"""
    return yaml.safe_load(text)


@mcp.tool()
async def to_json(data: dict, indent: int = 2) -> str:
    """转换为JSON字符串"""
    return json.dumps(data, indent=indent, ensure_ascii=False)
