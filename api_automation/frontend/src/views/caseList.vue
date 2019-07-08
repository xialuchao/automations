<template>
  <div class="listbody-part">
    <el-button class="upbtn" type="info" @click="newbtn">新增</el-button>
    <el-button class="upbtn" type="info" @click="getcaseList">刷新</el-button>
    <el-table :data="project" stripe style="width: 100%">
      <el-table-column prop="name" label="用例名" width="180"></el-table-column>
      <el-table-column prop="httpType" label="http/https" width="180"></el-table-column>
      <el-table-column prop="requestType" label="请求方式" width="180"></el-table-column>
      <el-table-column prop="caseAddress" label="用例接口地址" width="180"></el-table-column>
      <el-table-column fixed="right" label="操作">
        <template slot-scope="scope">
          <el-button type="text" size="small">编辑</el-button>
          <el-button @click="handleDel(scope.row)" type="text" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { requestProjectList, requestDelProject, requestCaseList} from '../api/api';
export default {
  name: 'listbody',
  data () {
    return {
      project: [],
    }
  },
  methods: {
    handleDel(row) {
      this.$confirm('确认删除该记录吗?', '提示', {type: 'warning'}).then(() => 
      {
        let self = this;
        let params = {ids: row.id + ''}
          requestDelProject(params).then(_data => {
            console.log(_data)
              let { msg, code, data } = _data;
              if (code === '999999') {
                  self.$message({
                      message: '删除成功',
                      center: true,
                      type: 'success'
                  })
              } else {
                  self.$message.error({
                      message: msg,
                      center: true,
                  })
              }
              self.getProjectList()
          });
      })
  },
    newbtn(){
        this.$router.push("/addcase")
    },
    getcaseList(){
        let self = this;
        requestCaseList().then((res) => {
            let { msg, code, data } = res;
            if (code === '999999') {
                self.project = data.data
                console.log(self.project)
            }
            else {
            self.$message.error({
                message: msg,
                center: true,
                })
            }
        })
    }
    },
  mounted() {
    this.getcaseList()
  },
}
</script>



<style>
.upbtn{
    float:left;
    margin:5px;
}
</style>


