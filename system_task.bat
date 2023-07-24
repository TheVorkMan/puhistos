@echo off
setlocal enabledelayedexpansion

set input_file=data.txt
set output_file=output.txt

REM Очистка выходного файла перед записью
echo. > %output_file%

REM Чтение и обработка данных из входного файла
for /f "tokens=*" %%a in (%input_file%) do (
    set line=%%a
    REM Добавление обработки для каждой строки данных
    echo Processed: !line! >> %output_file%
)

echo Done! Обработанные данные записаны в %output_file%.

endlocal