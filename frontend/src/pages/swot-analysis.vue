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
      swotData: {
        Opportunity: {},
        Strength: {},
        Threat: {},
        Weakness: {}
      },
      ticks: undefined,
      tickerName: "",
      valuedText: "",
      showDetails: false,
      cardLoading: false
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
    getFilteredTickers: function() {
     
    }
  },
  methods: {
    getSWOT: function() {
      this.cardLoading = true;
      axios.get(ENDPOINTS.swot + "/" + this.tickerName)
      .then((resp) => {
        
        this.swotData = resp.data;
        this.showDetails = true;
        this.cardLoading = false;
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
        <VCard title="SWOT Analyzer" :loading="cardLoading">
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
                  <VBtn type="submit" @click="getSWOT">
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
        <div class="text-h6 ma-5">
          Ticker:{{ tickerName }}
        </div>
        <VRow no-gutters>
          <VCol
            cols="12"
            sm="8"
            md="12"
            lg="6"
            order="2"
            order-lg="1"
          >
            <VCardItem>
              <VCardTitle>Strength</VCardTitle>
            </VCardItem>

            <VCardText>
              
            </VCardText>

            <VCardText>
              <VDivider />
            </VCardText>

            <VCardText class="d-flex justify-center">
              <div class="me-auto pe-4">
                <p class="d-flex align-center mb-6" v-for="item in Object.keys(swotData['Strength'])" :key="item">
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
                <p class="d-flex align-center mb-6" v-for="item in Object.keys(swotData['Strength'])" :key="item">
                  <span class="ms-3">{{ swotData['Strength'][item] }}</span>
                </p>
              </div>

              
            </VCardText>
          </VCol>
          
          <VCol
            cols="12"
            sm="8"
            md="12"
            lg="6"
            order="2"
            order-lg="1"
          >
            <VCardItem>
              <VCardTitle>Weakness</VCardTitle>
            </VCardItem>

            <VCardText>
              
            </VCardText>

            <VCardText>
              <VDivider />
            </VCardText>

            <VCardText class="d-flex justify-center">
              <div class="me-auto pe-4">
                <p class="d-flex align-center mb-6" v-for="item in Object.keys(swotData['Weakness'])" :key="item">
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
                <p class="d-flex align-center mb-6" v-for="item in Object.keys(swotData['Weakness'])" :key="item">
                  <span class="ms-3">{{ swotData['Weakness'][item] }}</span>
                </p>
              </div>

              
            </VCardText>
          </VCol>

          <VCol
            cols="12"
            sm="8"
            md="12"
            lg="6"
            order="2"
            order-lg="1"
          >
            <VCardItem>
              <VCardTitle>Opportunity</VCardTitle>
            </VCardItem>

            <VCardText>
              
            </VCardText>

            <VCardText>
              <VDivider />
            </VCardText>

            <VCardText class="d-flex justify-center">
              <div class="me-auto pe-4">
                <p class="d-flex align-center mb-6" v-for="item in Object.keys(swotData['Opportunity'])" :key="item">
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
                <p class="d-flex align-center mb-6" v-for="item in Object.keys(swotData['Opportunity'])" :key="item">
                  <span class="ms-3">{{ swotData['Opportunity'][item] }}</span>
                </p>
              </div>

              
            </VCardText>
          </VCol>

          <VCol
            cols="12"
            sm="8"
            md="12"
            lg="6"
            order="2"
            order-lg="1"
          >
            <VCardItem>
              <VCardTitle>Threat</VCardTitle>
            </VCardItem>

            <VCardText>
              
            </VCardText>

            <VCardText>
              <VDivider />
            </VCardText>

            <VCardText class="d-flex justify-center">
              <div class="me-auto pe-4">
                <p class="d-flex align-center mb-6" v-for="item in Object.keys(swotData['Threat'])" :key="item">
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
                <p class="d-flex align-center mb-6" v-for="item in Object.keys(swotData['Threat'])" :key="item">
                  <span class="ms-3">{{ swotData['Threat'][item] }}</span>
                </p>
              </div>

              
            </VCardText>
          </VCol>
          
        </VRow>
      </VCard>
    </VCol>
    </VRow>
  </div>
</template>
