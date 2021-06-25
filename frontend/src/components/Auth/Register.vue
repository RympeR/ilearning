<template>
  <Popup title="Регистрация" @popupClosed="v$.$reset()">
    <form id="formRegister" @submit.prevent="doRegister" v-if="!showResults">
              <div class="fields info_person">
                <small
                  class="error-message invalid"
                  v-if="v$.username.$dirty && v$.username.required.$invalid"
                >
                  Поле "E-mail" не должно быть пустым
                </small>
                <small
                  class="error-message invalid"
                  v-if="v$.username.$dirty && v$.username.email.$invalid"
                >
                  Введите корректный e-mail
                </small>
                <input
                  v-model.trim="username"
                  type="text"
                  class="login_name"
                  :class="{ invalid: (v$.username.$dirty && v$.username.required.$invalid) || (v$.username.$dirty && v$.username.email.$invalid) }"
                  name="username"
                  placeholder="E-mail"
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
                  :class="{ invalid: v$.password.$dirty && v$.password.required.$invalid }"
                  name="password"
                  placeholder="Пароль"
                />
              </div>
              <div class="privacy_policy_check">
                <label class="checkbox">
                  <input
                    v-model="age"
                    type="checkbox"
                    :class="{ invalid: v$.age.$dirty && v$.age.$invalid}"
                    id="ageConfirm"
                    name="age"
                  />
                  <div
                    class="check-info"
                    :class="{ invalid: v$.age.$dirty && v$.age.$invalid}"
                  >
                    Вам должно быть 13 или больше, чтобы продолжить.<br> Пожалуйста, подтвердите свой возраст
                  </div>
                </label>
              </div>
              <div class="alert alert-danger register-errors" style="display:none;" role="alert">
              </div>
              <div class="register-in">
                <input type="submit" class="active_popup" value="Регистрация">
                <div>
                  <a href="" class="popup-log_in-button disable_popup" @click.prevent="tooglePopupContent('login')">Вход</a>
                </div>
              </div>
              <div class="info_terms">
                <label class="checkbox">
                  <input
                    v-model="rules"
                    type="checkbox"
                    :class="{ invalid: v$.rules.$dirty && v$.rules.$invalid}"
                    id="rulesConfirm"
                    name="rules">
                  <div
                    class="check-info"
                    :class="{ invalid: v$.rules.$dirty && v$.rules.$invalid}"
                  >
                    Согласие с правилами
                  </div>
                </label>
                <label class="checkbox">
                  <input type="checkbox" id="subscribeConfirm" name="subscribe">
                  <div class="check-info">Согласие на получение e-mail</div>
                </label>
              </div>
    </form>
    <p class="success-message" v-if="showResults">Поздравляем! Вы успешно зарегистрировались. Теперь можете <a href="" @click.prevent="tooglePopupContent('login')">войти</a>.</p>
  </Popup>
</template>

<script>
import Popup from "@/components/Popup"
import {mapActions} from 'vuex'
import { required, email } from '@vuelidate/validators'
import { useVuelidate } from '@vuelidate/core'

const mustBeChecked = (value) => { return value }

export default {
    name: "register",
    setup: () => ({ v$: useVuelidate() }),
    data: () => ({
      username: '',
      password: '',
      age: false,
      rules: false,
      showResults: false
    }),
    validations () {
      return {
        username: { required, email },
        password: {required},
        age: { required, mustBeChecked },
        rules: {required, mustBeChecked},
      }
    },
    components: {
      Popup
    },
    methods: {
      ...mapActions([
        'SET_POPUP_CONTENT'
      ]),
      tooglePopupContent(content) {
        this.SET_POPUP_CONTENT(content)
      },
      doRegister() {
        if (this.v$.$invalid) {
          this.v$.$touch()
          return
        }
        let username = this.username
        let password = this.password
        this.$store.dispatch('REGISTER', {username, password})
          .then(() => {
            this.showResults = true
          })
          .catch(error => {
              console.log(error.response.data)
          })
      }
    }
}
</script>

<style lang="scss">
  .popup {
    .privacy_policy_check {
      margin-bottom: 35px;
      
      input {
        min-width: 30px;
        min-height: 30px;
      }
    }
    .info_terms {
      input {
        min-width: 30px;
        min-height: 30px;
      }
    }
    .check-info {
      padding-left: 15px;
      font-size: 15px;
      line-height: 1;
      color: #464646;

      &.invalid {
        color: red;
      }
    }
  }
</style>