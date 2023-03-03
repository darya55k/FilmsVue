<template>
  <div class="film-list">
    <film-card
      class="film-card"
      v-for="film in reversedItems"
      :key="film.id"
      :film="film"
    />
  </div>
</template>

<script>
import FilmCard from "./FilmCard";

export default {
  props: {
    films: {
      type: Array,
      default: () => [],
    },
  },
  computed: {
    reversedItems() {
      return [...this.films].reverse();
    },
  },

  components: { FilmCard },
};
</script>

<style lang="scss" scoped>
.film-card {
  margin-bottom: 40px;
}
</style>