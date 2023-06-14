<script setup>
defineProps({
  listData: Array,
  titleC: String,
});

</script>

<template>
  <VCard>
    <VCardItem>
      <VCardTitle>{{ titleC }}</VCardTitle>

      <template #append>
        <div class="me-n3">
          <VBtn
            icon
            size="x-small"
            variant="text"
            color="default"
          >
            <VIcon
              size="24"
              icon="mdi-dots-vertical"
            />
          </VBtn>
        </div>
      </template>
    </VCardItem>

    <VCardText>
      <VList class="card-list">
        <VListItem
          v-for="data in listData"
          :key="data.country"
        >
          <template #prepend>
            <VAvatar
              size="40"
              variant="tonal"
              :color="data.color"
              class="me-3"
            >
              {{ data.abbr }}
            </VAvatar>
          </template>

          <VListItemTitle class="mb-1">
            <span class="text-sm font-weight-semibold">{{ data.country }}</span>
            <VIcon
              size="22"
              :color="data.change.charAt(0) === '+' ? 'success' : 'error'"
              class="mx-1"
            >
              {{ data.change.charAt(0) === '+' ? 'mdi-chevron-up' : 'mdi-chevron-down' }}
            </VIcon>
            <span :class="`text-xs ${data.change.charAt(0) === '+' ? 'text-success' : 'text-error'}`">
              {{ data.change.slice(1) }}
            </span>
          </VListItemTitle>

          <VListItemSubtitle class="text-xs">
            {{ data.amount }}
          </VListItemSubtitle>

          <template #append>
            <div>
              <h4 class="font-weight-semibold">
                {{ data.sales }}
              </h4>
              <span class="text-xs text-medium-emphasis">Sales</span>
            </div>
          </template>
        </VListItem>
      </VList>
    </VCardText>
  </VCard>
</template>

  <style lang="scss" scoped>
  .card-list {
    --v-card-list-gap: 1.5rem;
  }
  </style>

