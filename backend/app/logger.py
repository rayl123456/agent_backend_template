import logging
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)


def get_logger(name: str = "agent_backend") -> logging.Logger:
    """
    创建并返回项目 logger。

    日志格式包含：
    1. 时间
    2. 日志级别
    3. 模块名
    4. 日志内容
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_DIR / "app.log", encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


if __name__ == "__main__":
    logger = get_logger()
    logger.info("这是一条 info 日志")
    logger.warning("这是一条 warning 日志")
    logger.error("这是一条 error 日志")