from config import get_settings
from exceptions import AppError, FileTooLargeError, InvalidFileTypeError
from logger import get_logger


logger = get_logger(__name__)
settings = get_settings()

ALLOWED_FILE_TYPES = ["pdf", "docx", "txt"]


def get_file_type(filename: str) -> str:
    """
    从文件名中获取扩展名。
    """

    if "." not in filename:
        raise InvalidFileTypeError("unknown")

    return filename.split(".")[-1].lower()


def validate_file(filename: str, size_mb: float) -> dict:
    """
    校验文件类型和文件大小。
    """

    file_type = get_file_type(filename)

    if file_type not in ALLOWED_FILE_TYPES:
        raise InvalidFileTypeError(file_type)

    if size_mb > settings.max_file_size_mb:
        raise FileTooLargeError(
            size_mb=size_mb,
            max_size_mb=settings.max_file_size_mb,
        )

    return {
        "filename": filename,
        "file_type": file_type,
        "size_mb": size_mb,
        "status": "valid",
    }


def run_demo() -> None:
    """
    模拟一次文件校验流程。
    """

    logger.info("应用启动：%s", settings.app_name)
    logger.info("上传目录：%s", settings.upload_dir)

    test_files = [
        ("case_material.docx", 2.5),
        ("virus.exe", 1.0),
        ("large_file.pdf", 20.0),
        ("no_extension", 1.0),
    ]

    for filename, size_mb in test_files:
        try:
            result = validate_file(filename, size_mb)
            logger.info("文件校验成功：%s", result)
        except AppError as e:
            logger.error(
                "文件校验失败：%s | error_code=%s",
                e.message,
                e.error_code,
            )
        except Exception:
            logger.exception("系统出现未知错误")


if __name__ == "__main__":
    run_demo()