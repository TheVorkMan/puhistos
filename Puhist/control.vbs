Set objShell = CreateObject("WScript.Shell")

' ќткрываем панель управлени€
objShell.Run "control"

' ∆дем, пока пользователь не закроет панель управлени€
WScript.Sleep 90000

' «акрываем панель управлени€
objShell.AppActivate "Control Panel"
objShell.SendKeys "%{F4}"

Set objShell = Nothing