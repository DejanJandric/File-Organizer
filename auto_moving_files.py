import shutil
from pathlib import Path

FOLDER_MAP = {
    ".exe": "Installations", ".msi": "Installations", ".vsix": "Installations",
    ".png": "Photos", ".jpeg": "Photos", ".jpg": "Photos", ".gif": "Photos", ".svg": "Photos",
    ".mp4": "Videos", ".avi": "Videos", ".mov": "Videos", ".mkv": "Videos",
    ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents",
    ".html": "Documents", ".csv": "Documents", ".rtf": "Documents",
}


def organize_downloads(target_directory=None):
    if target_directory is None:
        target_directory = Path.home() / "Downloads"
    else:
        target_directory = Path(target_directory)

    print(f"Starting to organize files in: {target_directory}\n")

    for folder_name in set(FOLDER_MAP.values()):
        folder_path = target_directory / folder_name
        folder_path.mkdir(exist_ok=True)

    files_moved = 0
    files_skipped = 0

    for item in target_directory.iterdir():
        if item.is_dir():
            continue

        file_suffix = item.suffix.lower()

        if file_suffix in FOLDER_MAP:
            destination_folder_name = FOLDER_MAP[file_suffix]
            destination_path = target_directory / destination_folder_name / item.name
            try:
                shutil.move(str(item), str(destination_path))
                print(f"MOVED: {item.name} -> {destination_folder_name}/")
                files_moved += 1
            except Exception as e:
                print(f"ERROR moving {item.name}: {e}")
        else:
            files_skipped += 1

    return files_moved 

if __name__ == "__main__":
    organize_downloads()
