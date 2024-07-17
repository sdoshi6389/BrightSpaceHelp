@echo off

node index.js

@echo on
call myenv\Scripts\activate.bat
set FLASK_APP=app.py
set FLASK_ENV=development
start /B flask run
timeout /t 5 /nobreak > nul
start http://localhost:5000
pause
