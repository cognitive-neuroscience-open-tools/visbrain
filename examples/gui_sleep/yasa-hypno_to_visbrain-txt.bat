@echo on
:: =============== config per project =======================
set PROJECT_DIR=D:\Documents\GitHub_listplot3d\visbrain
set EXEC_PATH=%PROJECT_DIR%\examples\gui_sleep\yasa-hypno_to_visbrain-txt.py

:: ===== only need to validate check points ============
set ANACONDA_DIR=D:\SW\anaconda3
set CONDA_ENV=py312  &:: :<<<<<<<<<<<<<< check point 1

:: 
chcp 65001

call %ANACONDA_DIR%\Scripts\activate.bat %ANACONDA_DIR%
call conda activate %CONDA_ENV%

set PYTHONPATH=%PROJECT_DIR%;%PYTHONPATH%
python %EXEC_PATH%  &:: :<<<<<<<<<<<<<< check point 2
pause 
