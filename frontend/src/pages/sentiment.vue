<script>
import DemoFormLayoutHorizontalForm from '@/views/user-interface/form-layouts/DemoFormLayoutHorizontalForm.vue'
import DemoFormLayoutHorizontalFormWithIcons from '@/views/user-interface/form-layouts/DemoFormLayoutHorizontalFormWithIcons.vue'
import DemoFormLayoutMultipleColumn from '@/views/user-interface/form-layouts/DemoFormLayoutMultipleColumn.vue'
import DemoFormLayoutVerticalForm from '@/views/user-interface/form-layouts/DemoFormLayoutVerticalForm.vue'
import DemoFormLayoutVerticalFormWithIcons from '@/views/user-interface/form-layouts/DemoFormLayoutVerticalFormWithIcons.vue'
import axios from 'axios'
import ENDPOINTS from '@/api/endpoints'
import c3 from 'c3';

export default {
  data: function() {
    return {
      checkbox: ref(false),
      ticks: undefined,
      tickerName: "",
      valuedText: "",
      showDetails: false,
      cardLoading: false,
      stockSentStatus: "UNKNOWN",
      myData: {
        columns: [
            ['sentiment', 0]
        ],
        type: 'gauge',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
        },
      indices: {
        "NIFTY": ["UNKNOWN", -1],
        "BANKNIFTY": ["UNKNOWN", -1]
      } 
    }
  },
  mounted: function () {
    this.mountChart("#gauge")
    axios.get(ENDPOINTS.sentiment.pcr + "/index")
    .then((resp) => {
      this.indices = resp.data;
    })
  },
  computed: {
    getFilteredTickers: function() {
     
    }
  },
  methods: {
    getSentiments: function() {
      this.cardLoading = true;
      
      axios.get(ENDPOINTS.sentiment.pcr + "/" + this.tickerName)
      .then((resp) => {
        this.myData.columns[1] = resp.data[this.tickerName][1] * 100
        this.stockSentStatus = resp.data[this.tickerName][0]
        this.cardLoading = false;
        this.showDetails = true;
      })
      
    },
    mountChart: function(chartr) {
      var chart = c3.generate({
          bindto: "#gauge",
          data: this.myData,
          gauge: {
            label: {
                format: function(pcr_value, ratio) {
                  pcr_value /= 100
                  if(pcr_value>=1)
                      return "Overbought"
                  if(pcr_value<1 && pcr_value>=0.75)
                      return "Slightly overbought"
                  if(pcr_value<0.75 && pcr_value>=0.50)
                      return "Neutral"
                  if(pcr_value<0.50 & pcr_value>=0.4)
                      return "Slightly oversold"
                  
                  return "Oversold"
                },
                show: false // to turn off the min/max labels.
            },
      //    min: 0, // 0 is default, //can handle negative min e.g. vacuum / voltage / current flow / rate of change
      //    max: 100, // 100 is default
      //    units: ' %',
      //    width: 39 // for adjusting arc thickness
          },
          color: {
              pattern: ['#60B044', '#FF0000', '#F97600', '#F6C600'], // the three color levels for the percentage values.
              threshold: {
                  values: [40, 50, 75, 100]
              }
          },
          size: {
              height: 300
          }
      });
    }
  }
}
</script>

<template>
  <div>
    <VRow>
      <VCol cols="6" class="d-flex justify-end">
          <v-card 
            class=""
            width="344"
            variant="outlined"
            :style='{borderColor:"green"}'
          >
            <v-card-item>
              <div>
                <div class="text-h6 mb-1">
                  NIFTY
                </div>
                <div class="text-overline mb-1">
                  {{ indices.NIFTY[0] }}
                </div>
              </div>
            </v-card-item>
          </v-card>
      </VCol>
      <VCol cols="6">
          <v-card 
            class=""
            width="344"
            variant="outlined"
            :style='{borderColor:"green"}'
          >
            <v-card-item>
              <div>
                <div class="text-h6 mb-1">
                  BANKNIFTY
                </div>
                <div class="text-overline mb-1">
                  {{ indices.BANKNIFTY[0] }}
                </div>
              </div>
            </v-card-item>
          </v-card>
      </VCol>
    </VRow>
    <VRow>
      <VCol
        cols="12"
        md="12"
      >
        <VCard title="Sentiment Analyser" :loading="cardLoading">
          <VCardText>
            <VForm @submit.prevent="() => {}">
              <VRow>
                <VCol cols="12">
                  <VRow no-gutters>
                    <!-- 👉 First Name -->
                    <VCol
                      cols="12"
                      md="3"
                    >
                      <label for="firstName" class="text-h6">Enter Stock Name:</label>
                    </VCol>

                    <VCol
                      cols="12"
                      md="9"
                    >
                      <VTextField
                        label="Stock Name"
                        v-model="tickerName"
                      ></VTextField>
                    </VCol>
                  </VRow>
                </VCol>

                <!-- 👉 Remember me -->

                <!-- 👉 submit and reset button -->
                <VCol
                  offset-md="3"
                  cols="12"
                  md="9"
                  class="d-flex gap-4"
                >
                  <VBtn type="submit" @click="getSentiments">
                    Submit
                  </VBtn>
                  <VBtn
                    color="secondary"
                    variant="tonal"
                    type="reset"
                  >
                    Reset
                  </VBtn>
                </VCol>
              </VRow>
            </VForm>
          </VCardText>
        </VCard>
      </VCol>
    <VCol
      md="6"
      lg="12"
      cols="12"
    >
      <VCard v-show="showDetails">
        <VRow no-gutters>

          <VCol
            cols="12"
            
            order="1"
            order-lg="2"
            class="member-pricing-bg text-center pa-5"
          >
          <v-card 
            class="mr-5"
            width="344"
            variant="outlined"
            :style='{display:"inline-block"}'
          >
            <v-card-item>
                <div>
                  <div class="text-h6 mb-1">
                    Stock Name
                  </div>
                  <div class="text-overline mb-1" style="font-size:16px">
                    {{ tickerName }}
                  </div>
                </div>
              </v-card-item>
            </v-card>
            <v-card 
            class=""
            :style='{display:"inline-block"}'
            width="344"
            variant="outlined"
          >
            <v-card-item>
                <div>
                  <div class="text-h6 mb-1">
                    {{ indices.NIFTY[0] }}
                  </div>
                  <div class="text-overline mb-1" style="font-size:16px">
                    PCR Value: {{ this.myData.columns[1] / 100 }}
                  </div>
                </div>
              </v-card-item>
            </v-card>
            
            
          </VCol>
        </VRow>
      </VCard>
    </VCol>
    </VRow>
  </div>
</template>
<style>
.c3-gauge-value{
  font-size: 25px !important;
  fill: white !important;
}
.c3-axis-y text {
   fill: white !important;
}
.c3-axis-x text {
    fill:white !important;
}
</style>
