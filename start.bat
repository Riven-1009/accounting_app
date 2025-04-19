@echo off
echo Starting backend...
cd backend
start /b python app.py > backend.log 2>&1
cd ..

echo Starting frontend...
cd frontend
npm install
npm run dev
pause
