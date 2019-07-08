import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import login from '@/common/login'
import projectList from '@/views/projectList.vue'
import caseList from '@/views/caseList'
import addproject from '@/components/addbody'
import addcase from '@/views/addCase'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path:'/project/project_list',
      name:'projectList',
      component:projectList,
    },
    {
      path:'/addproject',
      name:'addproject',
      component:addproject
    },
    {
      path:'/project/case_list',
      name:'caseList',
      component:caseList,
    },
    {
      path:'/addcase',
      name:'addcase',
      component:addcase,
    },
    
  ]
})
