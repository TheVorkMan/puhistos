Set objWMIService = GetObject("winmgmts:\\.\root\CIMV2")

Set colProcesses = objWMIService.ExecQuery("SELECT * FROM Win32_Process")

For Each objProcess in colProcesses
    WScript.Echo "Process Name: " & objProcess.Name
Next

strProcessName = InputBox("Введите имя процесса, который вы хотите завершить")

Set colProcessList = objWMIService.ExecQuery("SELECT * FROM Win32_Process WHERE Name='" & strProcessName & "'")

If colProcessList.Count > 0 Then
    For Each objProcess in colProcessList
        objProcess.Terminate()
    Next
    WScript.Echo "Процесс '" & strProcessName & "' был завершен"
Else
    WScript.Echo "Процесс с именем '" & strProcessName & "' не найден"
End If