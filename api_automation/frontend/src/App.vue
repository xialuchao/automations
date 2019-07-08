

<template>
  <div id="app">
    <el-menu
      default-active="1"
      class="top_side"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="/project/project_list">项目</el-menu-item>
      <el-menu-item index="/project/case_list">用例</el-menu-item>
      <el-menu-item index="/project/host_list">主机</el-menu-item>
    </el-menu>
    <router-view></router-view>
  </div> 
</template>

<script>
export default {
  name: 'App',
  methods: {
    handleSelect(key, keyPath) {
        this.$router.push({path:key});
      }
      
    }
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 61px;
}
</style>

