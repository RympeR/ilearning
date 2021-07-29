<template>
  <div>
    <span class="title" @click="toogle" :class="{rotate:isExpand}">{{ title }}</span>
    <span class="loading" v-if="isExpand && isLoading">
      <img src="@/assets/img/loading.gif">
    </span>
    <FilterItems v-if="isExpand" :items="items" :section="section" />
  </div>
</template>

<script>
import axios from 'axios'
import FilterItems from '@/components/Catalog/FilterItems.vue'

export default {
  name: "filter-section",
  props: ['title', 'apiUrl', 'section'],
  data: () => ({
    items: [],
    isExpand: false,
    isLoading: true
  }),
  components: {
    FilterItems
  },
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
    },
    selectItem(item) {
      let section = this.section
      let id = item
      let checked = false
      this.items.map(function (item) {
        if (item.id == id) {
          item.checked = !item.checked
          checked = item.checked
        }
      })
      this.$store.dispatch('catalog/CHANGE_FILTER', {section, id, checked})
    }
  }
}
</script>
