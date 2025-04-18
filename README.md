# 简易记账软件

## 项目说明

这是一个简化版的记账软件，包含添加、编辑、删除账目，分类管理和账目列表展示功能。  
不包含预算管理和身份验证。

## 技术栈

- 后端：Flask + SQLite
- 前端：Vue 3 + Vite + Axios

## 运行步骤

### 后端

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
后端默认运行在 http://127.0.0.1:5000

前端
cd frontend
npm install
npm run dev
前端默认运行在 http://localhost:5173