<template>
  <table class="entry-list">
    <thead>
      <tr>
        <th>类型</th>
        <th>金额</th>
        <th>分类</th>
        <th>备注</th>
        <th>日期</th>
        <th>操作</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="entry in entries" :key="entry.id">
        <td>{{ entry.type === 'income' ? '收入' : '支出' }}</td>
        <td>{{ entry.amount.toFixed(2) }}</td>
        <td>
          <select v-model="entry.category" @change="updateEntry(entry)">
            <option v-for="cat in categories" :key="cat" :value="cat">{{ cat }}</option>
          </select>
        </td>
        <td>{{ entry.note }}</td>
        <td>{{ entry.date }}</td>
        <td>
          <button @click="deleteEntry(entry.id)">删除</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
import { defineEmits, defineProps } from 'vue'
import axios from 'axios'

const props = defineProps({
  entries: {
    type: Array,
    required: true
  }
})

const emit = defineEmits(['entry-updated', 'entry-deleted'])

const categories = ['买菜', '交通', '娱乐', '工资', '其他']

async function updateEntry(entry) {
  try {
    await axios.put(`/api/entries/${entry.id}`, {
      type: entry.type,
      amount: entry.amount,
      category: entry.category,
      note: entry.note,
      date: entry.date
    })
    emit('entry-updated', entry)
    console.log('更新成功:', entry)
  } catch (error) {
    alert('更新失败')
    console.error(error)
  }
}

async function deleteEntry(id) {
  try {
    await axios.delete(`/api/entries/${id}`)
    emit('entry-deleted', id)
    console.log('删除成功:', id)
  } catch (error) {
    alert('删除失败')
    console.error(error)
  }
}
</script>

<style scoped>
.entry-list {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

.entry-list th,
.entry-list td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: center;
}

.entry-list select {
  width: 100px;
}

.entry-list button {
  padding: 4px 8px;
  cursor: pointer;
}
</style>