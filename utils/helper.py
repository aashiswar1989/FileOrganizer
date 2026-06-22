from utils.logger import get_logger
from pathlib import Path

logger = get_logger(__name__)

def create_folder(folder_path: Path):
        if folder_path.exists():
                logger.info(f'Folder {folder_path.name} already exists. Skipping folder creation')

        else:
            folder_path.mkdir(parents=True, exist_ok=True)
            logger.info(f'Folder {folder_path.name} created successfully')