export default {
    en: {
      name: 'English',
      load: () => { return import('./en.json'); },
    },
    ru: {
      name: 'Russian',
      load: () => { return import('./ru.json'); },
    },
    ua: {
      name: 'Ukrainian',
      load: () => { return import('./ua.json'); },
    },
  };