
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["pyqrcode", "png"], "excludes": []}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(
    name="QR_generator",
    version="0.1",
    description="QR_Generator",
    options={"build_exe": build_exe_options},
    executables=[Executable("QRCodegenerator.py", base = None)], # 이곳에서 오류 발생 base = base 를 base = None으로 변경해주니 해결
)
