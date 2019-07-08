<template>
    <div class="homeBox">
        <div style="width:32%;height: auto;margin-left: 30%">
            <div class="lun-container">
                <!-- <el-button type="width:100%" @click=root></el-button> -->
            </div>
            <img class="img-login" src="../assets/page1_3.jpg"/>
        </div>
        
            <!-- <el-input class="user" type="text" v-model.trim="ruleForm2.account" auto-complete="off" placeholder="账号"></el-input>
            <el-input class="pwd" type="password" v-model.trim="ruleForm2.checkPass" auto-complete="off" placeholder="密码"></el-input> -->
        
        <el-form :model="ruleForm2" :rules="rules2" ref="ruleForm2" label-position="left" label-width="0px" class="demo-ruleForm login-container">
            <h3 class="title">系统登录</h3>
            <el-form-item prop="account">
                <el-container></el-container>
                <el-input type="text" v-model.trim="ruleForm2.account" auto-complete="off" placeholder="账号">账号</el-input>
            </el-form-item>
            <el-form-item prop="checkPass">
                <el-input type="password" v-model.trim="ruleForm2.checkPass" auto-complete="off" placeholder="密码">密码</el-input>
            </el-form-item>
            <el-checkbox v-model="checked" checked class="remember">记住密码</el-checkbox>
            <el-form-item style="width:100%;">
                <el-button type="primary" style="width:100%;" @click.native.prevent="handleSubmit2" :loading="logining">登录</el-button>
                <!-- <el-button type="primary" style="width:100%;" @click.native.prevent="root">根目录</el-button> -->
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    /* eslint-disable */
    import { requestLogin } from '../api/api';
    export default {
        data () {
            return {
                logining: false,
                ruleForm2: {
                    account: '',
                    checkPass: ''
                },
                rules2: {
                    account: [
                        { required: true, message: '请输入账号', trigger: 'blur' }
                        // { validator: validaePass }
                    ],
                    checkPass: [
                        { required: true, message: '请输入密码', trigger: 'blur' }
                        // { validator: validaePass2 }
                    ]
                },
                checked: true
            }
        },
        methods: {
            root(){
                this.$router.push("/projectList")
            },
            handleSubmit2(ev) {
                var _this = this;
                this.$refs.ruleForm2.validate((valid) => {
                    if (valid) {
                        this.logining = true;
                        console.log(this.ruleForm2.account)
                        console.log(this.ruleForm2.checkPass)
                        var loginParams = { username: this.ruleForm2.account, password: this.ruleForm2.checkPass };
                        requestLogin(loginParams).then(_data => {
                            _this.logining = false;
                            console.log(_data)
                            let { msg, code, data } = _data;
                            console.log(_data);
                            if (code === '999999') {
                                sessionStorage.setItem('username', JSON.stringify(data.first_name));
                                sessionStorage.setItem('token', JSON.stringify(data.key));
                                console.log(_this.$route);
                                if (_this.$route.query.url) {
                                    _this.$router.push(_this.$route.query.url);
                                } else {
                                    _this.$router.push('/project/project_list');
                                }
                            }
                            else {
                                _this.$message.error({
                                    message: msg,
                                    center: true
                                })
                            }
                        });
                        // console.log("submit success")
                        // this.$router.push('/project/project_list')
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            }
        }
    }

</script>

<style lang="scss" scoped>
    .homeBox {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0px;
        background-color: #0d6e9b;
    }
  .login-container {
    /*box-shadow: 0 0px 8px 0 rgba(0, 0, 0, 0.06), 0 1px 0px 0 rgba(0, 0, 0, 0.02);*/
      position: absolute;
    -webkit-border-radius: 5px;
    border-radius: 5px;
    -moz-border-radius: 5px;
    background-clip: padding-box;
    /*margin: 180px auto;*/
      /*margin-top: 10%;*/
      /*right: 50px;*/
    width: 300px;
    padding: 35px 35px 15px 35px;
    background: #0041f3;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
      z-index: 1000;
    float: right;
    right: 4%;
    top: 25%;
    .title {
      margin: 0px auto 40px auto;
      text-align: center;
      color: #2ec0f6;
    }
    .remember {
      margin: 0px 0px 35px 0px;
        color: #eaeaea;
    }
  }
    .img-login {
        margin-top: -35%;
        width: 100%;
        height: auto;
    }
    .title0 {
        position: absolute;
        top: 10%;
        left: -41px;
        width: 100%;
        text-align: center;
        color: #f62e2e;
        font-size: 40px;
        height: 70px;
        line-height: 70px;
        /*<!--margin: -300px 0 0 0;-->*/
        z-index: 1000;
    }
    .title1 {
        position: absolute;
        top: 16%;
        left: -41px;
        width: 100%;
        text-align: center;
        color: #eaeaea;
        font-size: 20px;
        height: 70px;
        line-height: 70px;
        /*<!--margin: -300px 0 0 0;-->*/
        z-index: 1000;
        margin-top: 25px;
    }
    .tyg-div {
        color: #2ec0f6;
        z-index: -1000;
        float: left;
        position: absolute;
        left: 5%;
        top: 20%;
        font-size: 30px;
        list-style-type:none
    }
    .lun-container{
        width: 210px;
        height:140px;
        position: relative;
        font-size: 32px;
        color: #FFFFFF;
        text-align: center;
        line-height: 90px;
        margin: 200px auto;
        margin-bottom: 0px;
        margin-top:48%;
        perspective: 1000px;
        z-index: 1000;
    }
    .carouse{
        transform-style:preserve-3d;

    }
    .carouse div{
        display: block;
        position: absolute;
        width: 140px;
        height: 90px;
    }

    .carouse .pic1{
        transform: rotateY(0deg) translateZ(160px);
    }
    .carouse .pic2{
        transform: rotateY(120deg) translateZ(160px);
    }
    .carouse .pic3{
        transform: rotateY(240deg) translateZ(160px);
    }

    /*=== 下一个动画 ===*/
    @keyframes to-scroll1 {
        0%{
            transform: rotateY(0deg);
        }

        33%{
            transform: rotateY(-120deg);

        }
        66%{
            transform: rotateY(-240deg);

        }
        100%{
            transform: rotateY(-360deg);

        }

    }
    #carouse1{
        animation: to-scroll1  10s ease infinite;
        /*animation-fill-mode: both;*/
    }
</style>
