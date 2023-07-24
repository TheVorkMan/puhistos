Set objShell = CreateObject("WScript.Shell")

' Путь к файлу DLL, который нужно зарегистрировать
dllPath = "OS\system.dll"

' Зарегистрировать DLL с помощью Regsvr32
objShell.Run "regsvr32 /s """ & dllPath & """"

Set objShell = Nothing