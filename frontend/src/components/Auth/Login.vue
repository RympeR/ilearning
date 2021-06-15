<template>
  <Popup title="Log&nbsp;In">
    <form id="formLogin" action="test" method="post">
      <div class="fields info_person">
          <input
              v-model="email"
              type="email"
              class="login_name"
              name="email"
              placeholder="Username"
              required
              autofocus
          />
          <input
              v-model="password"
              type="password"
              class="login_pass"
              name="password"
              placeholder="Password"
              required
          />
      </div>
      <div class="alert alert-danger error-message" style="display:none;" role="alert">
      </div>
      <div class="return-pass">
          <a href="" class="popup-return-button" @click.prevent="tooglePopupContent('restore')">Forgot your password?</a>
      </div>
      <div class="register-in">
          <input type="submit" class="active_popup" value="Log&nbsp;In" @click.prevent="doLogin">
          <div>
          <a href="" class="popup-register-button disable_popup" @click.prevent="tooglePopupContent('register')">Sign Up</a>
          </div>
      </div>
    </form>
  </Popup>
</template>

<script>
import Popup from '@/components/Popup'
import {mapActions} from 'vuex'

export default {
    name: "login",
    data() {
        return {
            email: '',
            password: '',
        }
    },
    components: {
      Popup
    },
    methods: {
      ...mapActions([
        'SET_POPUP_CONTENT', 'TOOGLE_POPUP'
      ]),
      tooglePopupContent(content) {
        this.SET_POPUP_CONTENT(content)
      },
      doLogin() {
        let username = this.email;
        let password = this.password;
        this.$store.dispatch('LOGIN', {username, password})
          .then(() => {
              this.TOOGLE_POPUP()
          })
          .catch(response => {
              console.log(response)
          })
      }
    }
}
</script>
