\# Day 02 学习日志：Python 函数、类、类型注解



\## 今日目标



\- 理解 Python 函数

\- 理解 Python 类

\- 理解类型注解

\- 理解 dataclass

\- 编写 User、Document、Task 三个基础业务类

\- 完成运行检查和 Git 提交



\## 今日完成内容



\- \[ ] 复习函数 function

\- \[ ] 复习类 class

\- \[ ] 复习类型注解 type hint

\- \[ ] 学习 dataclass

\- \[ ] 编写 backend/app/models.py

\- \[ ] 运行 python backend/app/models.py

\- \[ ] 完成 Git commit



\## 今日核心理解



1\. 函数的作用是：

2\. 类的作用是：

3\. 类型注解的作用是：

4\. dataclass 的作用是：

5\. User、Document、Task 之间的关系是：



\## 今日代码运行结果



```powershell

python backend\\app\\models.py

## 基础业务对象

当前项目定义了三个基础对象：

- User：表示系统用户
- Document：表示用户上传的文档
- Task：表示基于文档创建的处理任务

这三个对象后续会逐步迁移为 Pydantic Schema 和 SQLAlchemy ORM Model。

