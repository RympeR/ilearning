<template>
<div v-if="!IS_LOGGED_IN">
    <Login v-if="POPUP_CONTENT == 'login'" />
    <Register v-if="POPUP_CONTENT == 'register'" />
    <Restore v-if="POPUP_CONTENT == 'restore'" />
</div>
</template>

<script>
import Login from '@/components/Auth/Login'
import Register from '@/components/Auth/Register'
import Restore from '@/components/Auth/Restore'
import {mapGetters} from 'vuex'

export default {
  name: 'auth-dialogs',
  components: {
    Login, Register, Restore
  },
  computed: {
    ...mapGetters([
      'POPUP_CONTENT', 'IS_LOGGED_IN'
    ])
  }
}
</script>
