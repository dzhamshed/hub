import Vue from 'vue';
import Router from 'vue-router';
import VueSocketio from 'vue-socket.io';
import Logger from '@/components/logger';
import AnketaComponent from '@/components/anketa';
import Login from '@/components/login';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/logger',
      name: 'Logger',
      component: Logger
    },
    {
      path: '/anketa',
      name: 'Anketa',
      component: AnketaComponent
    }
  ]
});

Vue.use(VueSocketio, 'http://localhost:5000');

