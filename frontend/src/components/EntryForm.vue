<template>
  <form @submit.prevent="submitEntry" class="entry-form">
    <label>
      类型:
      <select v-model="type">
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
      <select v-model="category" required>
        <option v-for="cat in categories" :key="cat" :value="cat">{{ cat }}</option>
      </select>
    </label>

    <label class="note-label">
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
import { ref, computed, watch, defineEmits } from 'vue'
import axios from 'axios'

const incomeCategories = ['工资', '奖金', '投资收益', '其他收入']
const expenseCategories = ['买菜', '交通', '娱乐', '水电煤', '其他支出']

const type = ref('expense')
const amount = ref(null)
const category = ref('')
const note = ref('')
const date = ref(new Date().toISOString().slice(0, 10))

const categories = computed(() => {
  return type.value === 'income' ? incomeCategories : expenseCategories
})

watch(type, (newType) => {
  category.value = newType === 'income' ? incomeCategories[0] : expenseCategories[0]
}, { immediate: true })

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
    type.value = 'expense'
    amount.value = null
    category.value = expenseCategories[0]
    note.value = ''
    date.value = new Date().toISOString().slice(0, 10)
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
  gap: 12px;
  align-items: center;
}

.entry-form label {
  white-space: nowrap; /* 防止标签和输入框换行 */
  display: flex;
  align-items: center;
  gap: 6px;
}

.entry-form input[type="text"],
.entry-form input[type="number"],
.entry-form input[type="date"],
.entry-form select {
  min-width: 120px;
  padding: 4px 6px;
  box-sizing: border-box;
}

/* 备注输入框宽度稍大 */
.note-label input[type="text"] {
  min-width: 200px;
}
</style>