<template>
  <div class="lang-switcher switcher">
    <language-switcher v-slot="{ links }" tag="ul" active-class="switch-arrow">
      <li>

        <a href="">{{ $i18n.locale }}</a>
        <ul>
          <li :class="link.activeClass" v-for="link in links" :key="link.langIndex" @click.prevent="switchLang(link.langIndex)">
            <a :href="link.url" >{{ link.langIndex }}</a>
          </li>
        </ul>
      </li>
  </language-switcher>
  </div>
</template>

<script>
export default {
  name: "LangSelector",
  computed: {
    locales: function () {
      return process.env.VUE_APP_I18N_SUPPORTED_LOCALE.split(",").filter(
        (item) => {
          return item !== this.$i18n.locale;
        }
      );
    },
  },
  methods: {
    switchLang(locale) {
      if (this.$i18n.locale !== locale) {
        this.$i18n.locale = locale.toLowerCase();
      }
    },
  },
};
</script>