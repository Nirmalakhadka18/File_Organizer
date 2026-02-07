import os
import shutil

# Automatically detect Downloads folder
DOWNLOADS_PATH = os.path.join(os.path.expanduser("~"), "Downloads")

print("Downloads folder path is:", DOWNLOADS_PATH)

# File types
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4"],
}

def organize_files():

    files = os.listdir(DOWNLOADS_PATH)

    print("Files found:", files)

    if not files:
        print("No files found in Downloads folder")
        return

    for filename in files:

        file_path = os.path.join(DOWNLOADS_PATH, filename)

        if os.path.isfile(file_path):

            ext = os.path.splitext(filename)[1].lower()

            moved = False

            for folder, extensions in FILE_TYPES.items():

                if ext in extensions:

                    folder_path = os.path.join(DOWNLOADS_PATH, folder)

                    os.makedirs(folder_path, exist_ok=True)

                    shutil.move(file_path, os.path.join(folder_path, filename))

                    print("Moved:", filename, "→", folder)

                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(DOWNLOADS_PATH, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print("Moved:", filename, "→ Others")

    print("Organizing complete")

organize_files()

input("Press Enter to exit...")
