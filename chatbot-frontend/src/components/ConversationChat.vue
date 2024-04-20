<template>
  <div class="conversation-chat">
    <!-- 新增对话历史记录容器 -->
    <div class="message-history">
      <ul>
        <li v-for="(message, index) in messages" :key="index" :class="{ 'self': message.role === 'user', 'bot': message.role === 'bot' }">
          <!-- 添加头像 -->
          <img :src="getAvatar(message.role)" :alt="message.role + ' avatar'" class="avatar" />
          <!-- 消息内容 -->
          <div class="message-content">{{ message.content }}</div>
        </li>
      </ul>
    </div>

    <!-- 输入框和发送按钮保持原样 -->
    <form @submit.prevent="sendMessage">
      <input type="text" v-model="userInput" placeholder="Type your message here..." />
      <button type="submit">Send</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      messages: [],
      userInput: '',
    };
  },
  methods: {
    async sendMessage() {
      try {
        // 先将用户输入的消息添加到对话历史记录中
        const userMessage = {
          role: 'user',
          content: this.userInput,
        };
        this.messages.push(userMessage);

        const response = await axios.post('/api/chat', { message: this.userInput });

        const botMessage = {
          role: 'bot',
          content: response.data.response,
        };

        this.userInput = '';
        this.messages.push(botMessage);
      } catch (error) {
        console.error('Error sending message:', error);
      }
    },
    getAvatar(role) {
      // 返回对应角色的头像URL
      switch (role) {
        case 'user':
          return require('@/assets/head.png'); // 替换为用户头像的实际路径
        case 'bot':
          return require('@/assets/logo.png'); // 替换为机器人头像的实际路径
        default:
          return '';
      }
    },  
  },
};
</script>

<style scoped>
  /* 添加对根元素（假设为#app）的样式 */
  #app {
     display: flex;
     min-height: 100vh;
     flex-direction: column;
     justify-content: space-between;
   }

  /* 保留原有样式 */
  .conversation-chat {
     max-width: 700px;
     margin: 0 auto; /* 可以删除此行，因为不再需要手动设置垂直距离 */
     flex-grow: 1; /* 新增样式 */
   }

  /* 添加头像样式 */
  .avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    object-fit: cover;
    margin-right: 10px; /* 与消息内容之间的间距 */
  }

  /* 新增对话历史记录容器样式 */
  .message-history {
    height: calc(100% - 90px); /* 调整高度以适应屏幕高度减去输入框高度（假设为40px） */
    overflow-y: auto; /* 添加滚动条以容纳过长的对话历史 */
  }

  /* 用户消息右对齐 */
  .self {
    text-align: right;
  }   

ul {
  list-style-type: none;
  padding: 0;
  flex-direction: column-reverse; /* 新增样式 */
}

li {
  margin-bottom: 10px;
  font-size: 16px;
}

.self {
  color: #007BFF;
}

.bot {
  color: #6C757D;
  text-align: left; /* 显式声明左对齐 */
}

form {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
}

input[type="text"] {
  flex-grow: 1;
  padding: 8px;
  border: 1px solid #ced4da;
  border-radius: 4px;
}

button {
  padding: 8px 12px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>