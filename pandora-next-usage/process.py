# -*- coding: utf-8 -*-
import os
import uuid
import requests
import json
import time
import logging

from dotenv import load_dotenv


# 不能删除此程序新建的对话，因为会话id在此程序运行过程中会一直保留，
# 如果删除了，会话id就无法找到（新会话conversation_id应为none），造成错误
class AskChatGPT:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def process_data(
        self,
        prompt,
        stop=None,
    ):
        model = "gpt-4"  # gpt-4/text-davinci-002-render-sha
        data = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt},
            ],
        }
        response = requests.post(
            f"{self.url}/v1/chat/completions", json=data, headers=self.headers
        )
        if response.status_code not in range(200, 300):
            logging.error(
                f"API call failed with status {response.status_code}: {response.text}"
            )
            return json.dumps({"error": f"API call failed: {response.text}"})
        try:
            # response_data = self.pre_process(response.text)  # 新的预处理
            response_data = response.text
            response_data = json.loads(response_data)  # 尝试解析数据
            # print("response_data", response_data)
            parts = response_data["choices"][0]["message"]["content"]
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON data: {response_data}")
            response_data = json.dumps(
                {"error": "Invalid data received, Jsondecodererror"}
            )  # 创建一个错误的 JSON 响应
            return response_data
        except TypeError:
            logging.error(f"Invalid JSON data: {response_data}")
            response_data = json.dumps({"error": "Invalid data received, type error"})
            return response_data
        # 将 parts 中的字符串连接起来形成完整的回复
        response_message = "".join(parts)
        if stop:
            for stop_value in stop:
                stop_index = response_message.find(stop_value)
                if stop_index != -1:
                    response_message = response_message[:stop_index]
                    break
        return response_message


if __name__ == "__main__":
    load_dotenv()  # 加载 .env 文件
    token = os.environ.get("PANDORA_SHARE_TOKEN")
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    url = os.environ.get("URL")
    ask_chatgpt = AskChatGPT(url, headers)
    while True:
        input_data = input("请输入：")
        print(ask_chatgpt.process_data(input_data))
        time.sleep(1)
