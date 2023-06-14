@echo off
setlocal

set PROJECT_ROOT=%~dp0
set ZIP_FILE=%PROJECT_ROOT%\my-deployment.zip

@REM rem Verifica se o arquivo .gitignore existe
@REM if exist "%PROJECT_ROOT%\.gitignore" (
    rem Cria o arquivo .zip excluindo os arquivos listados no .gitignore
    "%PROGRAMFILES%\7-Zip\7z.exe" a -r -tzip "%ZIP_FILE%" "%PROJECT_ROOT%\*" -xr@="%PROJECT_ROOT%.gitignore"
@REM ) else (
@REM     rem Cria o arquivo .zip sem excluir nenhum arquivo
@REM     "%PROGRAMFILES%\7-Zip\7z.exe" a -r -tzip "%ZIP_FILE%" "%PROJECT_ROOT%\*"
@REM )

@REM echo Arquivo zip criado em: %ZIP_FILE%

@REM endlocal
