from datetime import datetime
from typing import Optional, Literal


class User:
    """系统用户对象。后续会对应 users 数据表。"""

    def __init__(self, user_id: int, username: str, email: Optional[str] = None) -> None:
        self.user_id = user_id
        self.username = username
        self.email = email
        self.created_at = datetime.now()

    def to_dict(self) -> dict[str, object]:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
        }

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id}, username='{self.username}')"


class Document:
    """上传文档对象。后续会对应 documents 数据表。"""

    def __init__(
        self,
        document_id: int,
        user_id: int,
        filename: str,
        file_type: str,
        file_size: int,
        status: Literal["uploaded", "parsed", "failed"] = "uploaded",
    ) -> None:
        self.document_id = document_id
        self.user_id = user_id
        self.filename = filename
        self.file_type = file_type
        self.file_size = file_size
        self.status = status
        self.created_at = datetime.now()

    def mark_parsed(self) -> None:
        self.status = "parsed"

    def mark_failed(self) -> None:
        self.status = "failed"

    def is_pdf(self) -> bool:
        return self.file_type.lower() == "pdf"

    def to_dict(self) -> dict[str, object]:
        return {
            "document_id": self.document_id,
            "user_id": self.user_id,
            "filename": self.filename,
            "file_type": self.file_type,
            "file_size": self.file_size,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
        }

    def __repr__(self) -> str:
        return (
            f"Document(document_id={self.document_id}, "
            f"filename='{self.filename}', status='{self.status}')"
        )


class Task:
    """后端任务对象。后续可用于记录文档解析、RAG 检索、Agent 执行等任务。"""

    def __init__(
        self,
        task_id: int,
        user_id: int,
        document_id: Optional[int],
        task_type: str,
        status: Literal["pending", "running", "success", "failed"] = "pending",
    ) -> None:
        self.task_id = task_id
        self.user_id = user_id
        self.document_id = document_id
        self.task_type = task_type
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_status(self, status: Literal["pending", "running", "success", "failed"]) -> None:
        self.status = status
        self.updated_at = datetime.now()

    def to_dict(self) -> dict[str, object]:
        return {
            "task_id": self.task_id,
            "user_id": self.user_id,
            "document_id": self.document_id,
            "task_type": self.task_type,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def __repr__(self) -> str:
        return f"Task(task_id={self.task_id}, task_type='{self.task_type}', status='{self.status}')"


if __name__ == "__main__":
    user = User(user_id=1, username="rayl123456", email="rayl820@163.com")

    document = Document(
        document_id=101,
        user_id=user.user_id,
        filename="test.docx",
        file_type="docx",
        file_size=204800,
    )

    task = Task(
        task_id=1001,
        user_id=user.user_id,
        document_id=document.document_id,
        task_type="agent_review",
    )

    task.update_status("running")
    task.update_status("success")

    print(user)
    print(document)
    print(task)

    print(user.to_dict())
    print(document.to_dict())
    print(task.to_dict())

    print("Is PDF:", document.is_pdf())