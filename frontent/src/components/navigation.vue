<template>
  <header class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">
    <a href="/" class="d-flex align-items-center col-md-3 mb-2 mb-md-0 text-dark text-decoration-none">
      <svg class="bi me-2" width="40" height="32" role="img" aria-label="Bootstrap"><use xlink:href="#bootstrap"></use></svg>
    </a>

    <ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
      <li><router-link :to="{ name: 'home' }" class="nav-link px-2 link-secondary">Home</router-link></li>
      <li><router-link :to="{ name: 'admin' }" class="nav-link px-2 link-secondary">Admin</router-link></li>
       <li><router-link :to="{ name: 'songs' }" class="nav-link px-2 link-secondary">Songs</router-link></li>
    </ul>

    <div class="col-md-3 text-end">
      <button type="button" class="btn btn-outline-primary me-2">Login</button>
      <button type="button" class="btn btn-primary">Sign-up</button>
    </div>
  </header>
</template>

<script>
export default {
  name: 'navigation',
}
</script><!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>