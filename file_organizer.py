
import os
import shutil


def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    # File type categories
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
        "Audio": [".mp3", ".wav"],
        "Videos": [".mp4", ".mkv", ".mov"],
        "Archives": [".zip", ".rar"],
        "Scripts": [".py", ".js", ".java", ".c", ".cpp"],
    }

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if file.lower().endswith(tuple(extensions)):
                    folder_name = os.path.join(folder_path, folder)
                    os.makedirs(folder_name, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_name, file))
                    print(f"✅ Moved: {file} → {folder}/")
                    moved = True
                    break

            if not moved:
                others_folder = os.path.join(folder_path, "Others")
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, file))
                print(f"📂 Moved: {file} → Others/")


def main():
    folder_path = input("Enter the folder path to organize: ")
    organize_folder(folder_path)


if __name__ == "__main__":
    main()
