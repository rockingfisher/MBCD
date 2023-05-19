<template>
  <div>
    <h1>temp</h1>
    <p>이름 : {{ username }}</p>
  </div>
</template>

<script>
export default {
  name: 'ProFile',
  methods: {
    getUser() {
      this.$store.dispatch('getUser')
    }
  },
  created() {
    this.getUser()
  },
  computed: {
    username() {
      return this.$store.state.username
    }
  }
}
</script>

<style>

</style>