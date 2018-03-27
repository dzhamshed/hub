import Vue from 'vue';
import Router from 'vue-router';
import VueSocketio from 'vue-socket.io';
import Logger from '@/components/logger';
import AnketaComponent from '@/components/anketa';
import Login from '@/components/login';
import WatchMatch from '@/components/watchmatch';
import Face from '@/components/face';

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
    },
    {
      path: '/watchmatch',
      name: 'Watchmatch',
      component: WatchMatch
    },
    {
        path: '/face',
        name: 'Face',
        component: Face
    }
  ]
});

Vue.use(VueSocketio, 'http://localhost:5000');

