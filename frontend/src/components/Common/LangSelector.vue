<template>
  <div class="lang-switcher switcher">
    <ul class="switch-arrow">
    <li><a href="">{{ $i18n.locale }}</a>
      <ul>
        <li
          v-for="locale in locales"
          :key="locale"
          @click.prevent="switchLang(locale)"
        >
          <a href="">
            {{locale}}
          </a>
        </li>
      </ul>
    </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "LangSelector",
  computed: {
    locales: function() {
      return process.env.VUE_APP_I18N_SUPPORTED_LOCALE.split(',').filter(item => {
        return item !== this.$i18n.locale
      })
    }
  },
  methods: {
    switchLang(locale) {
      if(this.$i18n.locale !== locale) {
        this.$i18n.locale = locale
      }
    }
  }
}
</script>