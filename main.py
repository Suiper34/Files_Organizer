from os import listdir, makedirs, path
import shutil
from collections import defaultdict

FILE_CATEGORIES = {
    'images': {
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'
    },

    'documents': {
        '.pdf', '.doc', '.docx', '.txt', '.rtf', '.ppt', '.pptx', '.odt',
        '.ods'
    },
    'videos': {
        '.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm', '.mpeg'
    },

    'audio': {'.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'},

    'archives': {'.zip', '.rar', '.7z', '.tar', '.gz'},

    'code': {
        '.py', '.js', '.html', '.css', '.java', '.c', '.cpp', '.ts', '.php'
    },

    'executables': {'.exe', '.msi', '.bat', '.sh', '.apk', '.dmg'},

    'spreadsheets': {'.csv', '.tsv', '.xls', '.xlsx'},

    'design': {'.psd', '.ai', '.indd', '.xd', '.sketch'}
}


def detect_category(extension: str) -> str:
    """
    Return the file category name for a given file extension.

    Parameters
    ----------
    extension : str
        The file extension to look up (e.g. 'txt' or '.TXT'). Comparison is
        performed case-insensitively using extension.lower() against the
        extensions stored in the global FILE_CATEGORIES mapping.

    Returns
    -------
    str
        The matching category name from FILE_CATEGORIES.
        If no matching extension is found, returns the string 'others'.

    """
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category

    return 'others'


def organize_files_by_extension(
    source_dir: str,
    destination_dir: str
) -> None:
    """
    Move files from source_dir into categorized folders inside destination_dir
    based on common file extensions.
    """

    try:
        if not path.isdir(source_dir):
            raise FileNotFoundError('Source directory not found:', source_dir)

        makedirs(destination_dir, exist_ok=True)
        moved_counts = defaultdict(int)

        for filename in listdir(source_dir):
            source_path: str = path.join(source_dir, filename)

            if not path.isfile(source_path):
                continue  # skip directories and non-files

            _, extension = path.splitext(filename)
            if not extension:
                category = 'others'

            else:
                category: str = detect_category(extension)

            category_folder: str = path.join(destination_dir, category)
            makedirs(category_folder, exist_ok=True)

            destination_path: str = path.join(category_folder, filename)
            shutil.move(source_path, destination_path)
            moved_counts[category] += 1

            print(f'Moved: {source_path} -> {destination_path}')

        if moved_counts:
            print('\nSummary:')

            for category, count in moved_counts.items():
                print(f'  {category.capitalize()}: {count} file(s)')

        else:
            print('No files were moved. Check if the source directory is empty')

    except (FileNotFoundError, PermissionError, OSError) as fnfe_pe_ose:
        print(f'Error while organizing files: {fnfe_pe_ose}')
