<template>
  <div class="paddingSides fixed">
    <div class="vspace"></div>
    <div style="height: 100%">
      <div class="four columns">
        <button class="button-primary" @click="sendForm">Send!</button>
        <!--<ol>-->
          <!--<li>-->
            <!--<span class="sidebarHeading">Question 1</span>-->
            <!--<ul>-->
              <!--<li v-for="a in array">: {{a}}</li>-->
            <!--</ul>-->
          <!--</li>-->
        <!--</ol>-->
      </div>
      <form class="eight columns vscroll">
        <!--Q1-->
        <div class="row">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">1) Are you a male or a female?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="six columns">
              <label for="male">Male</label>
              <input v-model="q_1" value="male" id='male' type="radio" />
            </div>
            <div class="six columns">
              <label for="female">Female</label>
              <input v-model="q_1" value="female" id='female' type="radio" />
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q2-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">2) How often do you watch CITY soccer championships?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_2" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q3-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">3) How often do you watch COUNTRY soccer championships?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_3" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q4-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">4) How often do you watch UEFA Champions League?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_4" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q5-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">5) How often do you watch FIFA Club World Cup?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_5" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q6-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">6) How often do you watch FIFA World Cup?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_6" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q7-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">7) How willing are you to travel to a different city/state to see a National Championship (Your country)?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_7" class="u-full-width">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q8-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">8) How willing are you to travel to a different city/state to see a UEFA Champions League?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_8" class="u-full-width">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q9-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">9) How willing are you to travel to a different city/state to see a FIFA Club World Cup?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_9" class="u-full-width">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>
        <!--Q10-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">10) How willing are you to travel to a different city/state to see a FIFA World Cup?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_10" class="u-full-width">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q11-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">11) Do you prefer to watch the whole game or only the highlights?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_11" class="u-full-width">
                <option value="whole">Whole game</option>
                <option value="highlights">Highlights</option>
                <option value="np">No preference</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q12-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">
                Do you prefer to watch live streaming or a replay later?
              </span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_12" class="u-full-width">
                <option value="live">Live</option>
                <option value="replay">Replay</option>
                <option value="np">No preference</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q13-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">13)Evaluate how often you use TV for watching soccer?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_13" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q14-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">14) Evaluate how often you use computer for watching soccer?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_14" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q15-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">15) Evaluate how often you use tablet for watching soccer?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_15" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q16-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">16) Evaluate how often you use cellphone for watching soccer?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_16" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q17-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">17) How often do you check team/championship statistics?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_17" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>


        <!--Q18-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">18) Do you prefer to watch soccer alone or with others?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_18" class="u-full-width">
                <option value="alone">Alone</option>
                <option value="withothers">With Others</option>
                <option value="np">No preference</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q19-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">19) Evaluate how often you watch soccer with friends?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_19" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q20-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">20) Evaluate how often you watch soccer with relatives?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_20" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>


        <!--Q21-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">21) Evaluate how often you watch soccer alone?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_21" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q22-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">22) Evaluate how often you watch soccer at home?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_22" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q23-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">23) Evaluate how often you watch soccer at home?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_23" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>


        <!--Q24-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">24) Evaluate how often you watch soccer at the stadium?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_24" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q25-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">25) Evaluate how often you watch soccer in a bar?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_25" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q26-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">26) Evaluate how often you eat while watching soccer?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_26" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q27-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">27) Evaluate how often you drink non-alcoholic beverages while watching soccer?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_27" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q28-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">28) Evaluate how often you drink alcoholic beverages while watching soccer?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_28" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q29-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">29) Do you ever get very emotional while watching soccer?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_29" class="u-full-width">
                <option value="yes">Yes</option>
                <option value="no">No</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

       <!--Q29b-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">29b) Have you ever bought soccer paraphernalia (clothes, souvenirs, other items with a team/player logo on them)?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_29b" class="u-full-width">
                <option value="yes">Yes</option>
                <option value="no">No</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q30-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">30) Do you bet on soccer games?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_30" class="u-full-width">
                <option value="yes">Yes</option>
                <option value="no">No</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q31-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">31) Evaluate how often you win?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_31" class="u-full-width">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q32-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">32) How much detail do you want to see on the screen during corner-kick?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_32" class="u-full-width">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q33-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">33) How much detail do you want to see on the screen during save?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_33" class="u-full-width">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q34-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">34) How much detail do you want to see on the screen during free-kick?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_34" class="u-full-width">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q35-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">35) How much detail do you want to see on the screen during goal?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_35" class="u-full-width">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>


        <!--Q36-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">36) How much detail do you want to see on the screen during assist?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_36" class="u-full-width">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q37-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">37) How much detail do you want to see on the screen during foul?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_37" class="u-full-width">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q38-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">38) How much detail do you want to see on the screen during penalty?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_38" class="u-full-width">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q39-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">39) How much detail do you want to see on the screen during offside?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select v-model="q_39" class="u-full-width">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q40-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">40) How much detail do you want to see on the screen during steal?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select class="u-full-width" v-model="q_40">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>

        <!--Q41-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">41) How much detail do you want to see on the screen during fight</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select class="u-full-width" v-model="q_41">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>


        <!--Q42-->
        <div class="row paddingTop">
          <div class="row questionBody">
            <div class="twelve columns">
              <span class="question">42) How often do you watch UEFA Champions League?</span>
            </div>
          </div>
          <div class="row answerBody">
            <div class="twelve columns">
              <select class="u-full-width" v-model="q_42">
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
              </select>
            </div>
          </div>
        </div>
        <div class="divider"></div>


        <!--Q43-->
        <div class="row paddingTop">
          <div class="twelve columns">
            <label for="Q1">43) На какого/каких игрока/игроков вы обращаете больше всего внимания во время офсайда?</label>
            <table id="Q1" class="u-full-width">
              <thead>
              <tr>
                <th></th>
                <th>Нападающий</th>
                <th>Защитники</th>
                <th>Голкипер</th>
                <th>Само положение мяча</th>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>
                  Главное предпочтение
                </td>
                <td>
                  <input type="radio" value="forward" v-model="q_43_main">
                </td>
                <td>
                  <input type="radio" value="defender" v-model="q_43_main">
                </td>
                <td>
                  <input type="radio" value="goalkeeper" v-model="q_43_main">
                </td>
                <td>
                  <input type="radio" value="ball" v-model="q_43_main">
                </td>
              </tr>
              <tr>
                <td>
                  Алтернативное предпочтение
                </td>
                <td>
                  <input type="radio" value="forward" v-model="q_43_alt">
                </td>
                <td>
                  <input type="radio" value="defender" v-model="q_43_alt">
                </td>
                <td>
                  <input type="radio" value="goalkeeper" v-model="q_43_alt">
                </td>
                <td>
                  <input type="radio" value="ball" v-model="q_43_alt">
                </td>
              </tr>
              </tbody>
            </table >
          </div>
        </div>
        <div style="width: 100%; height: 2px; background-color: #333333"></div>

        <!--Q44-->
        <div class="row paddingTop">
          <div class="twelve columns">
            <label for="Q2">44) На какого/каких игрока/игроков вы обращаете больше всего внимания во время штрафного удара? </label>
            <table id="Q2" class="u-full-width">
              <thead>
              <tr>
                <th></th>
                <th>Нападающий</th>
                <th>Защитники</th>
                <th>Голкипер</th>
                <th>Само положение мяча</th>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>
                  Главное предпочтение
                </td>
                <td>
                  <input type="radio" value="forward" v-model="q_44_main">
                </td>
                <td>
                  <input type="radio" value="defender" v-model="q_44_main">
                </td>
                <td>
                  <input type="radio" value="goalkeeper" v-model="q_44_main">
                </td>
                <td>
                  <input type="radio" value="ball" v-model="q_44_main">
                </td>
              </tr>
              <tr>
                <td>
                  Алтернативное предпочтение
                </td>
                <td>
                  <input type="radio" value="forward" v-model="q_44_alt">
                </td>
                <td>
                  <input type="radio" value="defender" v-model="q_44_alt">
                </td>
                <td>
                  <input type="radio" value="goalkeeper" v-model="q_44_alt">
                </td>
                <td>
                  <input type="radio" value="ball" v-model="q_44_alt">
                </td>
              </tr>
              </tbody>
            </table >
          </div>
        </div>
        <div style="width: 100%; height: 2px; background-color: #333333"></div>


        <!--Q45-->
        <div class="row paddingTop">
          <div class="twelve columns">
            <label for="Q3">
              45) На какого/каких игрока/игроков вы обращаете больше всего внимания во время углового удара?
            </label>
            <table id="Q3" class="u-full-width">
              <thead>
              <tr>
                <th></th>
                <th>Нападающий</th>
                <th>Защитники</th>
                <th>Голкипер</th>
                <th>Само положение мяча</th>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>
                  Главное предпочтение
                </td>
                <td>
                  <input type="radio" value="forward" v-model="q_45_main">
                </td>
                <td>
                  <input type="radio" value="defender" v-model="q_45_main">
                </td>
                <td>
                  <input type="radio" value="goalkeeper" v-model="q_45_main">
                </td>
                <td>
                  <input type="radio" value="ball" v-model="q_45_main">
                </td>
              </tr>
              <tr>
                <td>
                  Алтернативное предпочтение
                </td>
                <td>
                  <input type="radio" value="forward" v-model="q_45_alt">
                </td>
                <td>
                  <input type="radio" value="defender" v-model="q_45_alt">
                </td>
                <td>
                  <input type="radio" value="goalkeeper" v-model="q_45_alt">
                </td>
                <td>
                  <input type="radio" value="ball" v-model="q_45_alt">
                </td>
              </tr>
              </tbody>
            </table >
          </div>
        </div>
        <div style="width: 100%; height: 2px; background-color: #333333"></div>


        <!--Q46-->
        <div class="row paddingTop">
          <div class="twelve columns">
            <label for="Q4">
              46) На какого/каких игрока/игроков вы обращаете больше всего внимания, когда вашей команде забивают гол?
            </label>
            <table id="Q4" class="u-full-width">
              <thead>
              <tr>
                <th></th>
                <th>Нападающий</th>
                <th>Защитники</th>
                <th>Голкипер</th>
                <th>Само положение мяча</th>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>
                  Главное предпочтение
                </td>
                <td>
                  <input type="radio" value="forward" v-model="q_46_main">
                </td>
                <td>
                  <input type="radio" value="defender" v-model="q_46_main">
                </td>
                <td>
                  <input type="radio" value="goalkeeper" v-model="q_46_main">
                </td>
                <td>
                  <input type="radio" value="ball" v-model="q_46_main">
                </td>
              </tr>
              <tr>
                <td>
                  Алтернативное предпочтение
                </td>
                <td>
                  <input type="radio" value="forward" v-model="q_46_alt">
                </td>
                <td>
                  <input type="radio" value="defender" v-model="q_46_alt">
                </td>
                <td>
                  <input type="radio" value="goalkeeper" v-model="q_46_alt">
                </td>
                <td>
                  <input type="radio" value="ball" v-model="q_46_alt">
                </td>
              </tr>
              </tbody>
            </table >
          </div>
        </div>
        <div style="width: 100%; height: 2px; background-color: #333333"></div>


        <!--Q47-->
        <div class="row paddingTop">
          <div class="twelve columns">
            <label for="Q5">
              47) На какого/каких игрока/игроков вы обращаете больше всего внимания, когда ваша команда забивает гол?
            </label>
            <table id="Q5" class="u-full-width">
              <thead>
              <tr>
                <th></th>
                <th>Нападающий</th>
                <th>Защитники</th>
                <th>Голкипер</th>
                <th>Само положение мяча</th>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>
                  Главное предпочтение
                </td>
                <td>
                  <input type="radio" value="forward" v-model="q_47_main">
                </td>
                <td>
                  <input type="radio" value="defender" v-model="q_47_main">
                </td>
                <td>
                  <input type="radio" value="goalkeeper" v-model="q_47_main">
                </td>
                <td>
                  <input type="radio" value="ball" v-model="q_47_main">
                </td>
              </tr>
              <tr>
                <td>
                  Алтернативное предпочтение
                </td>
                <td>
                  <input type="radio" value="forward" v-model="q_47_alt">
                </td>
                <td>
                  <input type="radio" value="defender" v-model="q_47_alt">
                </td>
                <td>
                  <input type="radio" value="goalkeeper" v-model="q_47_alt">
                </td>
                <td>
                  <input type="radio" value="ball" v-model="q_47_alt">
                </td>
              </tr>
              </tbody>
            </table >
          </div>
        </div>
        <div style="width: 100%; height: 2px; background-color: #333333"></div>
      </form>
      <div class="vspace"></div>
    </div>
  </div>
