@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION
FOR /F "delims=" %%i IN ('netstat -ano ^|findstr 9999') DO set server_status=%%i
echo %server_status% > C:\Users\KDT115\Desktop\KKOTalk\server_status.txt

ENDLOCAL
exit