@echo off
echo ============================================================
echo Cleaning up project for GitHub
echo ============================================================
echo.

REM Delete generated video files
del /Q *.mp4 2>nul
del /Q *_index.json 2>nul
del /Q *_index.faiss 2>nul

REM Delete environment file
del /Q .env 2>nul

REM Delete old documentation
del /Q HOW_TO_USE_WITH_FILES.md 2>nul
del /Q QUICK_START.md 2>nul
del /Q COMPLETE_GUIDE.md 2>nul

REM Delete temporary files
del /Q fix_dependencies.py 2>nul
del /Q fix_tf_issue.py 2>nul
del /Q set_api_key.bat 2>nul
del /Q setup_google_api.bat 2>nul

REM Delete venv folder
rmdir /S /Q venv 2>nul

REM Delete user documents
del /Q documents\*.txt 2>nul
del /Q documents\*.md 2>nul
del /Q documents\*.pdf 2>nul
del /Q pdfs\*.pdf 2>nul

REM Rename new README
if exist README_NEW.md (
    del /Q README.md 2>nul
    ren README_NEW.md README.md
)

echo.
echo ============================================================
echo Cleanup complete!
echo ============================================================
echo.
echo Project is ready for GitHub!
echo See UPLOAD_TO_GITHUB.txt for next steps.
echo.
pause
