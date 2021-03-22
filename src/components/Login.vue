<template>
  <form class="login" @submit.prevent="login">
    <h3>{{ msg }}</h3>
    <label for="email" class="visually-hidden">Email Address</label>
    <input required v-model="email" type="email" id="email" placeholder="yours@example.com">
    <label for="password" class="visually-hidden">Password</label>
    <input required v-model="password" type="password" id="password" placeholder="your password">
    <div class="buttons">
      <button type="submit" @click="authenticate">Login</button>
      <button type="submit" @click="register">Register</button>
    </div>
  </form>
</template>

<script>
export default {
  name: 'Login',
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.login {
  text-align: center;
  box-sizing: border-box;
  margin: auto;
}
</style>
