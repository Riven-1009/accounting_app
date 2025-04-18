<template>
    <div class="container">
      <h1>记账软件</h1>
      <EntryForm @entry-added="fetchEntries" />
      <EntryList :entries="entries" @entry-updated="fetchEntries" @entry-deleted="fetchEntries" />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import EntryForm from './components/EntryForm.vue'
  import EntryList from './components/EntryList.vue'
  
  const entries = ref([])
  
  async function fetchEntries() {
    try {
      const res = await axios.get('/api/entries')
      entries.value = res.data
    } catch (error) {
      console.error('获取账目失败', error)
    }
  }
  
  onMounted(() => {
    fetchEntries()
  })
  </script>
  
  <style>
  .container {
    max-width: 800px;
    margin: 20px auto;
    font-family: Arial, sans-serif;
  }
  </style>