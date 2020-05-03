@echo off
mongo "mongodb+srv://b7fun-2ldf3.mongodb.net/B7FunDb"  --username B7Fun --password B7FunDb --eval load('InsertData.js')
pause
