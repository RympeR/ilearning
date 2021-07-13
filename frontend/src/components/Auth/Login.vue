<template>
  <Popup title="Log&nbsp;In" @popupClosed="v$.$reset()">
    <form id="formLogin" @submit.prevent="doLogin">
      <div class="fields info_person">
          <small
            class="error-message invalid"
            v-if="v$.username.$dirty && v$.username.required.$invalid"
          >
            Поле "Логин" не должно быть пустым
          </small>
          <input
              v-model.trim="username"
              type="text"
              class="login_name"
              :class="{ invalid: v$.username.$dirty && v$.username.required.$invalid }"
              name="username"
              placeholder="Username"
              autofocus
          />
          <small
            class="error-message invalid"
            v-if="v$.password.$dirty && v$.password.required.$invalid"
          >
            Поле "Пароль" не должно быть пустым
          </small>
          <input
              v-model.trim="password"
              type="password"
              class="login_pass"
              :class="{ invalid: v$.password.$dirty && v$.password.required.$invalid}"
              name="password"
              placeholder="Password"
          />
      </div>
      <div class="alert alert-danger error-message" style="display:none;" role="alert">
      </div>
      <div class="return-pass">
          <a href="" class="popup-return-button" @click.prevent="tooglePopupContent('restore')">Forgot your password?</a>
      </div>
      <div class="register-in">
          <input type="submit" class="active_popup" value="Log&nbsp;In">
          <div>
          <a href="" class="popup-register-button disable_popup" @click.prevent="tooglePopupContent('register')">Sign Up</a>
          </div>
      </div>
    </form>
  </Popup>
</template>

<script>
import Popup from '@/components/Common/Popup'
import {mapActions} from 'vuex'
import { required } from '@vuelidate/validators'
import { useVuelidate } from '@vuelidate/core'

export default {
    name: "login",
    setup: () => ({ v$: useVuelidate() }),
    data: () => ({
      username: '',
      password: ''
    }),
    validations () {
      return {
        username: {required},
        password: {required}
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
        if (this.v$.$invalid) {
          this.v$.$touch()
          return
        }
        let username = this.username
        let password = this.password
        this.$store.dispatch('LOGIN', {username, password})
          .then(() => {
              this.TOOGLE_POPUP()
          })
          .catch(error => {
              console.log(error.response.data)
          })
      }
    }
}
</script>
