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
      showDetails: true,
      cardLoading: false,
      myData: {
        columns: [
            ['sentiment', 0]
        ],
        type: 'gauge',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
        }
    }
  },
  mounted: function () {
    
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
        this.mountChart(this.$refs.guage)
        this.cardLoading = false;
      })
      
    },
    mountChart: function(chartr) {
      var chart = c3.generate({
          bindto: chartr,
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
      <VCol
        cols="12"
        md="12"
      >
        <VCard title="Pattern Analyser" :loading="cardLoading">
          <VCardText>
            <iframe src="http://localhost:5000/scanner"
            style="width:100%;height:80vh">
            </iframe>
          </VCardText>
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
