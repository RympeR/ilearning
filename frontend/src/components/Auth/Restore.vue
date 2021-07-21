<template>
  <Popup title="Restore password" @popupClosed="v$.$reset()">
    <form id="formReset" @submit.prevent="doRestore" v-if="!showResults">

      <div class="fields info_person">
        <small
          class="error-message invalid"
          v-if="v$.email.$dirty && v$.email.required.$invalid"
        >
          Поле "E-mail" не должно быть пустым
        </small>
        <small
          class="error-message invalid"
          v-if="v$.email.$dirty && v$.email.email.$invalid"
        >
          Введите корректный e-mail
        </small>
        <input
          v-model="email"
          type="text"
          class="login_email"
          :class="{ invalid: (v$.email.$dirty && v$.email.required.$invalid) || (v$.email.$dirty && v$.email.email.$invalid) }"
          name="email"
          placeholder="Email"
          autofocus
        />
      </div>
      <div class="alert alert-info" style="display:none;" role="alert"></div>
      <div class="register-in">
        <input type="submit" class="active_popup" value="Restore password">
      </div>
    </form>
    <p class="success-message" v-if="showResults">Инструкции для сброса пароля отправлены на {{email}}. Проверьте почту.</p>
  </Popup>
</template>

<script>
import Popup from "@/components/Common/Popup"
import { required, email } from '@vuelidate/validators'
import { useVuelidate } from '@vuelidate/core'

export default {
  name: "restore",
  setup: () => ({ v$: useVuelidate() }),
  data: () => ({
    email: '',
    showResults: false
  }),
  validations () {
    return {
      email: { required, email }
    }
  },
  components: {
    Popup
  },
  methods: {
    doRestore() {
      if (this.v$.$invalid) {
        this.v$.$touch()
        return
      }
      let email = this.email
      this.$store.dispatch('PASSWORD_RESTORE', email)
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