</template>

<script>
  var _ = require('lodash');

  export default {
    name: 'AnketaComponent',
    data() {
      return {
        q_1: 'not chosen yet',
        q_2: 'not chosen yet',
        q_3: 'not chosen yet',
        q_4: 'not chosen yet',
        q_5: 'not chosen yet',
        q_6: 'not chosen yet',
        q_7: 'not chosen yet',
        q_8: 'not chosen yet',
        q_9: 'not chosen yet',
        q_10: 'not chosen yet',
        q_11: 'not chosen yet',
        q_12: 'not chosen yet',
        q_13: 'not chosen yet',
        q_14: 'not chosen yet',
        q_15: 'not chosen yet',
        q_16: 'not chosen yet',
        q_17: 'not chosen yet',
        q_18: 'not chosen yet',
        q_19: 'not chosen yet',
        q_20: 'not chosen yet',
        q_21: 'not chosen yet',
        q_22: 'not chosen yet',
        q_23: 'not chosen yet',
        q_24: 'not chosen yet',
        q_25: 'not chosen yet',
        q_26: 'not chosen yet',
        q_27: 'not chosen yet',
        q_28: 'not chosen yet',
        q_29: 'not chosen yet',
        q_29b: 'not chosen yet',
        q_30: 'not chosen yet',
        q_31: 'not chosen yet',
        q_32: 'not chosen yet',
        q_33: 'not chosen yet',
        q_34: 'not chosen yet',
        q_35: 'not chosen yet',
        q_36: 'not chosen yet',
        q_37: 'not chosen yet',
        q_38: 'not chosen yet',
        q_39: 'not chosen yet',
        q_40: 'not chosen yet',
        q_41: 'not chosen yet',
        q_42: 'not chosen yet',
        q_43_main: 'not chosen yet',
        q_43_alt: 'not chosen yet',
        q_44_main: 'not chosen yet',
        q_44_alt: 'not chosen yet',
        q_45_main: 'not chosen yet',
        q_45_alt: 'not chosen yet',
        q_46_main: 'not chosen yet',
        q_46_alt: 'not chosen yet',
        q_47_main: 'not chosen yet',
        q_47_alt: 'not chosen yet',
        sendButtonShow: false,
        array: []
      }
    },
//    watch: {
//      '$data': {
//        handler: function () {
//          this.array = [];
////          var that = this;
////        _.forEach(this.$data, value  => {
////            that.array.append(value);
////          });
//        },
//        deep: true
//      }
//    },

    sockets: {
      registered: function(data) {
        alert("Your ID is " + data + "\nPlease remember it");
      }
    },

    methods: {

      sendForm: function () {
        console.log('Form', this.$data);
        let test = true;
        _.forEach(this.$data, function (value) {
          if(value === 'not chosen yet'){
              test = false;
          }
        });
        if(test){
          alert('Success! Data has been sent!');
        } else {
          alert('Warn! You missed some fields!');
        }

        this.$socket.emit('anketa', this.$data);


        /* this.$data.forEach(function (data) {
           console.log("form instance", data)
         })*/
      }
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .divider {
    width: 100%; height: 2px; background-color: #333333
  }
  .vscroll{
    overflow-y: auto;
    height: calc(100vh - 120px);
  }
  .vspace {
    height: 60px;
  }
  .fixed {
    position: fixed;
  }
  .paddingTop {
    padding-top: 60px;
  }
  .paddingBottom {
    padding-bottom: 60px;
  }
  .paddingSides {
    padding-left: 130px;
    padding-right: 130px;
  }
  .sidebarHeading{
    color: #35495E;
    font-weight: 800;
  }
</style>
