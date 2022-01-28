<template>
  <div class="home">
    <section class="section is-dark hero is-medium">

      <div class="has-text-centered hero-body">
        <p class="title mb-6">
          WELCOME TO CARDS

        </p>
        <p class="subtitle"> A place to host all your cards from ATM cards to drivers license</p>

      </div>

    </section>
    <div class="column is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">
          Top Cards
        </h2>
      </div>
      <div class="row is-4 " v-for="card in recentCards" v-bind:key="card.id">
        <div class="column">
           <div class="box">
          <figure class="image mb-4">
            <img :src="card.get_thumbnail">
          </figure>
          <h3 class="is-size-4">{{ card.name }}</h3>
          <p class="is-size-6 has-text-grey">{{ card.price }}</p>
          <router-link :to="card.get_absolute_url" class="button is-dark mt-4">View details</router-link>

        </div>
        </div>


      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      recentCards: []
    }
  },
  components: {},
  mounted() {
    this.getRecentCards()
  },
  methods: {
    getRecentCards() {
      axios
          .get('api/v1/latest/')
          .then(response => {
            this.recentCards = response.data

          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}

</script>

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>