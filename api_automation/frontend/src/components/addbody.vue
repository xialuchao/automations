<template>
    <div class="top-add-part" style="width:500px">
        <div style="margin: 20px;"></div>
        <el-form :label-position="labelPosition" label-width="130px" :model="formLabelAlign">
        <el-form-item label="项目名称">
            <el-input v-model="formLabelAlign.name"></el-input>
        </el-form-item>
        <el-form-item label="版本号">
            <el-input v-model="formLabelAlign.version"></el-input>
        </el-form-item>
        <el-form-item label="类型">
            <el-input v-model="formLabelAlign.type"></el-input>
        </el-form-item>
        <el-form-item label="描述">
            <el-input v-model="formLabelAlign.description"></el-input>
        </el-form-item>
        </el-form>
        <el-button class="createbtn" type="primary" round @click="root">取    消</el-button>
        <el-button class="cancelbtn" type="primary" round @click="createProject">创建项目</el-button>
    </div>
    

</template>


<script>
import {requestAddProject} from "../api/api";
  export default {
    data() {
      return {
        labelPosition: 'left',
        formLabelAlign: {
          name: '',
          region: '',
          type: ''
        }
      }
    },
    methods:{
        createProject(){
            var projectParams = {name:this.formLabelAlign.name, version:this.formLabelAlign.version, type:this.formLabelAlign.type, description:this.formLabelAlign.description,
            status:this.formLabelAlign.status, lastUpdateTime:this.formLabelAlign.LastUpdateTime, createTime:this.formLabelAlign.createTime};
            var header = {"Content-Type": "application/json"};
            requestAddProject(projectParams).then(_data => {
                
                let { msg, code, data } = _data;
                
                if (code === '999999') {
                    this.$message({message: '添加成功',center: true,type: 'success'});
                    this.$router.push('/project/project_list')
                    }
                else {
                    alert(code)
                }
            })
        },
        root(){
                this.$router.push("/project/project_list")
            },
    }
  }
</script>

<style>
.createbtn{
    right: 0px;
}
</style>