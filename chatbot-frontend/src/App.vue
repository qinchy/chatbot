<template>
  <div id="app">
    <ConversationChat />
  </div>
</template>

<script>
import ConversationChat  from '@/components/ConversationChat.vue';

export default {
  components: {
    ConversationChat,
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

/* 如果您需要为整个应用添加额外的全局样式，可以在此处添加 */
</style>