<script>
import DemoFormLayoutHorizontalForm from '@/views/user-interface/form-layouts/DemoFormLayoutHorizontalForm.vue'
import DemoFormLayoutHorizontalFormWithIcons from '@/views/user-interface/form-layouts/DemoFormLayoutHorizontalFormWithIcons.vue'
import DemoFormLayoutMultipleColumn from '@/views/user-interface/form-layouts/DemoFormLayoutMultipleColumn.vue'
import DemoFormLayoutVerticalForm from '@/views/user-interface/form-layouts/DemoFormLayoutVerticalForm.vue'
import DemoFormLayoutVerticalFormWithIcons from '@/views/user-interface/form-layouts/DemoFormLayoutVerticalFormWithIcons.vue'
import axios from 'axios'
import VueApexCharts from 'vue3-apexcharts';
import dayjs from 'dayjs'
import ENDPOINTS from '@/api/endpoints'
import Datepicker from 'vue3-datepicker'


export default {
  data: function() {
    return {
      leftSide: ['Book Value', 'Price To Book', 'Trailing EPS', 'Promoter Holding', 'Price To Sales', 'Price To Earnings', 'Close'],
      rightSide: [0,0,0,0,0,0,0],
      valuationLeft: ['VAP_BV', 'VAP_SALES', 'VAP_GRAHAM', 'VAP_EARNINGS', 'LTP'],
      valuationRight: [0,0,0,0,0],
      firstName: ref(''),
      email: ref(''),
      mobile: ref(),
      password: ref(),
      checkbox: ref(false),
      ticks: undefined,
      tickerName: "",
      valuedText: "",
      showDetails: false,
      showChart: false,
      cardLoading: false,
      pickedDate: new Date(),
      chartOptions: {
        chart: {
          height: 350,
          type: 'candlestick',
        },
        title: {
          text: 'STOCK Data',
          align: 'left'
        },
        annotations: {
          xaxis: [
            {
              x: 'Oct 06 14:00',
              borderColor: '#00E396',
              label: {
                borderColor: '#00E396',
                style: {
                  fontSize: '12px',
                  color: '#fff',
                  background: '#45494f'
                },
                orientation: 'horizontal',
                offsetY: 7,
                text: 'Some Signal'
              }
            }
          ]
        },
        tooltip: {
          enabled: true,
        },
        xaxis: {
          type: 'category',
          labels: {
            formatter: function(val) {
              return dayjs(val).format('MMM DD HH:mm')
            }
          }
        },
        yaxis: {
          tooltip: {
            enabled: true
          }
        },
        theme: {
            mode: 'dark', 
            palette: 'palette1', 
            monochrome: {
                enabled: false,
                color: '#255aee',
                shadeTo: 'light',
                shadeIntensity: 0.65
            },
        }
      },
      series: [{
            name: 'candle',
            data: []
          }],
      ohlc: [],
      trades: [],
      validDateRange: true
    }
  },
  mounted: function () {
    
  },
  computed: {
    getFilteredTickers: function() {
     
    },
    getValidRange: function() {
      if(!this.validDateRange)
        return "Enter range between: " + String(this.ohlc.at(1).x) + " and " + String(this.ohlc.at(-1).x)
      else
        return ""
    }
  },
  methods: {
    getOHLC: function() {
      axios.get(ENDPOINTS.ohlc + "/" + this.tickerName + "/daily")
      .then( (resp) => {
        let prices = resp.data[this.tickerName+".NS"]["prices"]
        let ser = []
        prices.forEach( (valu, ind) => {
          ser.push({
            x: new Date(valu.date*1000),
            y: [parseFloat(valu.open).toFixed(2), parseFloat(valu.high).toFixed(2), parseFloat(valu.low).toFixed(2), parseFloat(valu.close).toFixed(2)]
          })
        })
        this.series[0].data = ser;
        this.$refs.ogcharto.updateSeries([{
          data: ser,
        }], false, true);
        this.showChart = true;
        this.ohlc = ser;
      } )
      axios.get(ENDPOINTS.getTrades + "/" + this.tickerName)
      .then((resp) => {
        let trades = resp.data["trades"];
        this.trades = []
        if (trades.length > 0){
        trades.forEach((v,i) => {
            this.trades.push(
              {
                id: v[0],
                tickerName: v[1],
                type: v[2], // 1 is buy 2 is sell
                enterPrice: v[3],
                exitPrice: v[4],
                isOpen: v[5] == "1" ? true : false,
              }
            )
          })
        }
      })
    },
    wrapTrade: function(trade) {
      if (trade.isOpen) {
        if (trade.type == 1) {
          trade.exitPrice = this.series[0].data.at(-1).y[3]
          console.log(trade.exitPrice)
          trade.isOpen = false
        } else {
          trade.exitPrice = this.series[0].data.at(-1).y[3]
          trade.isOpen = false
        }
        axios.get(ENDPOINTS.exitTrade + "/" + trade.id + "/" + trade.exitPrice).then((r) => {console.log("exited trade")})
      }
    },
    placeTrade: function(type){
      var trade = {
          id: this.trades.length > 0 ? this.trades.at(-1).id + 1 : 0,
          tickerName: this.tickerName,
          type: type, // 1 is buy 2 is sell
          enterPrice: this.series[0].data.at(-1).y[3],
          exitPrice: null,
          isOpen: true,
        }
      axios.post(ENDPOINTS.registerTrade, trade).then((r) => {console.log("registered trade")})
      this.trades.push(trade)
    },
    updateOhlcToDate: function (date){
      if (date > this.ohlc.at(1) && date < this.ohlc.at(-1)) {
        this.$refs.ogcharto.updateSeries([{
          data: ser,
        }], false, true);
      }
    },
  },
  watch: {
    pickedDate (ov, nv){
      if (nv > this.ohlc.at(1) && nv < this.ohlc.at(-1)){
        this.validDateRange = true;
      }else{
        this.validDateRange = false;
      }
    }
  },
  components: {
    VueApexCharts,
    Datepicker
  }
}
</script>

