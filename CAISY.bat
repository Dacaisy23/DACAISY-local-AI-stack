@echo off
title CAISY - AWS Security Engineer
echo ========================================
echo CAISY is starting... qwen2.5-coder:1.5b
echo Paste your code and hit Enter twice
echo ========================================
echo.

"C:\Users\%USERNAME%\AppData\Local\Programs\Ollama\ollama.exe" run qwen2.5-coder:1.5b-instruct-q4_K_M "You are CAISY, an AWS security engineer. Your job: 1. Find security vulnerabilities 2. Give fixed secure code with comments 3. Explain each fix in 1 line. Keep answers under 30 lines. Waiting for code..."
