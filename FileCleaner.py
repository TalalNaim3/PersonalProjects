import os
import datetime

# Replace 'your_directory_path' with the path to the directory containing the files
directory_path = r"C:\Users\Talal\OneDrive\Pictures\Renaming_python_testfiles"

def rename_files(directory_path):
    # Get today's date in the format YYYY-MM-DD
    creation_time = os.path.getctime(file_path)

    # List all files in the directory
    files = os.listdir(directory_path)

    # Iterate through each file
    for file_name in files:
        # Construct the new file name with lowercase and date
        new_file_name = f"{creation_time}_{file_name.lower()}"

        # Construct the full paths
        old_path = os.path.join(directory_path, file_name)
        new_path = os.path.join(directory_path, new_file_name)

        # Rename the file
        os.rename(old_path, new_path)

        print(f"Renamed: {file_name} -> {new_file_name}")



# Call the function to rename files
rename_files(directory_path)
