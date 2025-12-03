from cx_Freeze import setup, Executable
base = None

executables = [Executable("main.py", base=base)]

packages = ["idna", "pygame"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name = "Space Invaders",
    options = options,
    version = "2.5",
    description = 'Jeu vidéo Space Invaders',
    executables = executables, requires=['pygame', 'cx-freeze']
)