<template>
  <Popup title="Регистрация">
    <form id="formRegister" action="register" method="post">
              <div class="fields info_person">
                <input type="text" class="login_name" name="email" placeholder="Логин" value="{{ old('email') }}" required>
                <input type="password" class="login_pass" name="password" placeholder="Пароль" required>
              </div>
              <div class="privacy_policy_check">
                <label class="checkbox">
                  <input type="checkbox" id="ageConfirm" name="age">
                  <div class="check-info">Вам должно быть 13 или больше, чтобы продолжить.<br> Пожалуйста, подтвердите свой возраст</div>
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
                  <input type="checkbox" id="rulesConfirm" name="rules">
                  <div class="check-info">Согласие с правилами</div>
                </label>
                <label class="checkbox">
                  <input type="checkbox" id="subscribeConfirm" name="subscribe">
                  <div class="check-info">Согласие на получение e-mail</div>
                </label>
              </div>
    </form>
  </Popup>
</template>

<script>
import Popup from "@/components/Popup"
import {mapActions} from 'vuex'

export default {
    name: "register",
    components: {
      Popup
    },
    methods: {
      ...mapActions([
        'SET_POPUP_CONTENT'
      ]),
      tooglePopupContent(content) {
        this.SET_POPUP_CONTENT(content)
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
    }
  }
</style>