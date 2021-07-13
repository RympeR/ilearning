<template>
  <div class="popup-block" :class="(POPUP_STATE)? 'popup-active' : '' ">
    <div class="popup-container">
      <div class="popup">
        <div class="popup-close" @click="hidePopup"></div>

        <div class="popup-content">
          <h2>{{ title }}</h2>
          <slot></slot>
          <div class="notification-message">{{GET_ERROR}}</div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters,mapActions} from 'vuex'

export default {
  name: "popup",
  props: ['title'],
  computed: {
    ...mapGetters([
      'POPUP_STATE', 'GET_ERROR'
    ])
  },
  methods: {
    ...mapActions([
      'TOOGLE_POPUP'
    ]),
    hidePopup() {
      this.TOOGLE_POPUP()
      this.$emit('popupClosed')
    }
  }
}
</script>

<style lang="scss">
  .popup-block {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(49, 98, 162, 0.67);
    opacity: 0;
    z-index: 9999;

    &.popup-active {
      display: block;
      opacity: 1;
    }
  }
  .popup-container {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-pack: center;
        -ms-flex-pack: center;
            justify-content: center;
    -webkit-box-align: center;
        -ms-flex-align: center;
            align-items: center;
    margin: 1%;
  }
  .popup {
    position: relative;
    padding: 95px 75px 80px 75px;
    max-width: 690px;
    width: 100%;
    background-color: #f6f7f2;

    h2, p {
      font-size: 35px;
      font-weight: 700;
      color: #464646;
      margin-bottom: 30px;
    }

    p.success-message {
      color: #009845;
      font-size: 20px;
    }

    .fields {
      input {
        width: 100%;
        border: 1px solid #cacbc6;
        background-color: #ffffff;
        margin-bottom: 25px;
        padding: 25px 20px;
        color: #3a3b36;
        font-size: 20px;

        &::placeholder {
          color: #8a8a8a;
        }
        &::-webkit-input-placeholder {
          color: #8a8a8a;
        }
        &::-moz-placeholder {
          color: #8a8a8a;
        }
        &:-ms-input-placeholder {
          color: #8a8a8a;
        }
        &:-moz-placeholder {
          color: #8a8a8a;
        }
      }
    }

    .register-in > div {
      height: 56px;
      text-align: center;
      margin-left: auto;
    }

    .active_popup {
      background-color: #009845;
      border: 1px solid #009845!important;
      padding: 13px 60px 15px;
      border: none;
      font-size: 23px;
      font-family: "Museo Sans", sans-serif;
      color: #fff;
      font-weight: 700;
      transition: 0.4s;

      &:hover {
        background-color: #ffffff;
        color: #009845;
        border: 1px solid #009845!important;
      }
    }

    .disable_popup {
      border: 1px solid #ff7600;
      background-color: #ffffff;
      transition: 0.4s;
      color: #ff7600;
      padding: 12px 55px;
      font-size: 23px;
      font-family: "Museo Sans", sans-serif;
      font-weight: 700;
      display: block;
      line-height: 30px;

      &:hover {
        background-color: #ff7600;
        color: #fff;
        border: 1px solid #ff7600;
      }
    }

    .actions {
      input {
        padding-left: 40px;
        padding-right: 40px;
      }
      a.active_popup {
        border-radius: 0;
        line-height: 26.45px;
        padding-left: 30px;
        padding-right: 30px;
      }
      .disable_popup {
        float: right;
      }
    }

    .invalid {
      color: red;
    }
    input.invalid {
      border-color: red;
    }
  }
  .popup-close,
  .popup-close:after,
  .popup-close:before {
    position: absolute;
    content: '';
  }
  .popup-close {
    top: 35px;
    right: 25px;
    width: 19px;
    height: 19px;
    cursor: pointer;
  }

  .checkbox {
    display: flex;
    align-items: center;
    margin-bottom: .5rem;
  }

  .check-info {
    padding-left: 10px;

    a {
      color: #464646;
    }
  }

</style>