<template>
<ul class="switch-arrow">
  <li v-for="link in links" :key="link.url">
    <localized-link :to="link.url" active-class="active">{{link.title}}</localized-link>
    <ul v-if="link.links">
      <li v-for="sublink in link.links" :key="sublink.url">
        <localized-link :to="sublink.url" active-class="active">{{sublink.title}}</localized-link>
      </li>
    </ul>
  </li>
</ul>
</template>

<script>
export default {
  name: "header-menu",
  data: () => ({
    links: [
      { 
        title: 'Educational Resources',
        url: '/catalog',
        links: [
          { title: 'Пункт меню', url: '/'},
          { title: 'Пункт меню', url: '/'},
          { title: 'Пункт меню', url: '/'}
        ]
      },
      {
        title: 'Lesson Plan Maker',
        url: '/',
        links: [
          { title: 'Пункт меню', url: '/'},
          { title: 'Пункт меню', url: '/'},
          { title: 'Пункт меню', url: '/'}
        ]
      },
      {
        title: 'Teacher Resources',
        url: '/',
        links: [
          { title: 'Пункт меню', url: '/'},
          { title: 'Пункт меню', url: '/'},
          { title: 'Пункт меню', url: '/'}
        ]
      }
    ]
  })
}
</script>