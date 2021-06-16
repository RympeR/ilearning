import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    isPopupActive: false,
    popupContent: 'login',
    status: '',
    token: localStorage.getItem('token') || null
  },
  mutations: {
    CHANGE_POPUP: (state) => {
      state.isPopupActive = !state.isPopupActive
    },
    CHANGE_CONTENT: (state, content) => {
      state.popupContent = content
    },
    AUTH_REQUEST(state) {
      state.status = 'loading'
    },
    AUTH_SUCCESS(state, token) {
      state.status = 'success';
      state.token = token
    },
    AUTH_ERROR(state) {
      state.status = 'error'
    },
    LOGOUT(state) {
      state.status = ''
      state.token = null
    }
  },
  actions: {
    TOOGLE_POPUP({commit}) {
      commit('CHANGE_POPUP')
    },
    SET_POPUP_CONTENT({commit}, content) {
      commit('CHANGE_CONTENT', content)
    },
    LOGIN({commit}, user) {
      return new Promise((resolve, reject) => {
        commit('AUTH_REQUEST')
        let formData = new FormData();
        Object.keys(user).map(function (key) {
            if (user[key]) {
              formData.append(key, user[key])
            }
        });
        axios.post(process.env.VUE_APP_BACKEND_HOST + '/auth/token/login/', formData)
        .then(response => {
            const token = response.data.auth_token
            localStorage.setItem('token', token);
            axios.defaults.headers.common['Authorization'] = token;
            commit('AUTH_SUCCESS', token);
            resolve(response)
        })
        .catch(response => {
            commit('AUTH_ERROR');
            localStorage.removeItem('token');
            reject(response)
        })
      })
    },
    LOGOUT({commit}){
      return new Promise((resolve) => {
        commit('LOGOUT');
        localStorage.removeItem('token');
        delete axios.defaults.headers.common['Authorization'];
        resolve();
      })
    },
  },
  getters: {
    POPUP_STATE: (state) => state.isPopupActive,
    POPUP_CONTENT: (state) => state.popupContent,
    IS_LOGGED_IN: state => !!state.token,
    AUTH_STATUS: (state) => state.status,
    GET_TOKEN: (state) => state.token
  },
  modules: {
  }
})
