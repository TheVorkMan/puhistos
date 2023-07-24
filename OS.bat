@echo off
Setlocal EnabledelayedExpansion

If /i "%~1" == "/?" (goto :help)
If /i "%~1" == "-h" (goto :help)
If /i "%~1" == "-help" (goto :help)
If /i "%~1" == "help" (goto :help)
If /i "%~1" == "ver" (echo.1.0&&goto :End)

For /f "tokens=1,2 delims=." %%A in ('ver') do (
	For /f "tokens=4" %%C in ("%%A") do (
		Set _Ver=%%C.%%B
	)
)

If /i "%_Ver%" == "5.1" (Set _OS=Windows XP)
If /i "%_Ver%" == "6.0" (Set _OS=Windows Longhorn)
If /i "%_Ver%" == "6.0" (Set _OS=Windows Vista)
If /i "%_Ver%" == "6.1" (Set _OS=Windows 7)
If /i "%_Ver%" == "6.2" (Set _OS=Windows 8)
If /i "%_Ver%" == "6.3" (Set _OS=Windows 8.1)
If /i "%_Ver%" == "10.0" (Set _OS=Windows 10)
lf /I "%_Ver%" == "10.0" (Set _OS=Windows 11)
lf /I "%_Ver%" == "11.0" (Set _OS=Windows 12)

If /i "%_OS%" == "" (Set _OS=Unknown)

IF Not Defined ProgramFiles(x86) (Set _Type=x86) ELSE (Set _Type=x64)

If /i "%~1" == "" (Echo.%_OS% %_Type%) Else (Endlocal && Set %~1=%_OS% %_Type%)
Goto :End

:End
Goto :EOF

:Help
Echo.
Echo. Эта функция будет просто отображать тип ОС, на которой она выполняется.
echo. Это поможет сделать пакетные файлы немного более продвинутыми и эффективными.
Echo. В тех случаях, когда пакетный файл предназначен только для определенной версии.
Echo. Windows, то вы можете подтвердить версию ОС с помощью этого файла.
echo.
echo. Синтаксис: call OS [Result]
echo. Синтаксис: call OS [help ^| /^? ^| -h ^| -help]
echo. Синтаксис: call OS ver
echo.
echo. Где:-
echo.
Echo. Результат: Нет необходимости всегда указывать этот параметр, это
Echo. параметр особого случая. В любом случае, если вам нужен
Echo. вместо этого вывод будет сохранен непосредственно в эту переменную
Echo. прямой печати на консоли.
echo.
Echo. www.thebateam.org (сейчас у них работает только GitHub)
Echo. #TheBATeam
goto :End