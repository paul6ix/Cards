<template>
  <div class="page-card">
    <div class="columns is-multiline">
      <div class="column is-9">
        <figure class="image mb-6">
          <img v-bind:src="card.get_image">
        </figure>

        <h1 class="title">{{ card.name }}</h1>

        <p>{{ card.description }}</p>
      </div>

      <div class="column is-3">
        <h2 class="subtitle">Information</h2>

        <p><strong>Price: </strong>${{ card.price }}</p>

        <div class="field has-addons mt-6">
          <div class="control">
            <input type="number" class="input" min="1" v-model="quantity">
          </div>

          <div class="control">
            <a class="button is-dark" @click="addToCart()">Add to cart</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "Card",
  data() {
    return {
      card: {},
      quantity: 1
    }
  },
  mounted() {
    this.getCards()
  },
  methods: {
    getCards() {
      const card_slug = this.$route.params.card_slug
      const category_slug = this.$route.params.category_slug
      axios
          .get(`/api/v1/card/${category_slug}/${card_slug}`)
          .then(response => {
            this.card = response.data
          })
          .catch(error => {
            console.log(error)
          })

    }
  }
}
</script>

<style scoped>

</style>