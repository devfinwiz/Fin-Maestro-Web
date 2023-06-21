<script>
import DemoFormLayoutHorizontalForm from '@/views/user-interface/form-layouts/DemoFormLayoutHorizontalForm.vue'
import DemoFormLayoutHorizontalFormWithIcons from '@/views/user-interface/form-layouts/DemoFormLayoutHorizontalFormWithIcons.vue'
import DemoFormLayoutMultipleColumn from '@/views/user-interface/form-layouts/DemoFormLayoutMultipleColumn.vue'
import DemoFormLayoutVerticalForm from '@/views/user-interface/form-layouts/DemoFormLayoutVerticalForm.vue'
import DemoFormLayoutVerticalFormWithIcons from '@/views/user-interface/form-layouts/DemoFormLayoutVerticalFormWithIcons.vue'
import axios from 'axios'
import ENDPOINTS from '@/api/endpoints'

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
      valuedColor: "red",
      showDetails: false,
      cardLoading: false,
      filterT: []
    }
  },
  mounted: function () {
    axios.get(ENDPOINTS.tickers)
    .then((response) => {
      this.ticks = response.data;
    })
    .catch((error) => {
      console.log(error);
    })
  },
  computed: {
    filteredTickers: function() {
      var fi = []
      this.filterT.forEach((i,v) => {
        fi.push(i[1]);
     })
     return fi;
    }
  },
  methods: {
    getValuation: function() {
      this.getTicker()
      this.cardLoading = true;
      axios.get(ENDPOINTS.valuation + "/" + this.tickerName)
      .then((resp) => {
        this.valuedText = resp.data.v1.STATUS;
        this.valuedColor = this.valuedText == "Overvalued" ? "red" : "green";
        
        this.valuationRight = [resp.data.v1.VAP_BV, resp.data.v1.VAP_SALES, resp.data.v1.VAP_GRAHAM, resp.data.v1.VAP_EARNINGS]
        this.rightSide = [resp.data.v2.bookValue, resp.data.v2.priceToBook,resp.data.v2.trailingEPS,resp.data.v2.promoterHolding,resp.data.v2.priceToSales,resp.data.v2.priceToEarnings,resp.data.v2.close]
        this.showDetails = true
        const sum = this.valuationRight.reduce((a, b) => a + b, 0);
        const avg = (sum / this.valuationRight.length) || 0;
        this.valuationRight.push(resp.data.v1.LTP)
        this.cardLoading = false;
      })
      
    },
    getTicker: function(){
      this.filterT.forEach((i,v)=>{
        if (i[1] == this.tickerName){
          this.tickerName = i[0]
        }
      })
    }
  },
  watch: {
    tickerName: function(o,n){
      if (n.length < 3){
        return
      }
      axios.get(ENDPOINTS.filterTickers + "/" + n).then((r) => {
        this.filterT = r.data.tickers
      })
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
        <VCard title="Valuation Determiner" :loading="cardLoading">
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
                      <v-combobox
                        label="Stock Name"
                        v-model="tickerName"
                        :items="filteredTickers"
                      ></v-combobox>
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
                  <VBtn type="submit" @click="getValuation">
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
            sm="8"
            md="12"
            lg="7"
            order="2"
            order-lg="1"
          >
            <VCardItem>
              <VCardTitle>Ticker:{{ tickerName }}</VCardTitle>
            </VCardItem>

            <VCardText>
              
            </VCardText>

            <VCardText>
              <VDivider />
            </VCardText>

            <VCardText class="d-flex justify-center">
              <div class="me-auto pe-4">
                <p class="d-flex align-center mb-6" v-for="item in leftSide">
                  <VIcon
                    color="primary"
                    icon="mdi-lock-open-outline"
                  />
                  <span class="ms-3">{{ item }}</span>
                </p>
              </div>

              <VDivider
                v-if="$vuetify.display.smAndUp"
                vertical
                inset
              />

              <div class="me-auto ps-4">
                <p class="d-flex align-center mb-6" v-for="item in rightSide">
                  <span class="ms-3">{{ item }}</span>
                </p>
              </div>

              <div class="me-auto pe-4">
                <p class="d-flex align-center mb-6" v-for="item in valuationLeft">
                  <VIcon
                    color="primary"
                    icon="mdi-lock-open-outline"
                  />
                  <span class="ms-3">{{ item }}</span>
                </p>
              </div>

              <VDivider
                v-if="$vuetify.display.smAndUp"
                vertical
                inset
              />

              <div class="me-auto ps-4">
                <p class="d-flex align-center mb-6" v-for="item in valuationRight">
                  <span class="ms-3">{{ item }}</span>
                </p>
              </div>
            </VCardText>
          </VCol>

          <VCol
            cols="12"
            sm="4"
            md="12"
            lg="5"
            order="1"
            order-lg="2"
            class="member-pricing-bg text-center"
          >
            <div class="membership-pricing d-flex flex-column align-center py-14 h-100 justify-center">
              <p class="mb-5">
                <p class="text-h5 pr-3" style="display:inline">LTP: </p>
                <sup class="text-h4 font-weight-medium">{{ valuationRight[4] }}</sup>
                <sub class="text-h5">INR</sub>
              </p>

              <p class="text-h3 mt-6" :style='{"color":valuedColor}'>
                {{ valuedText }}
              </p>
            </div>
          </VCol>
        </VRow>
      </VCard>
    </VCol>
    </VRow>
  </div>
</template>
