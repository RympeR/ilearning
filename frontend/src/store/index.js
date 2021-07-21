import { createStore } from 'vuex'
import axios from 'axios'

import catalog from './modules/catalog'

export default createStore({
  state: {
    isPopupActive: false,
    popupContent: 'login',
    status: '',
    error: '',
    token: localStorage.getItem('token') || null,
    username: localStorage.getItem('username') || null,
  },
  mutations: {
    CHANGE_POPUP: (state) => {
      state.isPopupActive = !state.isPopupActive
      state.error = ''
    },
    CHANGE_CONTENT: (state, content) => {
      state.popupContent = content
    },
    AUTH_REQUEST(state) {
      state.status = 'loading'
    },
    AUTH_SUCCESS(state, token) {
      state.status = 'success'
      state.token = token
    },
    AUTH_ERROR(state, error) {
      state.status = 'error'
      state.error = error.response.data.non_field_errors ? error.response.data.non_field_errors[0] : 'Some error'
    },
    REGISTER_SUCCESS(state) {
      state.status = 'success'
    },
    LOGOUT(state) {
      state.status = ''
      state.token = null
    },
    SET_USERNAME(state, username) {
      state.username = username
    }
  },
  actions: {
    TOOGLE_POPUP({commit}) {
      commit('CHANGE_POPUP')
    },
    SET_POPUP_CONTENT({commit}, content) {
      commit('CHANGE_CONTENT', content)
    },
    LOGIN({commit, dispatch}, user) {
      return new Promise((resolve, reject) => {
        commit('AUTH_REQUEST')
        let formData = new FormData()
        Object.keys(user).map(function (key) {
            if (user[key]) {
              formData.append(key, user[key])
            }
        })
        axios.post('/auth/token/login/', formData)
        .then(response => {
            const token = 'Token ' + response.data.auth_token
            localStorage.setItem('token', token)
            axios.defaults.headers.common['Authorization'] = token
            commit('AUTH_SUCCESS', token)
            dispatch('USER_INFO')
            resolve(response)
        })
        .catch(error => {
            commit('AUTH_ERROR', error)
            localStorage.removeItem('token')
            reject(error)
        })
      })
    },
    LOGOUT({commit}){
      return new Promise((resolve, reject) => {
        axios.post('/auth/token/logout/')
        .then(response => {
          commit('LOGOUT')
          localStorage.removeItem('token')
          delete axios.defaults.headers.common['Authorization']
          resolve(response)
        })
        .catch(error => {
          commit('AUTH_ERROR', error)
          reject(error)
        })
      })
    },
    REGISTER({commit}, user){
      return new Promise((resolve, reject) => {
        commit('AUTH_REQUEST')
        let formData = new FormData()
        Object.keys(user).map(function (key) {
            if (user[key]) {
              formData.append(key, user[key])
            }
        })
        axios.post('/auth/users/', formData)
        .then(response => {
            commit('REGISTER_SUCCESS')
            resolve(response)
        })
        .catch(error => {
            commit('AUTH_ERROR', error)
            reject(error)
        })
      })
    },
    PASSWORD_RESTORE({commit}, email){
      return new Promise((resolve, reject) => {
        commit('AUTH_REQUEST')
        let formData = new FormData()
        formData.append('email', email)
        axios.post('/auth/users/reset_password/', formData)
        .then(response => {
            commit('REGISTER_SUCCESS')
            resolve(response)
        })
        .catch(error => {
            commit('AUTH_ERROR', error)
            reject(error)
        })
      })
    },
    USER_INFO({commit}){
      return new Promise((resolve, reject) => {
        axios.get('/auth/users/me/')
        .then(response => {
          let username = response.data.username
          localStorage.setItem('username', username)
          commit('SET_USERNAME', username)
          resolve(response)
        })
        .catch(error => {
          console.log(error.response.data)
          reject(error)
        })
      })
    }
  },
  getters: {
    POPUP_STATE: (state) => state.isPopupActive,
    POPUP_CONTENT: (state) => state.popupContent,
    IS_LOGGED_IN: state => !!state.token,
    AUTH_STATUS: (state) => state.status,
    GET_TOKEN: (state) => state.token,
    GET_ERROR: (state) => state.error,
    GET_USERNAME: (state) => state.username
  },
  modules: {
    catalog
  },
  plugins: [
    (store) => {
      if(store.state.token) {
        axios.defaults.headers.common['Authorization'] = store.state.token
      }
      axios.defaults.baseURL = process.env.VUE_APP_BACKEND_HOST
    }
  ]
})
