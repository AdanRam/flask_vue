<template>
  <div class="home">
    <Login msg="Login component"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Login from '@/components/Login.vue';
import { fetchAllUsers } from '@/api';

export default {
  name: 'Home',
  components: {
    Login,
  },
  data() {
    return {
      users: [],
    };
  },
  async created() {
    this.users = await fetchAllUsers();
  },
};
</script>
