import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from flask import Flask, jsonify, request

# 加载 .env 文件中定义的环境变量
_ = load_dotenv(find_dotenv())

# 初始化 OpenAI 客户端
client = OpenAI()  # 默认使用环境变量中的 OPENAI_API_KEY 和 OPENAI_BASE_URL

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    print(f"请求参数：{data}")
    user_input = data['message']

    response = query_gpt_3_5(user_input)
    print(f"响应结果：{response}")
    return jsonify({"response": response})

def query_gpt_3_5(message, response_format="text", model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": message}]    # 将 prompt 作为用户输入
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,                                  # 模型输出的随机性，0 表示随机性最小
        # 返回消息的格式，text 或 json_object
        response_format={"type": response_format},
    )

    return response.choices[0].message.content   

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
        )