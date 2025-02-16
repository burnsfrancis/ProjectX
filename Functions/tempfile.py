import os
import shutil

def delete_temp_files():
    # Define the temporary directories to clean
    temp_dirs = [
        os.path.join(os.environ["SystemRoot"], "Temp"),
        os.path.join(os.environ["LOCALAPPDATA"], "Temp")
    ]

    # Iterate through the temporary directories and delete files
    for temp_dir in temp_dirs:
        if not os.path.exists(temp_dir):
            print(f"Directory does not exist: {temp_dir}")
            continue

        print(f"Cleaning directory: {temp_dir}")
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    shutil.rmtree(dir_path)
                    print(f"Deleted directory: {dir_path}")
                except Exception as e:
                    print(f"Failed to delete {dir_path}: {e}")

    print("Temporary files cleanup complete.")