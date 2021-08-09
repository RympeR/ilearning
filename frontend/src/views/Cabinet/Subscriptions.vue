<template>
  <div class="subscribe container">
    <div class="row">
        <div class="col-4">
            <div class="subscribe-case start">
                <div class="case-name">Старт</div>
                <div class="case-price"><span class="case-price-value">Бесплатно</span></div>
                    <div class="case-action register-first"><a href="#">Выбрать</a></div>
                <div class="case-term">
                    <p>Вы будете перенаправлены на форму регистрации.</p>
                    <p><img src="@/assets/img/icons/checked.png"> Это Ваш текущий тарифный план.</p>
                </div>
                <div class="preferences">
                    <div class="tasks">
                        <h2>Развивающие задания</h2>
                        <p>Download incredible time-saving kindergarten, preschool and primary school teaching resources:</p>
                        <ul>
                            <li>1000 printable and digital resources to use in your classroom include worksheets, games, craft activities and more!</li>
                            <li>searchable by type, age, subject, programme and specific skill.</li>
                        </ul>
                    </div>
                    <div class="refs">
                        <h2>Справочные материалы</h2>
                        <p>Create your own brilliant lesson plans using ready online educational resources:</p>
                        <ul>
                            <li>add resources you like to the plan, rearrange them as you need and save your Lesson Plans online.</li>
                            <li>assign the lesson plan to the group of the student.</li>
                            <li>access all your Lesson Plans and all your groups and students any time you need in your personal cabinet.</li>
                        </ul>
                    </div>
                </div>
                <div class="case-action register-first"><a href="#">Выбрать</a></div>
            </div>
        </div>
        <div class="col-4">
            <div class="subscribe-case premium">
              <form method="post" action="">
                <div class="case-name">Премиум</div>
                <div class="case-price"><span class="case-price-value">100</span> грн/месяц</div>
                  <div class="case-action change-subscribe"><a href="">Выбрать</a></div>
                <div class="case-term">
                    <div class="term-selected">1 месяц <IconArrow /></div>
                    <div class="terms-available" style="display: none;">
                        <ul>
                            <li class="selected">1 месяц / 100 грн <IconArrow /></li>
                            <li>3 месяца / 285 грн / экономия 5%</li>
                            <li>6 месяцев / 540 грн / экономия 10%</li>
                            <li>1 год / 960 грн / экономия 20%</li>
                        </ul>
                    </div>
                </div>
                <div class="preferences">
                    <div class="tasks">
                        <h2>Развивающие задания</h2>
                        <p>Download incredible time-saving kindergarten, preschool and primary school teaching resources:</p>
                        <ul>
                            <li>1000 printable and digital resources to use in your classroom include worksheets, games, craft activities and more!</li>
                            <li>searchable by type, age, subject, programme and specific skill.</li>
                            <li>many ways to use: download PDF, add worksheets and activities to plans, create and share collections and more!</li>
                        </ul>
                    </div>
                    <div class="refs">
                        <h2>Справочные материалы</h2>
                        <p>Create your own brilliant lesson plans using ready online educational resources:</p>
                        <ul>
                            <li>add resources you like to the plan, rearrange them as you need and save your Lesson Plans online.</li>
                            <li>assign the lesson plan to the group of the student.</li>
                            <li>access all your Lesson Plans and all your groups and students any time you need in your personal cabinet.</li>
                        </ul>
                    </div>
                </div>
                    <div class="case-action change-subscribe"><a href="">Выбрать</a></div>
              </form>
            </div>
        </div>
        <div class="col-4">
            <div class="subscribe-case pro">
              <form method="post" action="">
                <div class="case-name">Профессионал</div>
                <div class="case-price"><span class="case-price-value">250</span> грн/месяц</div>
                    <div class="case-action change-subscribe"><a href="">Выбрать</a></div>
                <div class="case-term">
                    <div class="term-selected">1 месяц <IconArrow /></div>
                    <div class="terms-available" style="display: none;">
                        <ul>
                            <li class="selected">1 месяц / 250 грн <IconArrow /></li>
                            <li>3 месяца / 712,50 грн / экономия 5%</li>
                            <li>6 месяцев / 1350 грн / экономия 10%</li>
                            <li>1 год / 2400 грн / экономия 20%</li>
                        </ul>
                    </div>
                </div>
                <div class="preferences">
                    <div class="tasks">
                        <h2>Развивающие задания</h2>
                        <p>Download incredible time-saving kindergarten, preschool and primary school teaching resources:</p>
                        <ul>
                            <li>1000 printable and digital resources to use in your classroom include worksheets, games, craft activities and more!</li>
                            <li>searchable by type, age, subject, programme and specific skill.</li>
                            <li>many ways to use: download PDF, add worksheets and activities to plans, create and share collections and more!</li>
                        </ul>
                    </div>
                    <div class="cons">
                        <h2>Конструктор занятий</h2>
                        <p>Create your own brilliant lesson plans using ready online educational resources:</p>
                        <ul>
                            <li>add resources you like to the plan, rearrange them as you need and save your Lesson Plans online.</li>
                            <li>assign the lesson plan to the group of the student.</li>
                            <li>access all your Lesson Plans and all your groups and students any time you need in your personal cabinet.</li>
                        </ul>
                    </div>
                    <div class="refs">
                        <h2>Справочные материалы</h2>
                        <p>Create your own brilliant lesson plans using ready online educational resources:</p>
                        <ul>
                            <li>add resources you like to the plan, rearrange them as you need and save your Lesson Plans online.</li>
                            <li>assign the lesson plan to the group of the student.</li>
                            <li>access all your Lesson Plans and all your groups and students any time you need in your personal cabinet.</li>
                        </ul>
                    </div>
                </div>
                    <div class="case-action change-subscribe"><a href="">Выбрать</a></div>
              </form>
            </div>
        </div>
    </div>
    <div class="row feature-comparison">
        <div class="col-12">
            <h2>What do you get with your subscription?</h2>
            <h3>Feature Comparison</h3>
            <table>
                <thead>
                    <tr>
                        <th class="empty"></th>
                        <th class="premium">Premium</th>
                        <th class="pro">Professional</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Cost</td>
                        <td>100 UAH/month</td>
                        <td>250 UAH/month</td>
                    </tr>
                    <tr>
                        <td>Feature 1</td>
                        <td><img src="@/assets/img/icons/checked.png"></td>
                        <td><img src="@/assets/img/icons/checked.png"></td>
                    </tr>
                    <tr>
                        <td>Feature 2</td>
                        <td><img src="@/assets/img/icons/checked.png"></td>
                        <td><img src="@/assets/img/icons/checked.png"></td>
                    </tr>
                    <tr>
                        <td>Feature 3</td>
                        <td><img src="@/assets/img/icons/checked.png"></td>
                        <td><img src="@/assets/img/icons/checked.png"></td>
                    </tr>
                    <tr>
                        <td>Feature 4</td>
                        <td></td>
                        <td><img src="@/assets/img/icons/checked.png"></td>
                    </tr>
                    <tr>
                        <td>Feature 5</td>
                        <td></td>
                        <td><img src="@/assets/img/icons/checked.png"></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    <div class="row faq">
        <div class="col-12">
            <h2>Frequently Asked Questions</h2>
        </div>
        <div class="col-12">
            <div class="row">
                <div class="col-6 col-xs-12">
                    <section class="question-block">
                        <div class="question">
                            Can I cancel my subscription at any time?
                        </div>
                        <div class="answer">
                            Yes. If you ever decide that Teach Starter isn't the best educational teaching resource for your classroom or home, simply cancel your account from your profile page or contact us. Even after cancelling your subscription, you'll still have access to premium resources for the duration of your subscription year.
                        </div>
                    </section>
                    <section class="question-block">
                        <div class="question">
                            What is the duration of my subscription?
                        </div>
                        <div class="answer">
                            Subscription plans are for 12 months. You pay only one low fee for an entire year of access. Your subscription will automatically renew at the end of your subscription period; however, you can turn off auto-renewal at any time.
                        </div>
                    </section>
                </div>
                <div class="col-6 col-xs-12">
                    <section class="question-block">
                        <div class="question">
                            Can I change my subscription later on?
                        </div>
                        <div class="answer">
                            Absolutely! You can upgrade, downgrade or cancel your subscription at any time.
                        </div>
                    </section>
                    <section class="question-block">
                        <div class="question">
                            What are your download fees?
                        </div>
                        <div class="answer">
                            There are no additional download fees. Signing up for a subscription for one low fee gives you access to unlimited resources.
                        </div>
                    </section>
                    <section class="question-block">
                        <div class="question">
                            How do I pay for my subscription?
                        </div>
                        <div class="answer">
                            You can pay for your subscription securely via credit card or PayPal. You have total control over your account via our website and can cancel at any time, giving you security and peace-of-mind.
                        </div>
                    </section>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import IconArrow from '@/components/Icons/IconArrow.vue'

export default {
  name: 'subscriptions',
  components: {
    IconArrow
  }
}
</script>