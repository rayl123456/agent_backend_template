class AppError(Exception):
    """
    项目基础异常。

    所有业务异常都继承它，方便后续统一处理。
    """

    def __init__(self, message: str, error_code: str = "APP_ERROR"):
        self.message = message
        self.error_code = error_code
        super().__init__(message)


class InvalidFileTypeError(AppError):
    """
    文件类型不允许。
    """

    def __init__(self, file_type: str):
        super().__init__(
            message=f"不支持的文件类型：{file_type}",
            error_code="INVALID_FILE_TYPE",
        )


class FileTooLargeError(AppError):
    """
    文件过大。
    """

    def __init__(self, size_mb: float, max_size_mb: int):
        super().__init__(
            message=f"文件大小 {size_mb:.2f}MB 超过限制 {max_size_mb}MB",
            error_code="FILE_TOO_LARGE",
        )