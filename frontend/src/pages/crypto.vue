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
        <VCard title="Crypto Technical Analyser" :loading="cardLoading">
          <VCardText>
            <iframe src="http://localhost:8050"
            style="width:100%;height:50vh">
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
