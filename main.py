from src.File_Organizer.organizer import FileOrganizer
from utils.logger import get_logger


logger = get_logger(__name__)

def main():
    source_dir = input(r'Enter the source directory path:\n')

    if not source_dir:
        logger.error('Source directory path is empty. Please provide a valid path.')
        return
    
    organize = FileOrganizer(source_dir)
    files = organize.list_files()
    if not files:
        logger.error('No files found in the source directory. Exiting the program.')
        return

    extensions = organize.get_extensions(files)
    if not extensions:
        logger.error('No valid extensions found. Exiting the program.')
        return

    organize.create_folders(extensions)
    organize.move_files(files)
    

if __name__ == "__main__":
    main()
