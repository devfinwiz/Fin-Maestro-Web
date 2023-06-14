<script setup>

import logo from '@/assets/logo.svg?raw'
import {
  VerticalNavLink,
  VerticalNavSectionTitle,
} from '@layouts'
import { useTheme } from 'vuetify'

const vuetifyTheme = useTheme()
</script>

<template>
  <!-- 👉 Nav header -->
  <div class="nav-header">
    <RouterLink
      to="/"
      class="app-logo d-flex align-center gap-x-3 app-title-wrapper"
    >

      <Transition name="vertical-nav-app-title">
        <h1 class="font-weight-semibold leading-normal text-xl text-uppercase">
          Fin-Maestro
        </h1>
      </Transition>
    </RouterLink>
  </div>

  
  <ul>
    <VerticalNavLink
      :item="{
        title: 'Dashboard',
        to: 'index',
        icon: { icon: 'mdi-home-outline' }
      }"
    />
    <VerticalNavSectionTitle :item="{ heading: 'Tools' }" />
    <VerticalNavLink
      :item="{
        title: 'Valuation Determiner',
        to: 'valuation-determiner',
        icon: { icon: 'mdi-cash' }
      }"
    />
    <!-- 👉 Pages -->
    
    <VerticalNavLink
      :item="{
        title: 'Mock Trader',
        to: 'mock-trader',
        icon: { icon: 'mdi-login' }
      }"
    />

    <VerticalNavLink
      :item="{
        title: 'Sentiment Analyzer',
        to: 'sentiment',
        icon: { icon: 'mdi-cash' }
      }"
    />

    <VerticalNavLink
      :item="{
        title: 'Pattern Analyzer',
        to: 'pattern-analyzer',
        icon: { icon: 'mdi-cash' }
      }"
    />
    
    <VerticalNavLink
      :item="{
        title: 'Indices Health',
        to: 'indices-health',
        icon: { icon: 'mdi-cash' }
      }"
    />

    <VerticalNavLink
      :item="{
        title: 'SWOT Aanlyzer',
        to: 'swot-analysis',
        icon: { icon: 'mdi-cash' }
      }"
    />

    <VerticalNavLink
      :item="{
        title: 'Fundamental Scans',
        to: 'fundamental-scanner',
        icon: { icon: 'mdi-cash' }
      }"
    />

    <VerticalNavLink
      :item="{
        title: 'Crypto Tech. Analyzer',
        to: 'crypto',
        icon: { icon: 'mdi-cash' }
      }"
    />

    <VerticalNavLink
      :item="{
        title: 'Backtesting',
        to: 'backtesting',
        icon: { icon: 'mdi-cash' }
      }"
    />
    
  </ul>
</template>

<style lang="scss">
// .v-navigation-drawer {
//   height: 100%;

//   .v-navigation-drawer__content {
//     display: flex;
//     flex-direction: column;

//     > ul {
//       flex-grow: 1;
//     }
//   }
// }

.upgrade-banner {
  margin-top: auto;
  // position: absolute;
  // bottom: 13px;
  // left: 50%;
  // transform: translateX(-50%);
}
</style>
