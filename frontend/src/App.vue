<template>
  <component :is="layout">
    <router-view />
  </component>
</template>

<script>
import EmptyLayout from '@/layouts/EmptyLayout'
import MainLayout from '@/layouts/MainLayout'
export default {
  computed: {
    layout() {
      return (this.$route.meta.layout || 'main') + '-layout'
    }
  },
  components: {
    EmptyLayout, MainLayout
  }
};
</script>

<style lang="scss">
@import "~bootstrap/dist/css/bootstrap.min.css";
@import '~@/assets/css/normalize.css';
@import '~@/assets/style.css';
@import '~@/assets/scss/style.scss';
</style>
