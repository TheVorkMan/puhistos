@echo off 
title calculate
color 03
:start 
echo ___________________
echo Welcome to the calculate
echo ___________________
echo.
set /p sum=Please enter the question
echo.
set /a ans= %sum%
echo.
echo The answer =%ans%
echo.
echo ___________________
pause
cls
echo Previos Answer =%ans%
echo ___________________
echo.
goto start 
exit