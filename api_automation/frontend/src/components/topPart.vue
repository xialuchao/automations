<template>
  <div class="top-part">
    <el-menu
      :default-active="activeIndex"
      class="top_side"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="1" @click=projectList>项目</el-menu-item>
      <el-menu-item index="2" @click=caseList>用例</el-menu-item>
      <el-menu-item index="3" @click=hostList>主机</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'left-part',
  data () {
    return {
      msg: 'this is left part of vue',

    }
  },
  props:{
    activeIndex: String,
  },
  methods: {
      handleSelect(key, keyPath){
        console.log(key, keyPath);
      },
      projectList(){
        this.$router.push("/project/project_list")
      },
      caseList(){
        this.$router.push("/project/case_list")
      },
      hostList(){
        this.$router.push("/project/host_list")
      }
    }
}
</script>



<style>
/* .left-part {
    transition: width .28s;
    width: 220px!important;
    height: 100%;
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    z-index: 1001;
    background: rgb(48, 65, 86)
} */

li {
  display: inline-block;
  margin: 0 10px;
}

</style>
