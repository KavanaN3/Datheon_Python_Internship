
import os
import shutil

def organize_files(folder_path):
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".doc", ".txt"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Audio": [".mp3", ".wav"],
        "Python_Files": [".py"],
        "Others": []
    }

    if not os.path.isdir(folder_path):
        print("Folder does not exist!")
        return

    moved_count = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()

        category = "Others"

        for folder, extensions in categories.items():
            if extension in extensions:
                category = folder
                break

        destination_folder = os.path.join(folder_path, category)
        os.makedirs(destination_folder, exist_ok=True)

        destination_path = os.path.join(destination_folder, filename)

        # Avoid overwriting files with the same name
        if os.path.exists(destination_path):
            print(f"Skipped duplicate file: {filename}")
            continue

        try:
            shutil.move(file_path, destination_path)
            print(f"Moved {filename} to {category}")
            moved_count += 1

        except PermissionError:
            print(f"Permission denied: {filename}")

        except OSError as error:
            print(f"Could not move {filename}: {error}")

    print("\nFile organization completed!")
    print("Total files moved:", moved_count)


if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ").strip().strip('"')
    organize_files(folder)
