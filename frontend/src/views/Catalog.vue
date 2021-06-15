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
              <FilterSection :title="section.title" :apiUrl="host + section.apiurl" />
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
    host: process.env.VUE_APP_BACKEND_HOST,
    sections: [
      {
        title: 'By Type of Activity',
        apiurl: '/info/task-types-list/'
      },
      {
        title: 'By Grade',
        apiurl: '/info/learning-range-list/'
      },
      {
        title: 'By Subject',
        apiurl: '/info/learning-subjects-list/'
      },
      {
        title: 'By Topic',
        apiurl: '/info/lesson-theme-list/'
      },
      {
        title: 'By Type of Game',
        apiurl: '/info/lesson-type-list/'
      },
      {
        title: 'By Cognitive Process',
        apiurl: '/info/education-process-list/'
      }
    ],
    items: []
  }),
  components: {
    FilterSection
  },
  mounted() {
    axios
      .get(this.host + '/lessons/card-list/')
      .then(response => (this.items = response.data.results))
  }
}
</script>

<style lang="scss">
.filter-list {
  padding-right: 30px;
  span.title {
    font-size: 18px;
    font-weight: 700;
    display: block;
    cursor: pointer;
    position: relative;

    &:after {
      position: absolute;
      content: '';
      right: 2px;
      top: 7px;
      width: 10px;
      height: 10px;
      border-right: 4px solid #464646;
      border-bottom: 4px solid #464646;
      -webkit-transform: rotate(-45deg);
      -ms-transform: rotate(-45deg);
      transform: rotate(-45deg);
      transition: 0.4s;
    }

    &.rotate:after {
      -webkit-transform: rotate(45deg);
      -ms-transform: rotate(45deg);
      transform: rotate(45deg);
    }
  }
  span.loading {
    img {
      width: 10%;
      margin: 10px auto;
      display: block;
    }
  }
  ul {
    ul {
      padding-left: 23px;
    }
  }
  > li {
    padding: 13px 0;
    border-top: 1px solid rgba(70,70,70, 0.25);
    div {
      > ul {
        margin-top: 20px;
      }
    }
  }
}
</style>