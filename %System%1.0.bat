@echo off
start update_notifications.vbs
echo select a Q for off system S for start system C for activate system
set /p var=
)
if %var%==Q (exit
)
if %var%==S (echo system a start
)
if %var%==C (set /p code=activation code
)
if %var%==CD (echo System_page=Puhist
)
title Puhist Dos 2.0
start BEEP.BAT
color 2
echo Loading...
timeout /t 2 >nul
echo ......................................................................
timeout /t 1 >nul
echo ......................................................................
timeout /t 1 >nul
echo ......................................................................
timeout /t 1 >nul
echo ......................................................................
timeout /t 1 >nul
echo ......................................................................
timeout /t 1 >nul
echo loading a end

IF EXIST "C:\Users\Arsen Lupen\Desktop\OS\exp.bat" (
    echo directory exists
   cls
) ELSE (
color 17
echo.
echo error-0x00007d
echo restart os
ping -n 6 127.0.0.1 > nul
    recover c:\Users\Arsen Lupen\Desktop\OS\exp.bat
)
Echo Press any key
pause >nul
cls
echo welcome to puhist dos 2.0 x32 
color a
:x
set /p x="OS>"
)
if %x%==system (echo Puhist dos 2.0 videobox mx120
)
if %x%==help (echo help=help system=os loga=a dir=data acpi=acpi bios=bios test=test tasks=tasklist info=systeminfo data=date time=time shutdown=power off chrome=chrome anti=antivirus cls=cls host=HOSTNAME write=write settings=set media=pLayer calc=calc user=name dr=drivers vol=volume vo=soundrecorder ff=logoff g=activate hlp=help anitimeupdate=version update plugandplay=plug and play rand=random number mem=mem telnet=easter egg mss=iexpress msdos=c ping=pings dial=phone stor=discord crestik=crestiki noliki password=username update=update system copy=copy xcopy=files netsh=netsh photo=photos systemfile=regester secure_mode=setlocal scandisk=scandisk accounts=createAccount newmesage for random user hclp=creator_mail search=search file message=message for user
)
if %x%==dir (echo data
dir Puhist
)
if %x%==loga (echo a
)
if %x%==helpcenter (type center.txt
)
if %x%==productkey (type Product.txt
)
if %x%==acpi (set /p sum=acpi position
)
if %x%==bios (start bios.bat
)
if %x%==test (start testgravik.cmd
)
if %x%==tasks (tasklist
)
if %x%==info (systeminfo
)
if %x%==data (date /t
)
if %x%==time (time /t
)
if %x%==shutdown (shutdown /s /t 
)
if %x%==anti (start antivirus.bat
)
if %x%==chrome (start chrome.exe
)
if %x%==cls (cls
)
if %x%==media (start media.bat
)
if %x%==calc (start calculate.bat
)
if %x%==write (echo press alt in notepad for managment notepad&&edit
)
if %x%==settings (set /p sum=Settings
)
if %x%==host (hostname
)
if %x%==user (ECHO %USERNAME%
)
if %x%==cmd (WHOAMI /USER
)
if %x%==co (MEM
)
if %x%==ui (DEBUG
)
if %x%==dr (driverquery
)
if %x%==restart (shutdown /r
)
if %x%==gb (shutdown /h
)
if %x%==tree (tree
)
if %x%==vol (vol
)
if %x%==gift (set /p gift code=gift code
)
if %x%==ff (logoff
)
if %x%==vo (start Soundrecorder.exe
)
if %x%==g (slmgr /xpr
)
if %x%==d (type description
)
if %x%==hlp (start help.bat
)
if %x%==anitimeupdate (echo select a version os&&set /p p=os ver)
)
if %x%==plugandplay (set /p sys=plug and play
)
if %x%==rand (echo %random%
)
if %x%==mem (mem
)
if %x%==telnet (towel.blinkenlights.nl
)
if %x%==mss (start iexpress.exe
)
if %x%==msdos (cmd
)
if %x%==ping (ping discord.com
)
if %x%==dial (start dialer.exe
)
if %x%==stor (start https://discord.gg/dt29jAdUdd
)
if %x%==update (start update.html
)
if %x%==copy (copy %filename%
)
if %x%==xcopy (xcopy %filename%
)
if %x%==netsh (netsh
)
if %x%==systemfile (start system.reg
)
if %x%==secure_mode (setlocal
)
if %x%==scandisk (chkdsk A: /f
)
if %x%==accounts (net user john /add /profilepath:A:\UCC
)
if %x%==newmessage (msg *Уведомление От John=Ха я занят не могу сейчас*
)
if %x%==hclp (echo creator mail=arsenijgoj282@gmail.com
)
if %x%==search (set /p search_query=Please enter the search:
dir /s /b "*%search_query%*"
)
if %x%==message (set /p message=Введите сообщение для уведомления:
msg *%message%*
)
goto x 