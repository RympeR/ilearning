<template>
  <section
    class="single-product"
    :class="{ loading: isLoading }"
  >
    <div class="container" v-if="item">
      <div class="row">
              <div class="col-12 col-lg-9 col-md-8 categoty-name-single">
                <img
                  :src="item.card_type.icon"
                  :alt="item.card_type.name"
                  height="45"
                />
                <p>{{ item.card_type.name }}: </p>
              </div>
              <div class="col-12 d-md-none name-small">
                <h1>{{ item.name }}</h1>
              </div>
              <div class="col-12 col-lg-3 col-md-4 social">
                <p>Поделиться</p>
                <ul class="social-list">
                  <li>
                    <a href="">
                      <img src="@/assets/img/icons/face.png" alt="">
                    </a>
                  </li>
                  <li>
                    <a href="">
                      <img src="@/assets/img/icons/pin.png" alt="">
                    </a>
                  </li>
                  <li>
                    <a href="">
                      <img src="@/assets/img/icons/you.png" alt="">
                    </a>
                  </li>
                  <li>
                    <a href="">
                      <img src="@/assets/img/icons/inst.png" alt="">
                    </a>
                  </li>
                </ul>
              </div>  
          </div>
          <div class="info-product-wrapp">
              <h1 class="d-none d-md-block">{{ item.name }}</h1>
              <div class="row product-wrapp">
                <div class="col-md-4" v-if="item.images">
                  <div class="slider-for">
                    <div
                      class="slider-for-img"
                      v-for="image in item.images"
                      :key="image.id"
                    >
                      <img :src="image.file" alt="">
                    </div>
                  </div>
                  <div class="slider-nav" v-if="item.images.length > 1">
                      <div
                        class="slider-nav-img"
                        v-for="image in item.images"
                        :key="image.id"
                      >
                        <img :src="image.file" alt="">
                      </div>
                  </div>
                </div>
                <div class="col-md-7 offset-md-1">
                  <div class="product-short-description" v-html="item.short_description">
                  </div>
                  <div class="row">
                    <div class="col-6 col-sm-6 col-md-6 col-lg-6">
                      <div class="product-buy">
                        <a href="" class="btn buy disabled">Купить {{ item.price }} {{ item.valute }}</a>
                      </div>
                    </div>
                    <div class="col-6 col-sm-6 col-md-6 col-lg-6 actions-right-block">
                      <div class="product-buy">
                        <a href="" class="btn download-product disabled" download>Скачать pdf</a>
                      </div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-6 col-sm-6 col-md-6 col-lg-6">
                      <div class="add-block">
                        <a href="" class="btn add_plan disabled" title="В разработке">
                          <IconPlan />
                        Добавить в план</a>
                      </div>
                    </div>
                    <div class="col-6 col-sm-6 col-md-6 col-lg-6 actions-right-block">
                      <div class="add-block">
                        <a
                          href=""
                          class="btn add_collection"
                          :class="{ added : item.favourite }"
                          title="Добавить в коллекцию"
                        >
                          Добавить в коллекцию
                        </a>
                      </div>
                    </div>
                  </div>
                  <div class="meta-single">
                    <ul>
                      <!-- Tags -->
                      <li
                        v-for="range in item.learning_range"
                        :key="range.id"
                      >
                        <a href="">{{ range.name }}</a>
                      </li>
                      <li
                        v-for="subject in item.learning_subjects"
                        :key="subject.id"
                      >
                        <a href="">{{ subject.name }}</a>
                      </li>
                      <li
                        v-for="theme in item.learning_themes"
                        :key="theme.id"
                      >
                        <a href="">{{ theme.name }}</a>
                      </li>
                      <li
                        v-for="type in item.learning_types"
                        :key="type.id"
                      >
                        <a href="">{{ type.name }}</a>
                      </li>
                      <li
                        v-for="process in item.education_process"
                        :key="process.id"
                      >
                        <a href="">{{ process.name }}</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="product-description" v-html="item.full_description">
              </div>
            </div>
    </div>
    <div class="container" v-if="!isLoading && !item">
      <p>Not found</p>
    </div>
  </section>
</template>

<script>
import {mapGetters} from 'vuex'
import IconPlan from '@/components/Icons/IconPlan.vue'

export default {
    name: "catalog-item",
    data() {
      return {
        isLoading: false,
        id: this.$route.params.id,
        item: ''
      }
        
    },
    components: {
      IconPlan
    },
    created() {
      if(this.GET_ITEMS.length) {
        this.item = this.GET_ITEMS.filter(item => {
          return item.id == this.id
        })[0]
      }
      if(!this.item) {

        this.isLoading = true
        this.$store.dispatch('catalog/RECEIVE_CURRENT_ITEM', this.id)
        .then((response) => {
          this.isLoading = false
          this.item = response.data
        })
        .catch(error => {
          this.isLoading = false
          console.log(error.response.data)
        })
      }
    },
    computed: {
      ...mapGetters({
        GET_ITEMS: 'catalog/GET_ITEMS'
      })
    }
}
</script>

<style lang="scss">
.single-product {
  min-height: 800px;
}
</style>