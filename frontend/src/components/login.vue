<template>
  <div>
    <h1>Welcome!</h1>
    <div>
      <div><input type="text" style="width: 300px;" placeholder="Please enter you ID" v-model="id"/></div>
      <div><button type="button" style="width: 300px; background-color: cornflowerblue;" v-on:click="login">Login</button></div>
      <div><button type="button" style="width: 300px;"><router-link :to="'anketa'">Register</router-link></button></div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Login',
  data () {
    return {
      id: null
    }
  },

  sockets: {
    output_stream: function(data) {
      this.videostream = this.marginstream;
      this.marginstream = data;
    },
    output_log: function(data) {
      this.logs.unshift(data);
    }
  },

  methods: {
    login: function () {
      this.$socket.emit('login', this.id);
      this.$socket.emit('join', 'USER');
      this.$router.push('/watchmatch');
      this.$router.go(1);
    }
  }

}
</script>
