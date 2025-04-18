<template>
    <form @submit.prevent="submitEntry" class="entry-form">
      <label>
        类型:
        <select v-model="type" required>
          <option value="income">收入</option>
          <option value="expense">支出</option>
        </select>
      </label>
  
      <label>
        金额:
        <input type="number" v-model.number="amount" required min="0.01" step="0.01" />
      </label>
  
      <label>
        分类:
        <input type="text" v-model="category" required />
      </label>
  
      <label>
        备注:
        <input type="text" v-model="note" />
      </label>
  
      <label>
        日期:
        <input type="date" v-model="date" required />
      </label>
  
      <button type="submit">添加账目</button>
    </form>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  
  const type = ref('expense')
  const amount = ref(null)
  const category = ref('')
  const note = ref('')
  const date = ref(new Date().toISOString().slice(0, 10))
  
  async function submitEntry() {
    if (!amount.value || !category.value) {
      alert('请填写金额和分类')
      return
    }
    try {
      await axios.post('/api/entries', {
        type: type.value,
        amount: amount.value,
        category: category.value,
        note: note.value,
        date: date.value
      })
      alert('添加成功')
      // 重置表单
      type.value = 'expense'
      amount.value = null
      category.value = ''
      note.value = ''
      date.value = new Date().toISOString().slice(0, 10)
      // 触发父组件刷新
      emit('entry-added')
    } catch (error) {
      alert('添加失败')
      console.error(error)
    }
  }
  
  const emit = defineEmits(['entry-added'])
  </script>
  
  <style scoped>
  .entry-form {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 20px;
  }
  .entry-form label {
    flex: 1 1 150px;
    display: flex;
    flex-direction: column;
  }
  .entry-form button {
    padding: 6px 12px;
    cursor: pointer;
  }
  </style>