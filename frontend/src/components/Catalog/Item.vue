<template>
  <div class="category-item">
    <div class="type-printable-worksheet">
        <a href="" class="id-cat">Распечатка</a>
        <a href="" class="image-cat">
            <img src="@/assets/img/noimage.png" alt="">
        </a>
    </div>
    <div class="info-cat">
        <a href="" class="name-cat">{{ item.name }}</a>
        <div class="article">Чтение</div>
        <a class="add_collection" href="" title="Add to collection">&nbsp;</a>
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