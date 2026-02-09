@echo off
cd /d "C:\Users\admin\source\repos\Python-API-Postgres"
echo Настройка Git...
git init
echo # Visual Studio > .gitignore
echo .vs/ >> .gitignore
echo __pycache__/ >> .gitignore
echo *.pyc >> .gitignore
echo venv/ >> .gitignore
git add .
git commit -m "Initial commit: Python API для работы с PostgreSQL"
echo Готово! Теперь подключите удаленный репозиторий.
pause