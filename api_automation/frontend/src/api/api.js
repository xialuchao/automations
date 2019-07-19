import axios from 'axios';

export const test = 'http://127.0.0.1:8000';
// 登录
export const requestLogin = params => { return axios.post(`${test}/user/login`, params).then(res => res.data); };
// 添加项目
export const requestAddProject = params => { return axios.post(`${test}/project/add`, params).then(res => res.data); };
// 查询所有项目
export const requestProjectList = params => { return axios.get(`${test}/project/get`, params).then(res =>res.data); };
// 删除项目
export const requestDelProject = params => {return axios.delete(`${test}/project/del`, {data: params}).then(res => res.data); };
// 添加用例（接口）
export const requestAddCase = params => {return axios.post(`${test}/case/add`, params).then(res => res.data); };
// 查询所有接口
export const requestCaseList = params => {return axios.get(`${test}/case/get`, params).then(res =>res.data); };
// 删除接口
export const requestDelCase = params => {return axios.delete(`${test}/api/del`, {data: params}).then(res => res.data); };