<template>
  <div>
    <VRow>
      <VCol
        cols="12"
        md="12"
      >
        <VCard title="Mock Trader" :loading="cardLoading">
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
                  <VBtn type="submit" @click="getOHLC">
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
      <VCard v-show="showChart">
        <VRow no-gutters>
          <VCol
            cols="10"
            order="2"
            order-lg="1"
          >
            <VCardItem>
              <div id="chart">
                <VueApexCharts ref="ogcharto" type="candlestick" height="350" :options="chartOptions" :series="series"></VueApexCharts>
              </div>
            </VCardItem>

          </VCol>
          <VCol
            cols="2"
            order="2"
            order-lg="1"
          >
          <VRow>
          <VCol cols="12">
          <v-btn @click="placeTrade(1)" prepend-icon="mdi-arrow-up" class="ma-2 mt-4" color="success">
            Buy
          </v-btn>
          <v-btn @click="placeTrade(2)" prepend-icon="mdi-arrow-down" class="ma-2 mt-4" color="error">
            Sell
          </v-btn>
          <v-btn class="ma-2 mt-4" color="success">
              <VIcon icon="mdi-forward"></VIcon>
          </v-btn>
          </VCol>
          </VRow>
          <VRow>
            <Datepicker v-model="pickedDate" />
            <span style="color:red">{{ getValidRange }}</span>
          </VRow>

          </VCol>
        </VRow>
        <VRow>
          <VCol
            v-for="trade in trades" :key="trade.id"
            cols="3"
          >
          <v-card 
            class="ma-5"
            max-width="344"
            variant="outlined"
          >
            <v-card-item>
              <div>
                <div class="text-overline mb-1">
                  {{ trade.type == 1 ? "BUY" : "SELL" }} | {{ trade.tickerName }}
                </div>
                <div class="text-h6 mb-1">
                  {{ "IN:" + trade.enterPrice }} {{ trade.isOpen ? "" : "OUT:" + trade.exitPrice }}
                </div>
                <div class="text-caption">Trade Summary</div>
              </div>
            </v-card-item>

            <v-card-actions>
              <v-btn :disabled="!trade.isOpen" variant="outlined" :color="trade.type == 1 ? 'error' : 'success'" @click="wrapTrade(trade)">
                {{ trade.type == 1 ? "SELL" : "BUY" }}
              </v-btn>
            </v-card-actions>
          </v-card>
          </VCol>
        </VRow>
      </VCard>
    </VCol>
    </VRow>
  </div>
</template>
