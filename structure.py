from pathlib import Path

PROJECT_NAME = "File_Organizer"

file_list = [
    f'src/{PROJECT_NAME}/__init__.py',
    f'src/{PROJECT_NAME}/organizer.py',
    'utils/__init__.py',
    'utils/logger.py',
    'main.py'
]

for file_path in file_list:
    file, parent = Path(file_path), Path(file_path).parent

    if not parent.is_dir():
        parent.mkdir(parents=True, exist_ok=True)

    if not file.exists():
        file.touch(exist_ok=True)