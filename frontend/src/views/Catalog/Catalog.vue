<template>
<div>
  <section class="filter-section">
    <div class="container">
      <div class="row">
        <div class="col-12 show-filter">
          <span>Фильтры</span>
        </div>
        <aside class="sidebar-filter col-lg-3 col-md-6">
          <ul class="filter-list">
            <li v-for="(section, index) in sections" :key="index">
              <FilterSection :title="section.title" :apiUrl="section.apiurl" :section="section.code" />
            </li>
          </ul>
        </aside>
        <div class="list-category col-lg-9 col-md-12">
          <div 
            class="category-wrapp"
            :class="{ loading: isLoading }"
          >
            <Item 
              v-for="item in currentPageItems"
              :key="item.id"
              :item="item"
            />
            <p v-if="!isLoading && GET_FILTERED.length == 0">No items</p>
          </div>
        </div>
      </div>
    </div>
  </section>
  <Pagination
    :items="GET_FILTERED"
    :pageSize="pageSize"
  />
</div>
</template>

<script>
import FilterSection from '@/components/Catalog/FilterSection'
import Item from '@/components/Catalog/Item'
import Pagination from '@/components/Common/Pagination'
import {mapGetters} from 'vuex'

export default {
  name: 'catalog',
  data() {
    return {
      isLoading: true,
      sections: [
        {
          title: 'Периоды обучения',
          apiurl: '/info/learning-range-list/',
          code: 'learning_range'
        },
        {
          title: 'Познавательные процессы',
          apiurl: '/info/education-process-list/',
          code: 'education_process'
        },
        {
          title: 'Предметы обучения',
          apiurl: '/info/learning-subjects-list/',
          code: 'learning_subjects'
        },
        {
          title: 'Темы занятий',
          apiurl: '/info/lesson-theme-list/',
          code: 'learning_themes'
        },
        {
          title: 'Типы игр',
          apiurl: '/info/lesson-type-list/',
          code: 'learning_types'
        },
        {
          title: 'Тип материала',
          apiurl: '/info/task-types-list/',
          code: 'card_type'
        }
      ],
      pageSize: 12
    }
  },
  components: {
    FilterSection, Item, Pagination
  },
  computed: {
    ...mapGetters({
      GET_ITEMS: 'catalog/GET_ITEMS',
      GET_FILTERED: 'catalog/GET_FILTERED',
      GET_CURRENT_PAGE: 'catalog/GET_CURRENT_PAGE'
    }),
    currentPageItems: function() {
      let begin = (this.GET_CURRENT_PAGE-1) * this.pageSize
      let end = begin + this.pageSize
      if(Array.isArray(this.GET_FILTERED)) {
        return this.GET_FILTERED.slice(begin, end)
      } else {
        return false
      }
    }
  },
  mounted() {
    this.isLoading = true
    this.$store.commit('catalog/SET_CURRENT_PAGE', this.$route.query.page || 1)
    this.$store.dispatch('catalog/RECEIVE_ITEMS')
    .then(() => {
      this.isLoading = false
    })
    .catch(error => {
      console.log(error)
    })
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