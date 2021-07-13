<template>
<div>
  <div class="global-wrapper">
    <header>
      <div class="header-wrap">
        <div class="container">
          <div class="header">
            <div class="row menu-header">
              <div class="logo col-6 col-md-7 col-sm-6">
                <router-link to="/catalog"><img src="@/assets/img/icons/logo.png" alt="iLearning Tools"></router-link>
              </div>
              <div class="menu-list col-10 col-md-5">
                <HeaderMenu />
              </div>
              <div class="search-admin serch-app-j search col-2">
                <form action="/" method="get">
                  <input type="submit" alt="Search" class="butn-search" value=" " />
                  <input type="text" name="s" id="search" class="inp-search" value="" placeholder="Search" />
                </form>
              </div>
              <div class="search-admin lang col-2 col-md-2 col-lg-1">
                <div class="lang-switcher switcher">
                  <ul class="switch-arrow">
                    <li><a href="">En</a>
                      <ul>
                        <li><a href="">Ru</a></li>
                        <li><a href="">Ua</a></li>
                      </ul>
                    </li>
                  </ul>
                </div>
              </div>
              <div class="search-admin col-2 col-md-2 col-lg-1">
                <div class="lk-switcher switcher">
                  <ul class="switch-arrow">
                    <li>
                      <a href="#" v-if="!IS_LOGGED_IN" class="enter-lk" @click.prevent="showLogin">Log&nbsp;In</a>
                      <a href="" v-if="IS_LOGGED_IN" class="lk-admin">Личный кабинет</a>
                      <ul v-if="IS_LOGGED_IN">
                        <li><router-link :to="{name: 'profile'}">{{ GET_USERNAME }}</router-link></li>
                        <li><a class="disabled" href="">Настройки</a></li>
                        <li><a class="disabled" href="">Мои занятия</a></li>
                        <li><a class="disabled" href="">Мои группы</a></li>
                        <li><router-link :to="{name: 'collections'}">Мои коллекции</router-link></li>
                        <li><router-link :to="{name: 'purchases'}">Мои покупки</router-link></li>
                        <li><a class="disabled" href="">Уведомления</a></li>
                        <li><a class="disabled" href="">Сообщения</a></li>
                        <li><a href="" @click.prevent="doLogout">Logout</a></li>
                      </ul>
                    </li>
                  </ul>
                </div>
              </div>
              <div class="col-md-1 col-2 burger-m">
                <div class="nav-buttons">
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="sale-wrapp">
        <div class="container">
          <div class="row align-items-center">
            <div class="col-lg-8 col-md-8 col-sm-8 sale-info">
              <h1>Уже в ноябре запуск Конструктора занятий!</h1>
            </div>
            <div class="col-lg-2 col-md-4 col-sm-4 col-7 button-header">
              <a href="" class="green-hov">More details</a>
            </div>
          </div>
        </div>
      </div>
      <div class="search-bg">
        <div class="container">
          <div class="search-app search-admin"></div>
        </div>
      </div>
    </header>
    <main>
      <router-view/>
    </main>
    <footer>
      <section class="menu-footer-section">
        <FooterMenu />
      </section>
      <section class="footer-info">
        <div class="container">
          <div class="row">
            <div class="col-lg-3 col-md-6 col-sm-12 social order-md-2">
              <p>МЫ В СОЦСЕТЯХ</p>
              <ul class="social-list">
                <li>
                  <a href="https://www.facebook.com/groups/ilearning.tools/" target="_blank" title="Facebook">
                    <img src="@/assets/img/icons/face.png" alt="Facebook">
                  </a>
                </li>
                <li>
                  <a href="https://pinterest.com/ilearningtools/" target="_blank" title="Pinterest">
                    <img src="@/assets/img/icons/pin.png" alt="Pinterest">
                  </a>
                </li>
                <li>
                  <a href="" target="_blank" title="Youtube">
                    <img src="@/assets/img/icons/you.png" alt="Youtube">
                  </a>
                </li>
                <li>
                  <a href="https://www.instagram.com/ilearning.tools/" target="_blank" title="Instagram">
                    <img src="@/assets/img/icons/inst.png" alt="Instagram">
                  </a>
                </li>
              </ul>
            </div>
            <div class="logo col-lg-3 col-md-6 col-sm-6 col-6 order-md-1">
              <div class="logo-footer">
                <router-link to="/catalog"><img src="@/assets/img/icons/logo.png" alt="logo"></router-link>
              </div>
              <div class="copy">
                <p>Copyright © 2021 iLearning.tools</p>
              </div>
            </div>
            <div class="col-lg-2 col-md-4 col-sm-6 col-6 privacy order-md-3">
              <div class="img">
                <a href="http://deti-budushego.com/" target="_blank" title="Дети будущего"><img src="@/assets/img/prava.jpg" alt="Дети будущего"></a>
              </div>
              <p>Все права защищены ® </p>
            </div>
            <div class="col-lg-2 col-md-4 col-sm-6 col-6 order-md-3">
              <div class="pay">
                <div class="visa"><img src="@/assets/img/visa.png" alt=""></div>
                <div class="mastercard"><img src="@/assets/img/visa-mastercard.png" alt=""></div>
              </div>
            </div>
            <div class="col-lg-2 col-md-4 col-sm-6 col-6 p-kam order-md-3">
              <p>Powered by </p>
              <div class="kam">
                <a href="http://akaminsky.com/" title="A. Kaminsky Studio" target="_blank"><img src="@/assets/img/kam.png" alt="A. Kaminsky Studio"></a>
              </div>
            </div>   
          </div>
        </div>
      </section>
    </footer>
  </div>
  <AuthDialogs />
</div>
</template>

<script>
import HeaderMenu from '@/components/Common/HeaderMenu'
import FooterMenu from '@/components/Common/FooterMenu'
import AuthDialogs from '@/components/Auth/AuthDialogs'
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'main-layout',
  components: {
    HeaderMenu, FooterMenu, AuthDialogs
  },
  computed: {
    ...mapGetters([
      'POPUP_STATE', 'IS_LOGGED_IN', 'GET_USERNAME'
    ])
  },
  methods: {
    ...mapActions([
      'TOOGLE_POPUP', 'SET_POPUP_CONTENT', 'LOGOUT'
    ]),
    showLogin() {
      this.SET_POPUP_CONTENT('login')
      this.TOOGLE_POPUP()
    },
    doLogout() {
      this.LOGOUT()
    }
  }
}
</script>