@echo off
echo hello to pubios commands  systemfolder boot name id color vol tree date time check type hh recovery ping media mstcs iexplorer
:x
title Puhist bios 1.0
color 1f
) 
set /p x="RECOVERY>"
)
if %x%==systemfolder (cmd
)
if %x%==color (color 4c
)
if %x%==name (set /p b=username
)
if %x%==id (echo your id 20150106
)
if %x%==tree (tree&&echo your programs=%s%
)
if %x%==vol (echo your volume=%vol%
)
if %x%==boot (set /p f=drive status
)
if %x%==helpcenter (type center.txt
)
if %x%==recovery (start recovery.bat
)
if %x%==hh (start hh.exe
)
if %x%==type (start cttune.exe
)
if %x%==check (winsat
)
if %x%==date (date
)
if %x%==time (time
)
if %x%==ping (ping not.com
)
if %x%==media (start ehshell.exe
)
if %x%==mstcs (start taskmgr.exe
)
if %x%==iexplorer (iexplorer
)
pause
goto x

