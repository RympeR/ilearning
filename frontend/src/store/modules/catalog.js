import axios from 'axios'

const state = () => ({
    items: {},
    current_item: {},
    filters: {},
    filtered_items: {},
    current_page: 1
})

const mutations = {
    SET_ITEMS(state, items) {
      state.items = items
    },
    SET_CURRENT_ITEM(state, item) {
      state.current_item = item
    },
    ADD_FILTER(state, item) {
      if(state.filters[item.section]) {
        state.filters[item.section].push(item.id)
      } else {
        state.filters[item.section] = [item.id]
      }
    },
    REMOVE_FILTER(state, item) {
      let itemToRemove = state.filters[item.section].indexOf(item.id)
      state.filters[item.section].splice(itemToRemove, 1)
    },
    SET_FILTERED(state, items) {
      state.filtered_items = items
    },
    SET_CURRENT_PAGE(state, page) {
      state.current_page = page
    }
}

const actions = {
  RECEIVE_ITEMS({commit, dispatch}) {
    return new Promise((resolve, reject) => {
      axios.get('/lessons/card-filtered/')
      .then(response => {
        let items = response.data.results
        commit('SET_ITEMS', items)
        dispatch('FILTER_ITEMS')
        resolve(response)
      })
      .catch(error => {
        console.log(error.response)
        reject(error)
      })
    })
  },
  RECEIVE_CURRENT_ITEM({commit}, id) {
    return new Promise((resolve, reject) => {
      axios.get('/lessons/card-get/' + id)
      .then(response => {
        let item = response.data
        commit('SET_CURRENT_ITEM', item)
        resolve(response)
      })
      .catch(error => {
        console.log(error.response)
        reject(error)
      })
    })
  },
  CHANGE_FILTER({commit, dispatch}, item) {
    if(item.checked) {
      commit('ADD_FILTER', item)
    } else {
      commit('REMOVE_FILTER', item)
    }
    dispatch('FILTER_ITEMS')
  },
  FILTER_ITEMS({ commit, getters }) {
    let items = getters['GET_ITEMS']
    let filters = getters['GET_FILTERS']
    let itemsFiltered = items.filter(item => {
      let matched = {}
      Object.keys(filters).map((key) => {
        matched[key] = false
        if(key === 'card_type') { // For section "card types"
          // If type of current card is accepted by filter
          if(filters[key].indexOf(item[key].id) > -1 || filters[key].length == 0) {
            matched[key] = true // then card matched to conditions, we can show it
          }
        } else { // For all other sections (exclude "card types")
          item[key].map((elem) => { // Get each element in card
            // If at least one of it is accepted by filter
            if(filters[key].indexOf(elem.id) > -1 || filters[key].length == 0) {
              matched[key] = true // then card matched to conditions, we can show it
            }
          })
        }
      })
      let totalMatched = true
      Object.keys(matched).map((key) => {
        if(!matched[key]) {
          totalMatched = false
        }
      })
      return totalMatched
    })
    commit('SET_FILTERED', itemsFiltered)
  }
}

const getters = {
  GET_ITEMS: (state) => state.items,
  GET_CURRENT_ITEM: (state) => state.current_item,
  GET_FILTERS: (state) => state.filters,
  GET_FILTERED: (state) => state.filtered_items,
  GET_CURRENT_PAGE: (state) => state.current_page
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
