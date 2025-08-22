import psutil
import os

# List of apps we want to automatically close.
# ⚠️ Be careful: don't add "explorer.exe" unless you really want to kill the Windows desktop.
target_programs = [
    "brave.exe",               # Brave browser
    "snippingtool.exe",        # Windows Snipping Tool
    "mspaint.exe",             # Old Paint app
    "microsoft.photos.exe",    # Modern Photos app
    "notepad.exe",             # Notepad
    "winword.exe",             # Microsoft Word
    "chrome.exe"               # Google Chrome
]

def close_targeted_programs():
    closed_programs = []
    # Loop through all running processes
    for process in psutil.process_iter(['pid', 'name']):
        try:
            name = process.info['name'].lower()
            # If the process is in our "kill list", close it
            if name in target_programs:
                psutil.Process(process.info['pid']).terminate()
                closed_programs.append(name)
                print(f"Closed: {name}")
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            # In case the process disappears too quickly or we don't have permission
            print(f"Could not close {name}: {str(e)}")
            pass
    return closed_programs

if __name__ == "__main__":
    print("Closing specified programs...")
    closed = close_targeted_programs()
    if closed:
        print("Closed programs:", ", ".join(closed))
    else:
        print("No targeted programs were found running.")
    print("Done ✅")
