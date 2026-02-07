# File Organizer

A simple, automated file organization tool that intelligently categorizes and sorts files in your Downloads folder by file type.

## Overview

**File Organizer** automatically scans your Downloads folder and organizes files into categorized subdirectories based on their file extensions. It helps keep your Downloads folder clean and organized without manual effort.

## Features

- **Automatic File Categorization**: Organizes files into:
  - **Images** (.jpg, .jpeg, .png)
  - **Documents** (.pdf, .docx, .txt)
  - **Videos** (.mp4)
  - **Others** (unrecognized file types)

- **Easy to Use**: Simple one-command execution
- **Automatic Folder Creation**: Creates necessary folders if they don't exist
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

### Option 1: Run as Python Script

1. **Prerequisites**: Ensure Python 3.x is installed on your system
2. **Clone the repository**:
   ```bash
   git clone https://github.com/Nirmalakhadka18/File_Organizer.git
   cd File_Organizer
   ```
3. **Run the script**:
   ```bash
   python file_organizer.py
   ```

### Option 2: Run as Standalone Executable

1. Download `file_organizer.exe` from the [Releases](https://github.com/Nirmalakhadka18/File_Organizer/releases) page
2. Double-click to run (Windows only)

## Usage

Simply run the script:

```bash
python file_organizer.py
```

**What happens:**
- The script scans your Downloads folder (`~/Downloads`)
- Files are moved into subdirectories based on their file type
- Unrecognized file types go into the "Others" folder
- A confirmation message is displayed for each file moved
- Press Enter to exit the program

## Example Output

```
Downloads folder path is: C:\Users\YourName\Downloads
Files found: ['test.jpg', 'resume.pdf', 'video.mp4', 'image.png']
Moved: test.jpg → Images
Moved: resume.pdf → Documents
Moved: video.mp4 → Videos
Moved: image.png → Images
Organizing complete
Press Enter to exit...
```

## File Structure

```
File_Organizer/
├── file_organizer.py      # Main Python script
├── file_organizer.spec    # PyInstaller spec file
├── README.md              # This file
└── .gitignore             # Git ignore configuration
```

## Customization

To add more file types, edit the `FILE_TYPES` dictionary in `file_organizer.py`:

```python
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4"],
    "Archives": [".zip", ".rar", ".7z"],  # Add your own categories
}
```

## Building a Standalone Executable

If you want to create your own `.exe` file:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Build the executable:
   ```bash
   pyinstaller --onefile file_organizer.py
   ```
3. The `.exe` will be created in the `dist/` folder

## System Requirements

- **Python Version**: 3.6 or higher
- **Operating System**: Windows, macOS, or Linux
- **Permissions**: Read and write access to Downloads folder

## License

This project is open source. Feel free to use, modify, and distribute as needed.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements or new features.

## Support

If you encounter any issues or have suggestions, please open an issue on the [GitHub repository](https://github.com/Nirmalakhadka18/File_Organizer/issues).

## Author

Created as part of the Networkers Internship Program

---

**Made with ❤️ for a cleaner Downloads folder!**