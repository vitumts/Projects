@echo off

:: ===========================================
::  🔧 BACKEND — CONTROLE DE AMBIENTE
:: ===========================================
:: Se não estiver rodando dentro do Windows Terminal,
:: relança o próprio .bat dentro do WT para manter
:: UTF-8, estilo e layout correto.
:: ===========================================
if not defined WT_SESSION (
    wt cmd /k ""%~f0""
    exit
)

:: Força UTF-8 para suportar emojis
chcp 65001 >nul

:: Título da janela
title 🧮 Validador de Nosso Número

:: ===========================================
::  🎨 FRONTEND — MENU PRINCIPAL
:: ===========================================
:menu
cls
echo.
echo ===========================================
echo   🧮  VALIDADOR DE NOSSO NUMERO
echo ===========================================
echo.
echo   🏦 1 - Banco BMP
echo   🏦 2 - Banco VORTX
echo.
echo   ❌ 0 - Sair
echo.
set /p banco=👉 Escolha o banco: 

:: ===========================================
::  🔧 BACKEND — VALIDAÇÃO DA OPÇÃO
:: ===========================================
if "%banco%"=="1" goto bmp
if "%banco%"=="2" goto vortx
if "%banco%"=="0" exit

echo.
echo ❌ Opcao invalida! Digite apenas 1, 2 ou 0.
echo ⏳ Retornando ao menu...
timeout /t 2 >nul
goto menu

:: ===========================================
::  🏦 BMP
:: ===========================================
:bmp
cls
echo ===========================================
echo   🏦 BMP - Validação de Nosso Número
echo ===========================================
echo.
:: Chama o Python interno da pasta Validador_DV
"%~dp0python\python.exe" "%~dp0bmp.py"
goto menu

:: ===========================================
::  🏦 VORTX
:: ===========================================
:vortx
cls
echo ===========================================
echo   🏦 VORTX - Validação de Nosso Número
echo   📌 Carteira: 21 (padrão)
echo ===========================================
echo.
:: Chama o Python interno da pasta Validador_DV
"%~dp0python\python.exe" "%~dp0vortx.py"
goto menu