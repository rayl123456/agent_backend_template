from __future__ import annotations

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
TASK_FILE = DATA_DIR / "tasks.json"
LOG_FILE = LOG_DIR / "task_manager.log"

ALLOWED_STATUS = ["todo", "doing", "done"]


def setup_environment() -> None:
    """创建数据目录、日志目录，并初始化日志配置。"""

    DATA_DIR.mkdir(exist_ok=True)
    LOG_DIR.mkdir(exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


logger = logging.getLogger("task_manager")


def load_tasks() -> list[dict[str, Any]]:
    """从 JSON 文件读取任务列表。"""

    if not TASK_FILE.exists():
        return []

    try:
        content = TASK_FILE.read_text(encoding="utf-8")

        if not content.strip():
            return []

        return json.loads(content)

    except json.JSONDecodeError:
        logger.error("tasks.json 格式错误，无法解析")
        return []


def save_tasks(tasks: list[dict[str, Any]]) -> None:
    """把任务列表保存到 JSON 文件。"""

    TASK_FILE.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def get_next_task_id(tasks: list[dict[str, Any]]) -> int:
    """生成下一个任务 ID。"""

    if not tasks:
        return 1

    return max(task["task_id"] for task in tasks) + 1


def create_task(title: str, task_type: str = "general") -> dict[str, Any]:
    """创建一个任务对象。"""

    now = datetime.now().isoformat(timespec="seconds")
    tasks = load_tasks()

    new_task = {
        "task_id": get_next_task_id(tasks),
        "title": title,
        "task_type": task_type,
        "status": "todo",
        "created_at": now,
        "updated_at": now,
    }

    tasks.append(new_task)
    save_tasks(tasks)

    logger.info("新增任务：%s", new_task)

    return new_task


def list_tasks() -> list[dict[str, Any]]:
    """列出全部任务。"""

    tasks = load_tasks()
    logger.info("查询任务列表，共 %s 条", len(tasks))

    return tasks


def update_task_status(task_id: int, status: str) -> bool:
    """更新任务状态。"""

    if status not in ALLOWED_STATUS:
        logger.error("非法任务状态：%s", status)
        return False

    tasks = load_tasks()

    for task in tasks:
        if task["task_id"] == task_id:
            task["status"] = status
            task["updated_at"] = datetime.now().isoformat(timespec="seconds")
            save_tasks(tasks)

            logger.info("任务 %s 状态更新为 %s", task_id, status)

            return True

    logger.error("任务不存在：%s", task_id)

    return False


def print_tasks(tasks: list[dict[str, Any]]) -> None:
    """把任务列表打印到命令行。"""

    if not tasks:
        print("当前没有任务。")
        return

    print("\n当前任务列表：")

    for task in tasks:
        print(
            f"[{task['task_id']}] "
            f"{task['title']} | "
            f"type={task['task_type']} | "
            f"status={task['status']} | "
            f"created_at={task['created_at']}"
        )


def show_menu() -> None:
    """显示命令行菜单。"""

    print("\n====== task_manager mini demo ======")
    print("1. 新增任务")
    print("2. 列出任务")
    print("3. 更新任务状态")
    print("4. 退出")


def main() -> None:
    """程序入口。"""

    setup_environment()
    logger.info("task_manager 启动")

    while True:
        show_menu()
        choice = input("请选择操作：").strip()

        if choice == "1":
            title = input("请输入任务标题：").strip()
            task_type = input("请输入任务类型，例如 docs/logging/general：").strip() or "general"

            if not title:
                print("任务标题不能为空。")
                continue

            task = create_task(title=title, task_type=task_type)
            print(f"新增成功：{task}")

        elif choice == "2":
            tasks = list_tasks()
            print_tasks(tasks)

        elif choice == "3":
            task_id_text = input("请输入任务 ID：").strip()
            status = input("请输入新状态 todo/doing/done：").strip()

            if not task_id_text.isdigit():
                print("任务 ID 必须是数字。")
                continue

            success = update_task_status(int(task_id_text), status)
            print("更新成功。" if success else "更新失败，请检查任务 ID 或状态。")

        elif choice == "4":
            logger.info("task_manager 退出")
            print("已退出。")
            break

        else:
            print("无效选择，请输入 1/2/3/4。")


if __name__ == "__main__":
    main()