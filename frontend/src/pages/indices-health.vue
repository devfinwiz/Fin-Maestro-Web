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
        },
      indices: {
      } 
    }
  },
  mounted: function () {
    axios.get(ENDPOINTS.valuation + "/index")
    .then((resp) => {
      this.indices = resp.data;
    })
  },
  computed: {
    getFilteredTickers: function() {
     
    }
  },
  methods: {
  }
}
</script>

<template>
  <div>
    <VRow>
      <VCol cols="3" v-for="index in Object.keys(indices)" :key="index">
          <v-card 
            class=""
            width="344"
            variant="outlined"
            :style='{"border-width":"4px","border-color":indices[index]}'
          >
            <v-card-item>
              <div>
                <div class="text-h6 mb-1">
                  {{ index }}
                </div>
                <div class="text-overline mb-1">
                  {{ indices[index] }}
                </div>
              </div>
            </v-card-item>
          </v-card>
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
