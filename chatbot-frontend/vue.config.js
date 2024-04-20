const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {
    port: 8080,
    proxy: {
      '/api': {
        target: process.env.VUE_APP_API_URL, // 后端服务器地址
        changeOrigin: true,
        pathRewrite: {
          '^/api': '', // 如果后端接口需要去除'/api'前缀
        },
      },
    },
  },
});