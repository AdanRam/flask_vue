<template>
  <header>
    <h3>{{ title }}</h3>
    <a href="https://flask.palletsprojects.com/en/1.1.x/">
      <img src="../assets/flask-logo.png" alt="flask logo">
    </a>
    <img src="../assets/logo.png" alt="Vue logo">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </header>
</template>

<script>
export default {
  name: 'Header',
  props: {
    title: String,
  },
};
</script>

<style lang="scss" scoped>
header {
  background-color: #FBFBFB;
  text-align: center;
  padding: 10px;
  font-weight: bold;
  img {
    height: 50px;
  }
  a {
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
