from src.File_Organizer.organizer import FileOrganizer
from utils.logger import get_logger
import argparse

logger = get_logger(__name__)

def main():

    parser = argparse.ArgumentParser(description = "Organize files in a given source directory based on the file extensions")

    parser.add_argument('source_dir', type = str, 
                        help = 'Path to source directory')
    
    parser.add_argument('--dry-run', action = 'store_true',
                        help = 'Perform a dummy run without actually moving the files')
    
    args = parser.parse_args()

    if not args.source_dir:
        logger.error('Source directory path is empty. Please provide a valid path.')
        return
    
    organize = FileOrganizer(args.source_dir)
    files = organize.list_files()
    if not files:
        logger.error('No files found in the source directory. Exiting the program.')
        return

    extensions = organize.get_extensions(files)
    if not extensions:
        logger.error('No valid extensions found. Exiting the program.')
        return

    organize.create_folders(extensions)
    organize.move_files(files=files, dry_run=args.dry_run) #--dry-run auto converts to dry_run by argparse
    

if __name__ == "__main__":
    main()
