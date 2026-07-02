# agent_backend_template

# 项目定位

#

# 这是 AI Agent 智能体就业导向学习计划第一阶段的工程模板项目。

#

# 第一阶段目标不是直接开发 Agent，而是先补齐后续 RAG、Function Calling、LangGraph、多智能体系统所需的工程基础。

#

# 第一阶段目标

# 搭建 FastAPI 后端工程结构

# 实现文件上传接口

# 接入 SQLite / PostgreSQL 数据库

# 实现 Vue3 前端上传页面

# 使用 Docker Compose 一键启动后端、前端和数据库

# 形成可用于后续 Agent 项目的基础工程模板

# 当前进度

#

# 创建项目仓库

#

# 创建 backend / frontend / docs 目录

#

# 创建 Python 虚拟环境

#

# 初始化 Git

#

# 定义 User / Document / Task 三个基础业务对象

#

# 学习 Python 函数、类、类型注解和 dataclass

#

# 完成 config.py 配置管理模块

#

# 完成 logger.py 日志模块

#

# 完成 exceptions.py 项目异常模块

#

# 完成 main.py 文件校验演示流程

#

# FastAPI 后端最小服务

#

# 文件上传接口

#

# 数据库 CRUD

#

# Vue3 前端页面

#

# Docker Compose 一键启动

#

# 项目结构

# agent_backend_template/

# ├── backend/

# │ └── app/

# │ ├── \_\_init\_\_.py

# │ ├── models.py

# │ ├── config.py

# │ ├── logger.py

# │ ├── exceptions.py

# │ └── main.py

# ├── frontend/

# ├── docs/

# │ ├── day01_log.md

# │ ├── day02_log.md

# │ └── day03_log.md

# ├── README.md

# ├── .gitignore

# └── requirements.txt

# 基础业务对象

#

# 当前项目定义了三个基础业务对象：

#

# User：表示系统用户

# Document：表示用户上传的文档

# Task：表示基于文档创建的处理任务

#

# 这三个对象后续会逐步迁移为 Pydantic Schema 和 SQLAlchemy ORM Model，用于 FastAPI 接口校验和数据库表设计。

#

# 工程基础模块

#

# 当前已完成：

#

# config.py：集中管理项目配置和环境变量

# logger.py：统一日志格式，支持控制台和文件日志

# exceptions.py：定义项目级业务异常

# main.py：模拟文件校验流程，验证配置、日志和异常处理

#

# 这些模块是后续 FastAPI 文件上传、RAG 检索、Agent 工具调用的基础。

#

# 当前可运行命令

#

# 在项目根目录运行：

#

# python backend\\app\\models.py

#

# 用于检查 User、Document、Task 三个基础对象是否能正常创建。

#

# python backend\\app\\config.py

#

# 用于检查项目配置是否能正常读取，并自动创建 data/uploads 目录。

#

# python backend\\app\\logger.py

#

# 用于检查日志模块是否能正常输出日志，并生成 logs/app.log。

#

# python backend\\app\\main.py

#

# 用于模拟文件校验流程，检查合法文件、非法文件类型、文件过大等情况是否能被正确处理。

#

# 已实现的文件校验逻辑

#

# 当前 main.py 中模拟了文件校验流程：

#

# 允许上传的文件类型：pdf、docx、txt

# 不允许上传 exe 等非法类型

# 文件大小超过限制时抛出 FileTooLargeError

# 文件类型不合法时抛出 InvalidFileTypeError

# 所有业务错误通过 logger 输出简洁日志，不直接暴露原始堆栈

# .gitignore 说明

#

# 当前项目不会提交以下内容：

#

# Python 虚拟环境

# Python 缓存文件

# 环境变量文件

# 前端依赖目录

# 上传文件目录

# 日志目录和日志文件

#

# 这些内容不应该进入 Git 仓库。

#

# 后续计划

#

# 接下来继续完成：

#

# FastAPI 最小服务

# API 路由拆分

# 文件上传接口

# Pydantic 请求体校验

# SQLite / PostgreSQL 数据库 CRUD

# Vue3 前端上传页面

# Docker Compose 一键启动

## 启动周 mini_demo

本周完成了一个命令行 task_manager 小程序，用于验证 Python 工程基础：

- 使用 pathlib 管理项目路径
- 使用 json 保存任务数据
- 使用 logging 输出运行日志
- 支持新增任务、列出任务、更新任务状态
- 使用 Git 分支完成当天学习内容提交

### 运行命令

````powershell
python backend\app\task_manager.py## 启动周 mini_demo

本周完成了一个命令行 task_manager 小程序，用于验证 Python 工程基础：

- 使用 pathlib 管理项目路径
- 使用 json 保存任务数据
- 使用 logging 输出运行日志
- 支持新增任务、列出任务、更新任务状态
- 使用 Git 分支完成当天学习内容提交

### 运行命令

```powershell
python backend\app\task_manager.py
````
