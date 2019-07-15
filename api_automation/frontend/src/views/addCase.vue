<template>
    <section>
        <!-- <router-link :to="{ name: '接口列表', params: {project_id: this.$route.params.project_id}}" style='text-decoration: none;color: aliceblue;'>
            <el-button class="return-list"><i class="el-icon-d-arrow-left" style="margin-right: 5px"></i>接口列表</el-button>
        </router-link> -->
        <!-- <router-link :to="{ name: '接口列表', params: {project_id: this.$route.params.project_id}}" style='text-decoration: none;color: aliceblue;'> -->
        <!-- <el-button class="return-list" style="float: right">取消</el-button> -->
        <!-- </router-link> -->
        <!-- <el-button class="return-list" type="primary" style="float: right; margin-right: 15px z-index:999" @click.native="addApi">保存</el-button> -->
        <el-form :model="form" ref="form" :rules="FormRules">
            <div style="border: 1px solid #e6e6e6;margin-bottom: 10px;padding:15px">
                <el-row :gutter="9" class=topname style="margin-top:10px">
                    <el-col :span='8'>
                        <el-form-item label="接口名称:" label-width="83px" prop="name">
                            <el-input v-model.trim="form.name" placeholder="请填写接口名称" auto-complete></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row :gutter="10">
                    <el-col :span="4">
                        <el-form-item label="URL:" label-width="83px">
                            <!-- <el-select v-model="form.requestType"  placeholder="请求方式" @change="checkRequest"> -->
                            <el-select v-model="form.requestType"  placeholder="请求方式">
                                <el-option v-for="(item,index) in request" :key="index+''" :label="item.label" :value="item.value"></el-option>
                            </el-select>
                        </el-form-item>
                    </el-col>
                    <el-col :span="2">
                        <el-form-item>
                            <el-select v-model="form.httpType" placeholder="HTTP协议">
                                <el-option v-for="(item,index) in Http" :key="index+''" :label="item.label" :value="item.value"></el-option>
                            </el-select>
                        </el-form-item>
                    </el-col>
                    <el-col :span='18'>
                        <el-form-item prop="apiAddress">
                            <el-input v-model.trim="form.apiAddress" placeholder="路径地址" auto-complete></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
            </div>
            <el-row :span="24">
                <el-collapse v-model="activeNames" @change="handleChange">
                    <el-collapse-item title="请求头部" name="1">
                        <el-table :data="form.headDict" highlight-current-row>
                            <el-table-column prop="name" label="标签" min-width="20%" sortable>
                                <template slot-scope="scope">
                                    <el-select placeholder="head标签" filterable v-model="scope.row.name">
                                        <el-option v-for="(item,index) in header" :key="index+''" :label="item.label" :value="item.value"></el-option>
                                    </el-select>
                                    <el-input class="selectInput" v-model.trim="scope.row.name" :value="scope.row.name" placeholder="请输入内容"></el-input>
                                </template>
                            </el-table-column>
                            <el-table-column prop="value" label="内容" min-width="40%" sortable>
                                <template slot-scope="scope">
                                    <el-input v-model.trim="scope.row.value" :value="scope.row.value" placeholder="请输入内容"></el-input>
                                </template>
                            </el-table-column>
                            <el-table-column label="操作" min-width="5%">
                                <template slot-scope="scope">
                                    <!-- <el-button type="danger" icon="el-icon-delete" style="font-size:20px;cursor:pointer;" @click="delHead(scope.$index)" circle></el-button> -->
                                    <i class="el-icon-delete" style="font-size:25px;cursor:pointer;" @click="delHead(scope.$index)"></i>
                                </template>
                            </el-table-column>
                            <el-table-column label="" min-width="10%">
                                <template slot-scope="scope">
                                    <el-button v-if="scope.$index===(form.headDict.length-1)" size="mini" class="el-icon-plus" @click="addHead"></el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                    </el-collapse-item>
                    <el-collapse-item title="请求参数: 表单(form-data)" style="font-size:35px" name="2">
                        <!-- <div style="font-size:15px" floating:left>表单(form-data)</div> -->
                        <!-- <div style="margin: 5px">
                            <el-row :span="24">
                                <el-col :span="4"><el-radio v-model="radio" label="form-data">表单(form-data)</el-radio></el-col>
                                <el-col v-if="request3" :span="4"><el-radio v-model="radio" label="raw">源数据(raw)</el-radio></el-col>
                                <el-col v-if="request3" :span="16"><el-checkbox v-model="radioType" label="3" v-show="ParameterTyep">表单转源数据</el-checkbox></el-col>
                            </el-row>
                        </div> -->
                        <el-table :data="form.requestList" highlight-current-row class=parameter-a>
                            <el-table-column prop="name" label="参数名" min-width="25%" sortable>
                                <template slot-scope="scope">
                                    <el-input v-model.trim="scope.row.name" :value="scope.row.name" placeholder="请输入参数值"></el-input>
                                </template>
                            </el-table-column>
                            <el-table-column prop="value" label="参数值" min-width="30%" sortable>
                                <template slot-scope="scope">
                                    <el-input v-model.trim="scope.row.value" :value="scope.row.value" placeholder="请输入参数值"></el-input>
                                </template>
                            </el-table-column>
                            <el-table-column prop="_type" label="参数类型" min-width="14%" sortable>
                                <template slot-scope="scope">
                                    <el-select v-model="scope.row._type"  placeholder="请求方式">
                                        <el-option v-for="(item,index) in paramTyep" :key="index+''" :label="item.label" :value="item.value"></el-option>
                                    </el-select>
                                </template>
                            </el-table-column>
                            <el-table-column prop="description" label="参数说明" min-width="14%" sortable>
                                <template slot-scope="scope">
                                    <el-input v-model.trim="scope.row.description" :value="scope.row.desc" placeholder="请输入参数说明"></el-input>
                                </template>
                            </el-table-column>
                            <el-table-column label="操作" min-width="5%">
                                <template slot-scope="scope">
                                    <!-- <el-button type="danger" icon="el-icon-delete" style="font-size:20px;cursor:pointer;" @click="delHead(scope.$index)" circle></el-button> -->

                                    <i class="el-icon-delete" style="font-size:25px;cursor:pointer;" @click="delParameter(scope.$index)"></i>
                                </template>
                            </el-table-column>
                            <el-table-column label="" min-width="4%">
                                <template slot-scope="scope">
                                    <el-button v-if="scope.$index===(form.requestList.length-1)" size="mini" class="el-icon-plus" @click="addParameter"></el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                        <!-- <template>
                            <el-input :class=parameter-b type="textarea" :rows="5" placeholder="请输入内容" v-model.trim="parameterRaw"></el-input>
                        </template> -->
                    </el-collapse-item>
                    <el-collapse-item title="返回参数" name="3">
                        <el-table :data="form.responseList" highlight-current-row>
                            <el-table-column prop="name" label="参数名" min-width="25%" sortable>
                                <template slot-scope="scope">
                                    <el-input v-model.trim="scope.row.name" :value="scope.row.name" placeholder="请输入参数值"></el-input>
                                </template>
                            </el-table-column>
                            <el-table-column prop="value" label="参数值" min-width="30%" sortable>
                                <template slot-scope="scope">
                                    <el-input v-model.trim="scope.row.value" :value="scope.row.value" placeholder="请输入参数值"></el-input>
                                </template>
                            </el-table-column>
                            <el-table-column prop="_type" label="参数类型" min-width="14%" sortable>
                                <template slot-scope="scope">
                                    <el-select v-model="scope.row._type"  placeholder="请求方式">
                                        <el-option v-for="(item,index) in paramTyep" :key="index+''" :label="item.label" :value="item.value"></el-option>
                                    </el-select>
                                </template>
                            </el-table-column>
                            <el-table-column prop="description" label="参数说明" min-width="14%" sortable>
                                <template slot-scope="scope">
                                    <el-input v-model.trim="scope.row.description" :value="scope.row.desc" placeholder="请输入参数说明"></el-input>
                                </template>
                            </el-table-column>
                            <el-table-column label="操作" min-width="5%">
                                <template slot-scope="scope">
                                    <!-- <el-button type="danger" icon="el-icon-delete" style="font-size:20px;cursor:pointer;" @click="delHead(scope.$index)" circle></el-button> -->

                                    <i class="el-icon-delete" style="font-size:25px;cursor:pointer;" @click="delResponse(scope.$index)"></i>
                                    
                                </template>
                            </el-table-column>
                            <el-table-column label="" min-width="4%">
                                <template slot-scope="scope">
                                    <el-button v-if="scope.$index===(form.responseList.length-1)" size="mini" class="el-icon-plus" @click="addResponse"></el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                        
                    </el-collapse-item>
                </el-collapse>
            </el-row>
        </el-form>
        <el-button class="return-list" style="margin-top:10px">取消</el-button>
        <el-button class="return-list" type="primary" @click.native="addApi">保存</el-button>
    </section>
    
