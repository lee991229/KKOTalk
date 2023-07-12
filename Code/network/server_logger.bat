@ECHO OFF
FOR /F "delims=" %%i IN ('netstat -ano ^|findstr 9999') DO set server_status=%%i
set today=%date%
set now=%time%
echo %date% %time% %server_status% >> C:\Users\KDT107\Desktop\KKOTalk\log.txt
exit