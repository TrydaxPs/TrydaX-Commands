@echo off
title "TrydaX Tool Nuker [Commands] | Made By Trydax"

python3 TrydaX.py

if errorlevel 1 (
    python TrydaX.py
)

pause
