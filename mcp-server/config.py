import yaml
from pydantic import BaseModel
from pathlib import Path


class ServerConfig(BaseModel):
    name: str = "nova-mcp-server"
    host: str = "0.0.0.0"
    port: int = 8080


class ToolsConfig(BaseModel):
    enabled: list[str] = ["file_tools", "data_tools", "network_tools", "system_tools"]


class LoggingConfig(BaseModel):
    level: str = "INFO"


class Config(BaseModel):
    server: ServerConfig = ServerConfig()
    tools: ToolsConfig = ToolsConfig()
    logging: LoggingConfig = LoggingConfig()


def load_config(path: str = "configs.yaml") -> Config:
    config_path = Path(path)
    if config_path.exists():
        with open(config_path) as f:
            return Config(**yaml.safe_load(f))
    return Config()
