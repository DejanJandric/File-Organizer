import shutil
from pathlib import Path

FOLDER_MAP = {

    ".exe": "Installations",
    ".msi": "Installations",
    ".vsix": "Installations",


    ".png": "Photos",
    ".jpeg": "Photos",
    ".jpg": "Photos",
    ".gif": "Photos",
    ".svg": "Photos",


    ".mp4": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".mkv": "Videos",


    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".html": "Documents",
    ".csv": "Documents",
    ".rtf": "Documents",
}


def organize_downloads():
    DOWNLOADS_DIR = Path.home() / "Downloads"

    print(f"Starting to organize files in: {DOWNLOADS_DIR}\n")

    for folder_name in set(FOLDER_MAP.values()):
        folder_path = DOWNLOADS_DIR / folder_name
        folder_path.mkdir(exist_ok=True)
        print(f"Ensured folder exists: {folder_path}")

    print("\n--- Moving Files ---")

    files_moved = 0
    files_skipped = 0

    for item in DOWNLOADS_DIR.iterdir():
        if item.is_dir():

            if item.name not in set(FOLDER_MAP.values()):
                print(f"Skipping directory: {item.name}")
                continue

        file_suffix = item.suffix.lower()

        if file_suffix in FOLDER_MAP:
            destination_folder_name = FOLDER_MAP[file_suffix]
            destination_path = DOWNLOADS_DIR / destination_folder_name / item.name
            try:
                shutil.move(item, destination_path)
                print(f"MOVED: {item.name} -> {destination_folder_name}/")
                files_moved += 1
            except Exception as e:
                print(f"ERROR moving {item.name}: {e}")
        else:
            print(f"SKIPPED (no mapping): {item.name}")
            files_skipped += 1

            print("\n--- Summary ---")
    print(f"Organizing complete!")
    print(f"Total files moved: {files_moved}")
    print(f"Total files skipped (unmapped extension): {files_skipped}")


if __name__ == "__main__":
    organize_downloads()
