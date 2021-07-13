<template>
  <div class="category-item">
    <div
      class="card-type"
      :class="item.card_type.slug"
    >
        <router-link :to="{name: 'CatalogItem', params: {id: item.id}}" class="id-cat">{{ item.card_type.name }}</router-link>
        <router-link :to="{name: 'CatalogItem', params: {id: item.id}}" class="image-cat">
            <img v-if="item.images.length" :src="item.images[0].file" alt="">
            <img v-if="item.images.length == 0" src="@/assets/img/noimage.png" alt="">
        </router-link>
    </div>
    <div class="info-cat">
        <router-link :to="{name: 'CatalogItem', params: {id: item.id}}" class="name-cat">{{ item.name }}</router-link>
        <div class="article">{{ item.learning_subjects[0].name }}</div>
        <a
          class="add_collection"
          :class="{ added : item.favourite }"
          href=""
          title="Add to collection"
        >
          &nbsp;
        </a>
    </div>
  </div>
</template>

<script>
export default {  
  name: "catalog-item", 
  props: {
    item: {
      type: Object,
      default() {
        return {}
      }
    }
  }
}
</script>

<style lang="scss">
  .card-type.worksheet {
    background-color: #37dc74;
  }
  .card-type.video {
    background-color: #02aaf3;
  }
  .card-type.offline-game {
    background-color: #fe6440;
  }
  .card-type.arts-and-crafts {
    background-color: #c866cd;
  }
  .card-type.music {
    background-color: #0077a2;
  }
  .card-type.science-research {
    background-color: #630a9a;
  }
  .card-type.workbook {
    background-color: #fece00;
  }
  .card-type.online-game {
    background-color: #e4a001;
  }
  .card-type.project {
    background-color: #e40981;
  }
  .card-type.lapbook {
    background-color: #009746;
  }
  .card-type.collection {
    background-color: #2b4898;
  }
</style>