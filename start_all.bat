@echo off
title TikTok Follower System

cd /d C:\Users\mike\Desktop\tiktok-followers

echo Starter follower updater...
start "" cmd /c auto_update.bat

timeout /t 2 >nul

echo Starter webserver...
start "" cmd /c python -m http.server 8000

timeout /t 2 >nul

echo Åbner dashboard...
start http://localhost:8000

echo Systemet kører.
pause
