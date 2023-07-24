@echo off
:menu
chcp 866 > nul
echo 1 - Показать список запущенных процессов
echo 2 - Завершить процесс по имени
echo 3 - Показать информацию о системе
echo 4 - Выход

set /p choice=Выберите опцию:
if "%choice%"=="1" (
    tasklist
    goto menu
) 
if "%choice%"=="2" (
    set /p processName=Введите имя процесса для завершения:
    taskkill /f /im %processName%
    goto menu
) 
if "%choice%"=="3" (
    systeminfo
    goto menu
) 
if "%choice%"=="4" (
    exit
) else (
    echo Неверный выбор. Пожалуйста, выберите снова.
    goto menu
)