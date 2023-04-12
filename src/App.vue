<script setup lang="ts">
import { NConfigProvider } from 'naive-ui'
import { NaiveProvider } from '@/components/common'
import { useTheme } from '@/hooks/useTheme'
import { useLanguage } from '@/hooks/useLanguage'
import { ref } from 'vue'

const { theme, themeOverrides } = useTheme()
const { language } = useLanguage()

// 添加登录表单所需的数据和方法
const username = ref('')
const loggedIn = ref(false)

async function login() {
  const response = await fetch(`/api/login?username=${username.value}`)
  const data = await response.json()
  if (data.allowed) {
    loggedIn.value = true
  } else {
    alert('Access denied. You are not an allowed user.')
  }
}
</script>

<template>
  <NConfigProvider
    class="h-full"
    :theme="theme"
    :theme-overrides="themeOverrides"
    :locale="language"
  >
    <NaiveProvider>
      <RouterView />
      <div>
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" />
        <button @click="login">Login</button>
      </div>
    </NaiveProvider>
  </NConfigProvider>
</template>

