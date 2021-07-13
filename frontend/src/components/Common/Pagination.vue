<template>
    <section class="pagination-section" v-if="pages.length > 1">
        <div class="container">
          <div class="pagination">
            <ul>
              <li v-for="page,index in pages" :key="index" :class="{ 'active-link': page == GET_CURRENT_PAGE } ">
                <a href="" @click.prevent="pageChangeHandler(page)">{{ page }}</a>
              </li>
            </ul>
          </div>
        </div>
      </section>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: "pagination",
  props: {
    items: {
      type: Object
    },
    pageSize: {
      type: Number,
      default: 20
    }
  },
  computed: {
    ...mapGetters({
      GET_CURRENT_PAGE: 'catalog/GET_CURRENT_PAGE'
    }),
    pages: function () {
      let pageCount = Math.ceil(this.items.length / this.pageSize)
      let output = []
      for(let i=1;i<=pageCount;i++){
        output.push(i)
      }
      if(pageCount > 4) {
        let prev = Number.parseInt(this.GET_CURRENT_PAGE) - 1
        let next = Number.parseInt(this.GET_CURRENT_PAGE) + 1
        if(next < pageCount-1) {
          output.splice(next,pageCount-next-1,'...')
        }
        if(prev > 2) {
          output.splice(1,prev-2,'...')
        }
      }
      return output
    }
  },
  methods: {
    pageChangeHandler(page) {
      if(page != this.GET_CURRENT_PAGE && page != '...') {
        this.$store.commit('catalog/SET_CURRENT_PAGE', page)
        if(page == 1) {
          this.$router.push(`${this.$route.path}`)
        } else {
          this.$router.push(`${this.$route.path}?page=${page}`)
        }
      }
    }
  }
}
</script>