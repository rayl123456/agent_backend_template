import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Settings:
    """
    项目配置对象。

    作用：
    1. 集中管理项目名称、调试模式、上传目录、日志级别等配置。
    2. 避免把配置散落在业务代码里。
    3. 后续接入 FastAPI、数据库、大模型 API 时，可以统一从这里读取。
    """

    app_name: str
    debug: bool
    upload_dir: Path
    log_level: str
    max_file_size_mb: int


def get_settings() -> Settings:
    """
    从环境变量读取配置。
    如果环境变量不存在，就使用默认值。
    """

    app_name = os.getenv("APP_NAME", "agent_backend_template")
    debug = os.getenv("DEBUG", "true").lower() == "true"
    upload_dir = Path(os.getenv("UPLOAD_DIR", "data/uploads"))
    log_level = os.getenv("LOG_LEVEL", "INFO")
    max_file_size_mb = int(os.getenv("MAX_FILE_SIZE_MB", "10"))

    upload_dir.mkdir(parents=True, exist_ok=True)

    return Settings(
        app_name=app_name,
        debug=debug,
        upload_dir=upload_dir,
        log_level=log_level,
        max_file_size_mb=max_file_size_mb,
    )


if __name__ == "__main__":
    settings = get_settings()
    print(settings)