</template>
<script>
    import { requestAddCase } from "../api/api";

    export default {
        data() {
            return {
                request: [{value: 'GET', label: 'GET'},
                    {value: 'POST', label: 'POST'},
                    {value: 'PUT', label: 'PUT'},
                    {value: 'DELETE', label: 'DELETE'}],
                Http: [{value: 'HTTP', label: 'HTTP'},
                    {value: 'HTTPS', label: 'HTTPS'}],
                paramTyep: [{value: 'Int', label: 'Int'},
                    {value: 'String', label: 'String'}],
                checkHeadList: [],
                checkParameterList: [],
                ParameterTyep: true,
                group: [],
                radio: "form-data",
                secondGroup: [],
                // status: [{value: true, label: '启用'},
                //     {value: false, label: '禁用'}],
                header: [{value: 'Accept', label: 'Accept'},
                    {value: 'Accept-Charset', label: 'Accept-Charset'},
                    {value: 'Accept-Encoding', label: 'Accept-Encoding'},
                    {value: 'Accept-Language', label: 'Accept-Language'},
                    {value: 'Accept-Ranges', label: 'Accept-Ranges'},
                    {value: 'Authorization', label: 'Authorization'},
                    {value: 'Cache-Control', label: 'Cache-Control'},
                    {value: 'Connection', label: 'Connection'},
                    {value: 'Cookie', label: 'Cookie'},
                    {value: 'Content-Length', label: 'Content-Length'},
                    {value: 'Content-Type', label: 'Content-Type'},
                    {value: 'Content-MD5', label: 'Content-MD5'},
                    {value: 'Date', label: 'Date'},
                    {value: 'Expect', label: 'Expect'},
                    {value: 'From', label: 'From'},
                    {value: 'Host', label: 'Host'},
                    {value: 'If-Match', label: 'If-Match'},
                    {value: 'If-Modified-Since', label: 'If-Modified-Since'},
                    {value: 'If-None-Match', label: 'If-None-Match'},
                    {value: 'If-Range', label: 'If-Range'},
                    {value: 'If-Unmodified-Since', label: 'If-Unmodified-Since'},
                    {value: 'Max-Forwards', label: 'Max-Forwards'},
                    {value: 'Origin', label: 'Origin'},
                    {value: 'Pragma', label: 'Pragma'},
                    {value: 'Proxy-Authorization', label: 'Proxy-Authorization'},
                    {value: 'Range', label: 'Range'},
                    {value: 'Referer', label: 'Referer'},
                    {value: 'TE', label: 'TE'},
                    {value: 'Upgrade', label: 'Upgrade'},
                    {value: 'User-Agent', label: 'User-Agent'},
                    {value: 'Via', label: 'Via'},
                    {value: 'Warning', label: 'Warning'}],
                header4: "",
                addParameterFormVisible: false,
                addResponseFormVisible: false,
                required4:[{value: true, label: '是'},
                    {value: false, label: '否'}],
                httpCode:[{value: '', label: ''},
                    {value: '200', label: '200'},
                    {value: '404', label: '404'},
                    {value: '400', label: '400'},
                    {value: '500', label: '500'},
                    {value: '502', label: '502'},
                    {value: '302', label: '302'}],
                radioType: "",
                result: true,
                activeNames: ['1', '2', '3', '4'],
                id: "",
                // parameterRaw: "",
                request3: false,
                form: {
                    // apiGroupLevelFirst_id: '',
                    name: '',
                    // status: true,
                    requestType: 'POST',
                    httpType: 'HTTP',
                    apiAddress: '',
                    headDict: [{name: "", value: ""},
                        {name: "", value: ""}],
                    requestList: [{name: "", value: "", _type:"String", required: true, restrict: "", description: ""},
                        {name: "", value: "", _type:"String", required: true, restrict: "", description: ""}],
                    // requestParameterType: "",
                    responseList: [{name: "", value: "", _type:"String", required:true, description: ""},
                        {name: "", value: "", _type:"String", required:true, description: ""}],
                    // mockCode: '',
                    // data: '',
                },
                FormRules: {
                    name : [{ required: true, message: '请输入名称', trigger: 'blur' },
                        { max: 50, message: '不能超过50个字', trigger: 'blur' }],
                    apiAddress : [{ required: true, message: '请输入地址', trigger: 'blur' }],
                    // required : [{ type: 'boolean', required: true, message: '请选择状态', trigger: 'blur' }],
                    // apiGroupLevelFirst_id : [{ type: 'number', required: true, message: '请选择分组', trigger: 'blur'}],
                },
                editForm: {
                    name: "",
                    value: "",
                    required: "",
                    restrict: "",
                    description: "",
                },
                // editLoading: false
            }
        },
        methods: {
            addApi: function () {
                this.$refs.form.validate((valid) => {
                    if (valid) {
                        let self = this;
                        console.log(this.form.requestList);
                        this.$confirm('确认提交吗？', '提示', {}).then(() => {
                            let _parameter = {};
                            _parameter = this.form.requestList;
                            console.log(_parameter)
                            // _parameter = JSON.stringify(_parameter)
                            // console.log(_parameter)
                            let params = {
                                // project_id: Number(self.$route.params.project_id),
                                // apiGroupLevelFirst_id: Number(self.form.apiGroupLevelFirst_id),
                                name: self.form.name,
                                httpType: self.form.httpType,
                                requestType: self.form.requestType,
                                apiAddress: self.form.apiAddress,
                                // status: self.form.status,
                                headDict: self.form.headDict,
                                // requestParameterType: _type,
                                requestList: _parameter,
                                responseList: self.form.responseList,
                                // mockCode: self.form.mockCode,
                                // data: self.form.data,
                                description: "",
                            };
                            console.log(_parameter)
                            let headers = {
                                "Content-Type": "application/json",
                                // Authorization: 'Token ' + JSON.parse(sessionStorage.getItem('token'))
                            };
                            // requestAddCase(headers, params).then(_data => {
                            requestAddCase(params).then(_data => {
                                let {msg, code, data} = _data;
                                if (code === '999999') {
                                    self.$router.push("/project/case_list");
                                    self.$message({
                                        message: '保存成功',
                                        center: true,
                                        type: 'success'
                                    })
                                }
                                else {
                                    self.$message.error({
                                        message: msg,
                                        center: true,
                                    })
                                }
                            })
                        })
                    }
                })
            },
            
            addHead() {
                let headers = {name: "", value: ""};
                this.form.headDict.push(headers)
            },
            delHead(index) {
                this.form.headDict.splice(index, 1);
                if (this.form.headDict.length === 0) {
                    this.form.headDict.push({name: "", value: ""})
                }
            },
            addParameter() {
                let headers = {name: "", value: "", _type:"String", required:true, restrict: "", description: ""};
                this.form.requestList.push(headers)
            },
            delParameter(index) {
                this.form.requestList.splice(index, 1);
                if (this.form.requestList.length === 0) {
                    this.form.requestList.push({name: "", value: "", _type:"String", required:true, restrict: "", description: ""})
                }
            },
            addResponse() {
                let headers = {name: "", value: "", _type:"String", required:true, description: ""};
                this.form.responseList.push(headers)
            },
            delResponse(index) {
                this.form.responseList.splice(index, 1);
                if (this.form.responseList.length === 0) {
                    this.form.responseList.push({name: "", value: "", _type:"String", required:true, description: ""})
                }
            },
            handleChange(val) {
            },
            onSubmit() {
                console.log('submit!');
            },
        //     fastAdd() {
        //         let form = this.$route.params.formData;
        //         let _type = this.$route.params._type;
        //         let _typeData = this.$route.params._typeData;
        //         console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        //         console.log(form)
        //         if (form) {
        //             this.form.requestList = [];
        //             this.form.requestType = form.request4.toUpperCase();
        //             this.form.httpType = form.Http4;
        //             this.form.apiAddress = form.addr;
        //             this.form.headDict = form.head;
        //             // this.form.parameterRaw = form.parameterRaw;
        //             form.parameter.forEach((item) => {
        //                 item['_type'] = 'String';
        //                 item['required'] = true;
        //                 item['restrict'] = '';
        //                 item['description'] = '';
        //                 this.form.requestList.push(item)
        //             });
        //             this.form.parameter = form.parameter;
        //             this.form.mockCode = form.statusCode;
        //             this.form.data = JSON.stringify(form.resultData)
        //         }
        //         if (_type) {
        //             this.radio = _type
        //         }
        //         if (_typeData) {
        //             this.radioType = _typeData
        //         }
        //     }
        },
        mounted() {
            // this.getApiGroup();
            // this.fastAdd();
        }
    }
</script>

<style lang="scss" scoped>
    .return-list {
        margin-top: 0px;
        margin-bottom: 10px;
        border-radius: 25px;
    }
    .head-class {
        font-size: 17px
    }
    .parameter-a {
        display: block;
    }
    .parameter-b {
        display: none;
    }
    .selectInput {
        position: absolute;
        /*margin-left: 7px;*/
        padding-left: 9px;
        width: 180px;
        /*border-radius:0px;*/
        /*height: 38px;*/
        left: 1px;
        border-right: 0px;
    }
</style>
<style lang="scss">
    .selectInput{
        input{
            border-right: 0px;
            border-radius: 4px 0px 0px 4px;
        }
    }
</style>

