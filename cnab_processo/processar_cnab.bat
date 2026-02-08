@echo off
:: ===========================================
:: 🔧 BACKEND — CONTROLE DE AMBIENTE
:: ===========================================
chcp 65001 > nul
title 🧮 Processar CNAB 400 - Bradesco

:: ===========================================
:: Força execução na pasta do BAT
:: ===========================================
cd /d "%~dp0"

:: ===========================================
:: Pastas
:: ===========================================
set "PASTA_ORIGEM=cnab_origem"
set "PASTA_SAIDA=cnab_saida"

if not exist "%PASTA_SAIDA%" mkdir "%PASTA_SAIDA%"

:: ===========================================
:: Valida pasta de origem
:: ===========================================
if not exist "%PASTA_ORIGEM%" (
    echo ❌ Pasta "%PASTA_ORIGEM%" nao encontrada.
    echo Crie a pasta e coloque o CNAB original dentro dela.
    pause
    exit /b 1
)

dir "%PASTA_ORIGEM%\*.txt" >nul 2>&1
if errorlevel 1 (
    echo ❌ Nenhum arquivo .txt encontrado em "%PASTA_ORIGEM%".
    pause
    exit /b 1
)

echo 📂 Pasta de origem validada.
echo.

:: ===========================================
:: Executa Python portátil
:: ===========================================
if exist ".\python\python.exe" (
    .\python\python.exe separar_cnab.py
) else (
    echo ❌ Python portátil nao encontrado em ".\python\python.exe".
    pause
    exit /b 1
)

:: ===========================================
:: Fim
:: ===========================================
pause
exit /b 0