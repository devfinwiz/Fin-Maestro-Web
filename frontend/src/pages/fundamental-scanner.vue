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
      fundamentalData: {
        bookValue: [],
        sales: [],
        graham: [],
        earnings: []
      },
      ticks: undefined,
      tickerName: "",
      valuedText: "",
      showDetails: true,
      cardLoading: false
    }
  },
  mounted: function () {
    axios.get(ENDPOINTS.fundamental)
    .then((response) => {
      this.fundamentalData = response.data;
    })
    .catch((error) => {
      console.log(error);
    })
  },
  computed: {
  },
  methods: {
  }
}
</script>

<template>
  <div>
    <VRow>

      <VCol md="6" lg="12" cols="12">
        <VCard v-show="showDetails">
          <VRow no-gutters>
            <v-expansion-panels>
              <v-expansion-panel title="Book Value Based">
                <v-expansion-panel-text>
                  <VCol cols="12" sm="8" md="12" lg="12" order="2" order-lg="1">
                    <VCardItem>
                      <VCardTitle>Book Value Based</VCardTitle>
                    </VCardItem>

                    <VCardText>

                    </VCardText>

                    <VCardText>
                      <VDivider />
                    </VCardText>

                    <VCardText class="d-flex justify-center">

                      <VRow>
                        <VCol cols="2" v-for="item in fundamentalData.bookValue" :key="item">
                          {{ item }}
                        </VCol>
                      </VRow>


                    </VCardText>
                  </VCol>
                </v-expansion-panel-text>
              </v-expansion-panel>
              <v-expansion-panel title="Sales Based">
                <v-expansion-panel-text>
                  <VCol cols="12" sm="8" md="12" lg="12" order="2" order-lg="1">
                    <VCardItem>
                      <VCardTitle>Sales Based</VCardTitle>
                    </VCardItem>

                    <VCardText>

                    </VCardText>

                    <VCardText>
                      <VDivider />
                    </VCardText>

                    <VCardText class="d-flex justify-center">

                      <VRow>
                        <VCol cols="2" v-for="item in fundamentalData.sales" :key="item">
                          {{ item }}
                        </VCol>
                      </VRow>


                    </VCardText>
                  </VCol>
                </v-expansion-panel-text>
              </v-expansion-panel>
              <v-expansion-panel title="Graham Number Based">
                <v-expansion-panel-text>
                  <VCol cols="12" sm="8" md="12" lg="12" order="2" order-lg="1">
                    <VCardItem>
                      <VCardTitle>Graham Number Based</VCardTitle>
                    </VCardItem>

                    <VCardText>

                    </VCardText>

                    <VCardText>
                      <VDivider />
                    </VCardText>

                    <VCardText class="d-flex justify-center">

                      <VRow>
                        <VCol cols="2" v-for="item in fundamentalData.graham" :key="item">
                          {{ item }}
                        </VCol>
                      </VRow>


                    </VCardText>
                  </VCol>
                </v-expansion-panel-text>
              </v-expansion-panel>
              <v-expansion-panel title="Earnings Based">
                <v-expansion-panel-text>
                  <VCol cols="12" sm="8" md="12" lg="12" order="2" order-lg="1">
                    <VCardItem>
                      <VCardTitle>Earnings Based</VCardTitle>
                    </VCardItem>

                    <VCardText>

                    </VCardText>

                    <VCardText>
                      <VDivider />
                    </VCardText>

                    <VCardText class="d-flex justify-center">

                      <VRow>
                        <VCol cols="2" v-for="item in fundamentalData.earnings" :key="item">
                          {{ item }}
                        </VCol>
                      </VRow>


                    </VCardText>
                  </VCol>
                </v-expansion-panel-text>
              </v-expansion-panel>
            </v-expansion-panels>
          </VRow>
        </VCard>
      </VCol>
    </VRow>
  </div>
</template>
