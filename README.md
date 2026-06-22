# Nova - 本地AI代理系统

Nova是一个完整的本地AI代理系统，包含三个独立子项目，可独立开发、测试和部署。

## 项目结构

```
Nova/
├── mcp-server/          # MCP工具服务器
├── agent-system/        # AI代理系统
├── local-llm/           # 本地模型服务
└── plan/                # 项目计划
```

## 子项目说明

### 1. mcp-server
MCP (Model Context Protocol) 工具服务器，提供各种实用工具。

**功能：**
- 文件操作工具
- 数据处理工具
- 网络工具
- 系统工具

**技术栈：** Python + MCP SDK + FastAPI

### 2. agent-system
AI代理系统，连接MCP服务器和本地模型，提供智能对话能力。

**功能：**
- 任务规划与执行
- 工具调用管理
- 多轮对话
- Web界面

**技术栈：** Python + FastAPI + React/Vue.js

### 3. local-llm
本地大语言模型服务，提供API接口供代理系统调用。

**功能：**
- 模型部署与管理
- OpenAI兼容API
- 流式响应
- 性能监控

**技术栈：** vLLM + Qwen3-0.6B

## 系统架构

```
用户 → agent-system → mcp-server
              ↓
         local-llm
```

## 快速开始

### 1. 启动 local-llm
```bash
cd local-llm
# 安装vLLM
pip install vllm
# 启动服务
python -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen3-0.6B \
    --port 8000
```

### 2. 启动 mcp-server
```bash
cd mcp-server
conda activate mcp-server
pip install -r requirements.txt
python server.py
```

### 3. 启动 agent-system
```bash
cd agent-system
pip install -r requirements.txt
python main.py
```

## 技术栈

- **后端：** Python, FastAPI
- **前端：** React/Vue.js
- **数据库：** SQLite (开发阶段)
- **模型：** Qwen3-0.6B
- **推理框架：** vLLM
- **协议：** MCP (Model Context Protocol)

## 开发指南

每个子项目都是独立的，可以：
1. 独立开发和测试
2. 独立部署
3. 有自己的依赖和环境

详细文档请查看各子项目的 `docs/` 目录。

## 计划

项目计划详见 [plan/PLAN.md](plan/PLAN.md)

## 许可证

MIT License
