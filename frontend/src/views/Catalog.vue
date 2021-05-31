<template>
  <section class="filter-section">
    <div class="container">
      <div class="row">
        <div class="col-12 show-filter">
          <span>Фильтры</span>
        </div>
        <aside class="sidebar-filter col-lg-3 col-md-6">
          <ul class="filter-list">
            <li v-for="(section, index) in sections" :key="index">
              <FilterSection :title="section.title" :apiUrl="section.apiurl" />
            </li>
          </ul>
        </aside>
        <div class="list-category col-lg-9 col-md-12">
          <div class="category-wrapp">
            <div class="category-item" v-for="item in items" :key="item.id">

            </div>
            <p v-if="items.length == 0">No items</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import FilterSection from '@/components/FilterSection'
import axios from 'axios'
export default {
  name: 'main-layout',
  data: () => ({
    sections: [
      {
        title: 'By Type of Activity',
        apiurl: 'https://ilearning.tools/info/task-types-list/'
      },
      {
        title: 'By Grade',
        apiurl: 'https://ilearning.tools/info/learning-range-list/'
      },
      {
        title: 'By Subject',
        apiurl: 'https://ilearning.tools/info/learning-subjects-list/'
      },
      {
        title: 'By Topic',
        apiurl: 'https://ilearning.tools/info/lesson-theme-list/'
      },
      {
        title: 'By Type of Game',
        apiurl: 'https://ilearning.tools/info/lesson-type-list/'
      },
      {
        title: 'By Cognitive Process',
        apiurl: 'https://ilearning.tools/info/education-process-list/'
      }
    ],
    items: []
  }),
  components: {
    FilterSection
  },
  mounted() {
    axios
      .get('https://ilearning.tools/lessons/card-list/')
      .then(response => (this.items = response.data.results))
  }
}
</script>