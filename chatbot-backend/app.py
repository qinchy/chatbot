import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from flask import Flask, jsonify, request

# 加载环境变量
load_dotenv(find_dotenv())

# 初始化 OpenAI 客户端
client = OpenAI()  # 使用环境变量中的 OPENAI_API_KEY 和 OPENAI_BASE_URL

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    """
    处理来自客户端的聊天请求。
    
    接收 POST 请求，其中包含用户的消息，然后将该消息发送给 GPT-3.5 模型，
    并将模型的响应返回给用户。
    
    参数:
    - 无
    
    返回值:
    - 包含模型响应的 JSON 对象
    """
    data = request.get_json()
    print(f"请求参数：{data}")
    user_input = data['message']

    response = query_gpt_3_5(user_input)
    print(f"响应结果：{response}")
    return jsonify({"response": response})

def query_gpt_3_5(message, response_format="text", model="gpt-3.5-turbo"):
    """
    向 GPT-3.5 模型发送查询并获取响应。
    
    参数:
    - message: str，要发送给模型的用户消息
    - response_format: str，指定返回消息的格式，默认为 'text'
    - model: str，指定使用的 GPT 模型，默认为 'gpt-3.5-turbo'
    
    返回值:
    - 模型响应的内容（根据 response_format 可能是文本或 JSON 对象）
    """
    messages = [{"role": "user", "content": message}]    # 构造用户输入
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,                                  # 设置温度为 0，减少随机性
        response_format={"type": response_format},      # 指定响应格式
    )

    return response.choices[0].message.content    # 返回模型的响应内容

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
        )