<template>
  <ul>
    <li v-for="item in rootItems" :key="item.id">
      <label class="checkbox">
          <input type="checkbox" :checked="item.checked" @click.stop="selectItem(item.id)">
          <div class="check-info">
            <a href="#" @click.prevent="selectItem(item.id)">
              {{ item.name }}
            </a>
          </div>
        </label>
        <FilterItems v-if="hasSubItems(item.id)" :items="items" :id="item.id" :section="section" />
    </li>
  </ul>
</template>

<script>
export default {
  name: 'FilterItems',
  props: {
    items: {
      type: Array,
      required: true
    },
    id: {
      type: Number,
      required: false,
      default: null
    },
    section: {
      type: String,
      required: true
    }
  },
  computed: {
    rootItems: function () {
      let id = this.id
      if(id === null) {
        return this.items.filter(function (item) {
          return !item.parent
        })
      } else {
        return this.items.filter(function (item) {
          return item.parent == id
        })
      }
      
    }
  },
  methods: {
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
    },
    hasSubItems: function (id) {
      if(this.items.filter(function (item) {
          return item.parent == id
      }).length > 0) {
        return true
      } else {
        return false
      }
    }
  }
}
</script>