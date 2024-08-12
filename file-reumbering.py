import os
import re

def add_leading_zero(directory):
    for filename in os.listdir(directory):
        match = re.match(r'^(\d{2})\.\s(.+)$', filename)
        if match:
            new_name = f"0{filename}"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} to {new_name}")

# Replace 'your_directory_path' with the path to your directory
add_leading_zero('.')