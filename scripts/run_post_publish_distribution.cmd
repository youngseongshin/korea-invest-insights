@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_DIR%run_post_publish_distribution.ps1" %*
exit /b %ERRORLEVEL%
