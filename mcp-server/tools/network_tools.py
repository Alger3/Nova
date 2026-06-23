import httpx
from fastmcp import FastMCP

mcp = FastMCP("network-tools")


@mcp.tool()
async def http_get(url: str) -> str:
    """发送HTTP GET请求"""
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text


@mcp.tool()
async def http_post(url: str, data: dict) -> str:
    """发送HTTP POST请求"""
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
        return response.text
