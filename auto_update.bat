@echo off
cd /d C:\Users\mike\Desktop\tiktok-followers

:loop
python tracker.py
timeout /t 60
goto loop
