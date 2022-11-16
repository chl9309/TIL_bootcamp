<template>
  <div id="app">
    <nav>
      <router-link to="/movies">Movie</router-link> |
      <router-link to="/random">Random</router-link> |
      <router-link to="/watch-list">WatchList</router-link>
    </nav>
    <router-view/>
    
  </div>
</template>

<style>

body{
  background: linear-gradient(135deg, rgb(72, 108, 96), #275654);
  background-size: 300% 300%;
}


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #001310e0;
}

nav a.router-link-exact-active {
  color: #96f9eae0;
}

</style>

