import sys
from pathlib import Path
from PyInstaller import __main__ as pyi

SCRIPT_PATH = Path(__file__).resolve().parent

ASSETS_PATH = SCRIPT_PATH / "assets/frame0"

OUTPUT_PATH = SCRIPT_PATH / "dist"

OUTPUT_PATH.mkdir(exist_ok=True)

# 执行 PyInstaller 的命令行参数列表
pyinstaller_args = [
    "--onefile",
    "--windowed",
    f"--distpath={OUTPUT_PATH}",
    "--add-data", f"{ASSETS_PATH};assets/frame0"
]

# 添加入口文件路径
pyinstaller_args.append("entry_point.py")

# 调用 PyInstaller 运行打包命令
pyi.run(pyi_args=pyinstaller_args)

