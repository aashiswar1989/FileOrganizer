from utils.logger import get_logger
from utils.helper import create_folder
from pathlib import Path
import shutil

class FileOrganizer:
    def __init__(self, source_dir: str):
        self.source_dir = Path(source_dir)
        self.logger = get_logger(__name__)

    def list_files(self) -> list:
        if not self.source_dir.is_dir():
            self.logger.error(f'Source directory {self.source_dir.name} does not exist')
            return []
        
        files = list(self.source_dir.glob("*"))
        self.logger.info("Listed all files in the given source directory")
        return files
    
    def get_extensions(self, files: list) -> set:
        extensions = set(file.suffix for file in files)
        self.logger.info("Retrieved the extension of all files in the given source directory")
        return extensions
    
    def create_folders(self, extensions: set):
        for ext in extensions:
            if ext in ['.jpg', '.jpeg', '.png', '.gif']:
                folder_name = 'Images'
            elif ext in ['.pdf', '.docx', '.txt', 'xlsx', '.csv', '.pptx']:
                folder_name = 'Documents'
            elif ext in ['.mp4', '.avi', '.mkv', '.mov']:
                folder_name = 'Videos'
            elif ext in ['.mp3', '.wav', '.aac']:
                folder_name = 'Audio'
            elif ext in ['.zip', '.rar', '.tar', '.gz']:
                folder_name = 'Archives'
            else:
                folder_name = 'Others'
            
            folder_path = self.source_dir/folder_name
            create_folder(folder_path)

    def move_files(self, files: list):
        for file in files:
            ext = file.suffix
            if ext in ['.jpg', '.jpeg', '.png', '.gif']:
                folder_name = 'Images'
            elif ext in ['.pdf', '.docx', '.txt', 'xlsx', '.csv', '.pptx']:
                folder_name = 'Documents'
            elif ext in ['.mp4', '.avi', '.mkv', '.mov']:
                folder_name = 'Videos'
            elif ext in ['.mp3', '.wav', '.aac']:
                folder_name = 'Audio'
            elif ext in ['.zip', '.rar', '.tar', '.gz']:
                folder_name = 'Archives'
            else:
                folder_name = 'Others'

            destination_dir = self.source_dir/folder_name
            destination_path = destination_dir/file.name
            self.logger.info(f'Destination path for file {file.name} is {destination_path}')

            shutil.move(str(file), str(destination_path))
            self.logger.info(f"File {file.name} moved from {self.source_dir.name} to {destination_dir.name}")

