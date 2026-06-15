from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    """
    用户对象。

    在后续 Agent 项目中，User 用来表示系统的使用者。
    例如：上传材料的人、发起咨询的人、创建任务的人。
    """

    id: int
    username: str
    email: str
    created_at: datetime


@dataclass
class Document:
    """
    文档对象。

    在后续 Agent 项目中，Document 用来表示用户上传的材料。
    例如：处罚决定书、证据材料、PDF、Word、TXT 文件。
    """

    id: int
    filename: str
    file_type: str
    file_size: int
    owner_id: int
    created_at: datetime


@dataclass
class Task:
    """
    任务对象。

    在后续 Agent 项目中，Task 用来表示一次处理任务。
    例如：解析文档、抽取要素、检索法规、生成文书。
    """

    id: int
    title: str
    status: str
    document_id: int
    created_at: datetime


def create_demo_user() -> User:
    """
    创建一个测试用户。
    """

    return User(
        id=1,
        username="ray",
        email="ray@example.com",
        created_at=datetime.now(),
    )


def create_demo_document(user: User) -> Document:
    """
    创建一个测试文档。
    """

    return Document(
        id=1,
        filename="test.pdf",
        file_type="pdf",
        file_size=2048,
        owner_id=user.id,
        created_at=datetime.now(),
    )


def create_demo_task(document: Document) -> Task:
    """
    创建一个测试任务。
    """

    return Task(
        id=1,
        title="学习 Python 类和类型注解",
        status="todo",
        document_id=document.id,
        created_at=datetime.now(),
    )

def is_allowed_file_type(file_type: str) -> bool:
    """
    判断文件类型是否允许上传。
    """

    allowed_types = ["pdf", "docx", "txt"]
    return file_type.lower() in allowed_types

if __name__ == "__main__":
    user = create_demo_user()
    document = create_demo_document(user)
    task = create_demo_task(document)

    print(user)
    print(document)
    print(task)

    print(is_allowed_file_type("pdf"))
    print(is_allowed_file_type("exe"))