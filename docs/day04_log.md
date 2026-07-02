# Day 04 学习日志：启动周集成 mini_demo

## 今日目标

- 学习 json、pathlib、logging 的工程用法
- 编写命令行 task_manager 小程序
- 支持新增任务、列出任务、更新任务状态
- 把任务保存到 data/tasks.json
- 把运行过程写入 logs/task_manager.log
- 使用 Git 分支完成当天提交

## 今日完成情况

- [x] 创建 backend/app/task_manager.py
- [x] 创建 data/tasks.json
- [x] 生成 logs/task_manager.log
- [x] 新增至少 2 个任务
- [x] 成功列出任务
- [x] 成功更新任务状态
- [x] README 已更新
- [ ] Git commit 已完成
- [ ] 合并回 main

## 今日运行命令

```powershell
python backend\app\task_manager.py
Get-Content data\tasks.json -Encoding UTF8
Get-Content logs\task_manager.log -Encoding UTF8