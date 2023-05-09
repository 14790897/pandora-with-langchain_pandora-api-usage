[English](README.md)| 简体中文

# Pandora ChatGPT API Integration for Langchain(customize-longchain-LLm.py)

本项目通过整合 Pandora 项目，以 API 的形式调用 ChatGPT 网页版，并将其与 Langchain 的自定义语言模型结合使用，从而节省使用 GPT-4 API 的费用。

## 功能

- 调用 ChatGPT 网页版的 API
- 使用自定义。语言模型实现 ChatGPT 的功能
- 可选的停止符列表支持

## 代码示例

```python
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
import uuid
import requests
import json
from pydantic import BaseModel
import os
from tool import other_tools

class CustomChatGPT(LLM):
    ...

if __name__ == "__main__":
    llm = CustomChatGPT(base_url="your url")  # 需要自己在服务器上搭建pandora程序
    response = llm("This is a foobar thing")
```

## 使用方法

1. 将 Pandora 项目部署到您的服务器上。
2. 使用您的服务器 URL 替换 `your url`。
3. 实例化 `CustomChatGPT` 类。
4. 调用 `_call` 方法（也就是llm（“prompt“）），传入相关参数并获取返回的消息。

## 注意事项

- 请确保您的服务器已成功部署 Pandora 项目。
- 在使用 `_call` 方法时，请确保传入正确的参数，如：prompt、stop 等。

# Pandora ChatGPT API Integration for Langchain - 附加内容(pandora-usage.py)

本项目除了提供整合 Pandora 的功能，还会介绍 Pandora 的基本用法。

## Pandora 基本用法

下面的代码提供了一些基本的 Pandora 用法，包括：

- 列出可用模型
- 以分页方式列出会话列表
- 删除所有会话
- 通过会话 ID 获取指定会话详情
- 通过会话 ID 删除指定会话
- 通过会话 ID 设置指定的会话标题
- 自动生成指定新会话的标题
- 让 ChatGPT 重新生成回复
- 让 ChatGPT 讲之前的恢复继续下去
- 向 ChatGPT 提问，等待其回复

```python
import requests
import json
import uuid

# base_url = "https://your-api-domain"  # 替换为您的API域名

# 列出账号可用的模型
def list_models():
    ...

# 以分页方式列出会话列表
def list_conversations(offset=1, limit=20):
    ...

# 删除所有会话
def delete_all_conversations():
    ...

# 通过会话ID获取指定会话详情
def get_conversation(conversation_id):
    ...

# 通过会话ID删除指定会话
def delete_conversation(conversation_id):
    ...

# 通过会话ID设置指定的会话标题
def set_conversation_title(conversation_id, title):
    ...

# 自动生成指定新会话的标题
def generate_conversation_title(conversation_id, model, message_id):
    ...

# 让ChatGPT重新生成回复
def regenerate_chatgpt(prompt, model, message_id, parent_message_id, conversation_id, stream=True):
    ...

# 让ChatGPT讲之前的恢复继续下去
def continue_chatgpt(model, parent_message_id, conversation_id, stream=True):
    ...

# 向ChatGPT提问，等待其回复
def ask_chatgpt(prompt, model, message_id, parent_message_id, conversation_id=None, stream=False):
    ...

def ask():
    ...

def main():
    ...

if __name__ == "__main__":
    main()
```

## 使用方法

1. 将您的 API 域名替换 `base_url`。
2. 调用相应的函数进行相应的操作。

## 注意事项

- 请确保您的 API 域名正确配置。
- 在调用函数时，请确保传入正确的参数。

## 贡献者

欢迎您为本项目作出贡献！请在 GitHub 上提交 issue 或 pull request。



