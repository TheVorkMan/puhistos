Set objShell = CreateObject("WScript.Shell")

' Создаем окно сообщения
msg = "Компьютер завис! Что будем делать?"

' Выводим окно сообщения
objShell.Popup msg, 0, "Компьютер завис!", 48

Set objShell = Nothing