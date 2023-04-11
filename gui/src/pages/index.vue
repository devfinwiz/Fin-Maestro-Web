<script>
import AnalyticsSalesByCountries from '@/views/dashboards/analytics/AnalyticsSalesByCountries.vue'
import axios from 'axios'
import ENDPOINTS from '@/api/endpoints'

export default {
  data: function() {
    return {
      checkbox: ref(false),
      ticks: undefined,
      tickerName: "",
      valuedText: "",
      showDetails: false,
      cardLoading: false,
      indicesAll: [],
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
      },
      salesByCountries: [
        {
          abbr: 'HB',
          amount: 'Vol. 15,738,874',
          country: 'HDFC Bank',
          change: '-2.5%',
          sales: '1560.00',
          color: 'success',
        },
        {
          abbr: 'RL',
          amount: 'Vol. 5,711,497',
          country: 'Reliance',
          change: '-1.98%',
          sales: '2203.00',
          color: 'error',
        },
        {
          abbr: 'RL',
          amount: 'Vol. 5,711,497',
          country: 'Reliance',
          change: '-1.98%',
          sales: '2203.00',
          color: 'error',
        },
        {
          abbr: 'RL',
          amount: 'Vol. 5,711,497',
          country: 'Reliance',
          change: '-1.98%',
          sales: '2203.00',
          color: 'error',
        },
      ]
    }
  },
  mounted: function () {
    console.log(this);
    axios.get(ENDPOINTS.sentiment.pcr + "/index")
    .then((resp) => {
      this.indices = resp.data;
    })
    axios.get(ENDPOINTS.valuation + "/index")
    .then((resp) => {
      this.indicesAll = resp.data;
    })
  },
  computed: {
    getFilteredTickers: function() {
     
    }
  },
  methods: {
    
    
  },
  components: {
    AnalyticsSalesByCountries
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
    <VRow class="match-height">
        <VCol
        cols="4"
        >
        <AnalyticsSalesByCountries
          :listData="salesByCountries"
          :titleC="'Top Gainer'"
          /> 
        </VCol>
        <VCol
          cols="4"
        >
        <AnalyticsSalesByCountries
        :listData="salesByCountries"
            :titleC="'Top Loser'"
          /> 
          </VCol>
          <VCol
          cols="4"
        >
          <AnalyticsSalesByCountries
          :listData="salesByCountries"
          :titleC="'Top Active'"
          /> 
        </VCol>
    </VRow>
    <VRow>
      <VCol cols="3" v-for="index in Object.keys(indicesAll).slice(0,8)" :key="index">
          <v-card 
            class=""
            width="344"
            variant="outlined"
            :style='{"border-width":"4px","border-color":indicesAll[index]}'
          >
            <v-card-item>
              <div>
                <div class="text-h6 mb-1">
                  {{ index }}
                </div>
                <div class="text-overline mb-1">
                  {{ indicesAll[index] }}
                </div>
              </div>
            </v-card-item>
          </v-card>
      </VCol>
    </VRow>
  </div>
</template>

