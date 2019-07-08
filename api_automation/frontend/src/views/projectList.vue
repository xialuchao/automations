<template>
  <div class="projectList">

    <listbody label1="项目名称" label2="版本" label3="类型" label4="描述" listname="project"></listbody>
  </div>
</template>

<script>
import listbody from "../components/listbody"
import toppart from "../components/topPart"

export default {
  name: 'projectList',
  data () {
    return {
      msg: 'Welcome to Your Project list PAGE',
      activeIndex: 1
    }
  },
  components: {toppart, listbody},
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
