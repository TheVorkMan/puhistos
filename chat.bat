@echo off
setlocal

:chat
set /p user_input=Write: 
echo Otvet "%user_input%"!
chcp 65001 >nul
goto chat

endlocal