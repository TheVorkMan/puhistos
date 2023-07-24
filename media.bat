@echo off
title Медиаплеер
echo Please enter the music
set /p sum=music file
echo ----------------------------
dir /s /b|find "%sum%"
echo ----------------------------
start wmplayer.exe