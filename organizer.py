import os
import shutil

# Define the folder categories and extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Code": [".py", ".cpp", ".js", ".java"],
    "Others": []
}

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            moved = False
            for category, extensions in FILE_TYPES.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    category_path = os.path.join(folder_path, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_path, filename))
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(folder_path, "Others")
                os.makedirs(other_path, exist_ok=True)
                shutil.move(file_path, os.path.join(other_path, filename))

if __name__ == "__main__":
    folder = input("Enter full path of the folder to organize: ").strip()
    if os.path.isdir(folder):
        organize_files(folder)
        print("Files organized successfully.")
    else:
        print("Invalid folder path.")
