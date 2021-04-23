import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["common", "logs", "client", "unit_tests"],
}
setup(
    name="Denis_mess_client",
    version="1.0.0",
    options={
        "build_exe": build_exe_options
    },
    executables=[Executable('client.py',
                            # Чтобы убрать консоль, разкоментировать строку:
                            # base='Win32GUI',
                            targetName='client.exe',
                            )]
)
