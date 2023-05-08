import requests
import json
import uuid

# base_url = "https://your-api-domain"  # 替换为您的API域名

# 列出账号可用的模型
def list_models():
    response = requests.get(f"{base_url}/api/models")
    return response.json()

# 以分页方式列出会话列表
def list_conversations(offset=1, limit=20):
    params = {"offset": offset, "limit": limit}
    response = requests.get(f"{base_url}/api/conversations", params=params)
    return response.json()

# 删除所有会话
def delete_all_conversations():
    response = requests.delete(f"{base_url}/api/conversations")
    return response.json()

# 通过会话ID获取指定会话详情
def get_conversation(conversation_id):
    response = requests.get(f"{base_url}/api/conversation/{conversation_id}")
    return response.json()

# 通过会话ID删除指定会话
def delete_conversation(conversation_id):
    response = requests.delete(f"{base_url}/api/conversation/{conversation_id}")
    return response.json()

# 通过会话ID设置指定的会话标题
def set_conversation_title(conversation_id, title):
    data = {"title": title}
    response = requests.patch(f"{base_url}/api/conversation/{conversation_id}", json=data)
    return response.json()

# 自动生成指定新会话的标题
def generate_conversation_title(conversation_id, model, message_id):
    data = {"model": model, "message_id": message_id}
    response = requests.post(f"{base_url}/api/conversation/gen_title/{conversation_id}", json=data)
    return response.json()


# 让ChatGPT重新生成回复
def regenerate_chatgpt(prompt, model, message_id, parent_message_id, conversation_id, stream=True):
    data = {
        "prompt": prompt,
        "model": model,
        "message_id": message_id,
        "parent_message_id": parent_message_id,
        "conversation_id": conversation_id,
        "stream": stream
    }
    response = requests.post(f"{base_url}/api/conversation/regenerate", json=data)
    return response.json()

# 让ChatGPT讲之前的恢复继续下去
def continue_chatgpt(model, parent_message_id, conversation_id, stream=True):
    data = {
        "model": model,
        "parent_message_id": parent_message_id,
        "conversation_id": conversation_id,
        "stream": stream
    }
    response = requests.post(f"{base_url}/api/conversation/goon", json=data)
    return response.json()

# 向ChatGPT提问，等待其回复
def ask_chatgpt(prompt, model, message_id, parent_message_id, conversation_id=None, stream=False):
    data = {
        "prompt": prompt,
        "model": model,
        "message_id": message_id,
        "parent_message_id": parent_message_id,
        "stream": stream,
        "conversation_id": conversation_id,
    }
    if conversation_id is not None:
        data["conversation_id"] = conversation_id
    response = requests.post(f"{base_url}/api/conversation/talk", json=data)
    response_data = response.text
    response_data = json.loads(response_data)
    parts = response_data['message']['content']['parts']
    # 将 parts 中的字符串连接起来形成完整的回复
    response_message = ''.join(parts)
    print(response_message)
    return response_data["conversation_id"],response_data["message"]['id']

def ask():
    # 向ChatGPT提问
    leap_parent_message_id = False
    conversation_id = str(input("请输入conversation_id："))  # 需要手动设置5.2
    print("当前会话的id:", conversation_id)
    if conversation_id == "":
        print("创建会话")
        conversation_id = None
        parent_message_id = str(uuid.uuid4())
        leap_parent_message_id = True
    if not leap_parent_message_id:
        parent_message_id = str(input("请输入parent_message_id："))  # 需要手动设置5.2
    while True:
        # 向ChatGPT提问，等待其回复
        model = "text-davinci-002-render-sha"  # 选择一个可用的模型Default (GPT-3.5)：text-davinci-002-render-sha
        prompt = str(input("请输入prompt："))
        message_id = str(uuid.uuid4())  # 随机生成一个消息ID
        conversation_id, parent_message_id = ask_chatgpt(prompt, model, message_id, parent_message_id, conversation_id)
        print("当前会话的id:", parent_message_id)


def main():
    # 列出可用模型
    models = list_models()
    print("Available models:", models)

    # 以分页方式列出会话列表
    conversations = list_conversations(offset=1, limit=20)
    print("Conversations list:", conversations)

    # 向ChatGPT提问
    #ask()


    # # 获取会话ID，以便后续操作

    # # 通过会话ID获取指定会话详情
    # conversation_id = "a4eba9e6-4ca1-4d7b-80ef-fb96fbea74f5"
    # conversation = get_conversation(conversation_id)
    # print("Conversation details:", conversation)

    # 自动生成指定新会话的标题
    # gen_title_response = generate_conversation_title(conversation_id, model, message_id)
    # print("Generated title:", gen_title_response)

    # # 通过会话ID设置指定的会话标题
    # set_title_response = set_conversation_title(conversation_id, "新标题")
    # print("Set title response:", set_title_response)

    # # 让ChatGPT讲之前的恢复继续下去
    # parent_message_id = chatgpt_response["message_id"]
    # continue_response = continue_chatgpt(model, parent_message_id, conversation_id)
    # print("Continue response:", continue_response)

    # # 删除会话
    # conversation_id = "10daeb20-0eb4-4cc9-a2ba-05b6fdd4311b"
    # delete_response = delete_conversation(conversation_id)
    # print("Delete conversation response:", delete_response)

    #删除全部对话（慎用）
    # really_delete = str(input("是否删除全部对话？(y/n)"))
    # if really_delete == "y":
    #     delete_response = delete_all_conversations()
    #     print("Delete conversation response:", delete_response)

if __name__ == "__main__":
    main()
