@echo off
REM PreTeXt Build Helper for LC Maths
REM This uses the correct Python environment

set PYTHON=C:\Users\ronan\anaconda3\envs\pretext\python.exe

if "%1"=="" (
    echo Usage: pretext.bat [command]
    echo Examples:
    echo   pretext.bat build web
    echo   pretext.bat build print
    echo   pretext.bat view web
    echo   pretext.bat generate
    exit /b
)

%PYTHON% -m pretext %*
