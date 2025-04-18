<template>
    <div>
      <table border="1" cellpadding="6" cellspacing="0" style="width:100%; text-align:center;">
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
            <td>{{ entry.type }}</td>
            <td>{{ entry.amount.toFixed(2) }}</td>
            <td>{{ entry.category }}</td>
            <td>{{ entry.note }}</td>
            <td>{{ entry.date }}</td>
            <td>
              <button @click="startEdit(entry)">编辑</button>
              <button @click="deleteEntry(entry.id)">删除</button>
            </td>
          </tr>
        </tbody>
      </table>
  
      <div v-if="editingEntry" class="edit-form">
        <h3>编辑账目</h3>
        <form @submit.prevent="submitEdit">
          <label>
            类型:
            <select v-model="editingEntry.type" required>
              <option value="income">收入</option>
              <option value="expense">支出</option>
            </select>
          </label>
  
          <label>
            金额:
            <input type="number" v-model.number="editingEntry.amount" required min="0.01" step="0.01" />
          </label>
  
          <label>
            分类:
            <input type="text" v-model="editingEntry.category" required />
          </label>
  
          <label>
            备注:
            <input type="text" v-model="editingEntry.note" />
          </label>
  
          <label>
            日期:
            <input type="date" v-model="editingEntry.date" required />
          </label>
  
          <button type="submit">保存</button>
          <button type="button" @click="cancelEdit">取消</button>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  
  const props = defineProps({
    entries: Array
  })
  const emit = defineEmits(['entry-updated', 'entry-deleted'])
  
  const editingEntry = ref(null)
  
  function startEdit(entry) {
    editingEntry.value = { ...entry }
  }
  
  function cancelEdit() {
    editingEntry.value = null
  }
  
  async function submitEdit() {
    try {
      await axios.put(`/api/entries/${editingEntry.value.id}`, editingEntry.value)
      alert('更新成功')
      emit('entry-updated')
      editingEntry.value = null
    } catch (error) {
      alert('更新失败')
      console.error(error)
    }
  }
  
  async function deleteEntry(id) {
    if (!confirm('确定删除该账目吗？')) return
    try {
      await axios.delete(`/api/entries/${id}`)
      alert('删除成功')
      emit('entry-deleted')
    } catch (error) {
      alert('删除失败')
      console.error(error)
    }
  }
  </script>
  
  <style scoped>
  .edit-form {
    margin-top: 20px;
    border: 1px solid #ccc;
    padding: 10px;
  }
  .edit-form form {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }
  .edit-form label {
    flex: 1 1 150px;
    display: flex;
    flex-direction: column;
  }
  .edit-form button {
    padding: 6px 12px;
    cursor: pointer;
    margin-right: 10px;
  }
  </style>