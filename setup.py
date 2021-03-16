from cx_Freeze import *

includefiles = ["mini.ico"]
excludes = []
packages = []
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut",  # shortcut
     "DesktopFolder",  # directory
     "management",  # name
     "TARGETDIR",  # component
     "[TARGETDIR]\management.exe",  # target
     None,  # arguments
     None,  # description
     None,  # hotkey
     None,  # icon
     None,  # iconindex
     None,  # showcmd
     "TARGETDIR",  # wkdir
     )
]

msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {'data': msi_data}
setup(
    version="0.1",
    description="Management system developed by Mahima Choudhary",
    author="Mahima Choudhary",
    name="Management system",
    options={'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables=[
        Executable(
            script="management.py",
            base=base,
            icon='mini.ico',
        )
    ]
)