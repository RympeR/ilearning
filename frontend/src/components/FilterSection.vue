<template>
  <div>
    <span class="title" @click="toogle" :class="{rotate:isExpand}">{{ title }}</span>
    <span class="loading" v-if="isExpand && isLoading">
      <img src="@/assets/img/loading.gif">
    </span>
    <ul v-if="isExpand">
      <li v-for="item in items" :key="item.id">
        <label class="checkbox">
          <a href="#">
            <input type="checkbox">
          </a>
          <div class="check-info">
            <a href="#">
              {{ item.name }} (<span>0</span>)
            </a>
          </div>
        </label>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "filter-section",
  props: ['title', 'apiUrl'],
  data: () => ({
    items: [],
    isExpand: false,
    isLoading: true
  }),
  mounted() {
    axios
      .get(this.apiUrl)
      .then(response => {
        this.items = response.data.results
        this.isLoading = false
      })
  },
  methods: {
    toogle() {
      this.isExpand = !this.isExpand
    }
  }
}
</script>
