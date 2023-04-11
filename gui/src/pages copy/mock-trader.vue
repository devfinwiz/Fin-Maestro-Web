<script setup>
import DemoFormLayoutHorizontalForm from '@/views/user-interface/form-layouts/DemoFormLayoutHorizontalForm.vue'
import DemoFormLayoutHorizontalFormWithIcons from '@/views/user-interface/form-layouts/DemoFormLayoutHorizontalFormWithIcons.vue'
import DemoFormLayoutMultipleColumn from '@/views/user-interface/form-layouts/DemoFormLayoutMultipleColumn.vue'
import DemoFormLayoutVerticalForm from '@/views/user-interface/form-layouts/DemoFormLayoutVerticalForm.vue'
import DemoFormLayoutVerticalFormWithIcons from '@/views/user-interface/form-layouts/DemoFormLayoutVerticalFormWithIcons.vue'
let leftSide = ['Book Value', 'Price To Book', 'Trailing EPS', 'Promoter Holding', 'Price To Sales', 'Price To Earnings', 'Close']
let rightSide = [237.74, 2.03, 14.84, 0.0, 7.31, 32.53, 482.75]
let valuationLeft = ['VAP_BV', 'VAP_SALES', 'VAP_GRAHAM', 'VAP_EARNINGS', 'LTP']
let valuationRight = [570.74, 132.08, 281.75, 400.68, 482.75]
</script>

<template>
  <div>
    <VRow>
      <VCol
        cols="12"
        md="12"
      >
        <VCard title="Valuation Determiner">
          <VCardText>
            <DemoFormLayoutHorizontalForm />
          </VCardText>
        </VCard>
      </VCol>
    <VCol
      md="6"
      lg="12"
      cols="12"
    >
      <VCard>
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
              <VCardTitle>BSE</VCardTitle>
            </VCardItem>

            <VCardText>
              Maybe some info about reliance.
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
                <sup class="text-h4 font-weight-medium">473.30</sup>
                <sub class="text-h5">INR</sub>
              </p>

              <p class="text-h3 mt-6" style="color:limegreen">
                Fairly Valued
              </p>
            </div>
          </VCol>
        </VRow>
      </VCard>
    </VCol>
    </VRow>
  </div>
</template>
