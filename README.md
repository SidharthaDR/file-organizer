A 📁 File Organizer (Python CLI Tool)

A simple and customizable command-line tool that automatically organizes files in a directory by type (e.g., Images, Documents, Code, Archives).
✨ Features

 Automatically creates folders like Images/, Documents/, Code/, etc.

 Moves files based on their extensions

 Easy to customize file types and categories

 Works on Linux and Windows (via WSL)

🚀 Usage

Clone the repo or download the script:

    git clone https://github.com/SidharthaDR/file-organizer.git

    cd file-organizer

Run the script:

    python3 organizer.py

    Enter the full path of the folder you want to organize when prompted.

    ⚠️ Files will be moved into categorized subfolders inside the given directory.

🧠 Example File Types

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Code": [".py", ".cpp", ".js", ".java"],
    "Others": []
}

You can edit this dictionary in the script to add more types.
🛠️ Requirements

    Python 3.6+

    Works in Linux, macOS, and Windows (via WSL)

📄 License

This project is open-source and free to use under the MIT License.

Author:

Made by sidhartha — feel free to reach out or fork the project!
