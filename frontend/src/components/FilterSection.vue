<template>
    <span @click="toogle" :class="{rotate:isExpand}">{{ title }}</span>
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
</template>

<script>
import axios from 'axios'
export default {
  props: ['title', 'apiUrl'],
  data: () => ({
    items: [],
    isExpand: false
  }),
  mounted() {
    axios
      .get(this.apiUrl)
      .then(response => (this.items = response.data.results))
  },
  methods: {
    toogle() {
      this.isExpand = !this.isExpand
    }
  }
}
</script>
