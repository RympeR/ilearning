<template>
  <Popup title="Restore password">
    <form id="formReset" action="test" method="post">

      <div class="fields info_person">
        <input type="email" class="login_email" name="email" placeholder="Email" required autofocus>
      </div>
      <div class="alert alert-info" style="display:none;" role="alert"></div>
      <div class="register-in">
        <input type="submit" class="active_popup" value="Restore password">
      </div>
    </form>
  </Popup>
</template>

<script>
import Popup from "@/components/Popup"

export default {
  name: "restore",
  components: {
    Popup
  }
}
</script>