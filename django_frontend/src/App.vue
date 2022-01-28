<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Cards</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu"
           @click="showMobileMenu =!showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>

      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
        <div class="navbar-end">
          <router-link to="#" class="navbar-item">Visa</router-link>
          <router-link to="#" class="navbar-item">MasterCard</router-link>
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="#" class="button is-light">Login</router-link>

              <router-link to="#" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart({{ cartTotalLength }})</span>
              </router-link>
            </div>

          </div>

        </div>

      </div>

    </nav>

  </div>
  <section class="section">
    <router-view/>
  </section>

  <footer class="footer">
    <p class="has-text-centered">All right reserved 2022</p>
  </footer>

</template>

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }
      return totalLength
    }
  }
}
</script>

<style lang="scss">
@import "../node_modules/bulma";

</style>
