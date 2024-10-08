import os

def get_folder_size(folder_path):
    """
    Calculates the total size of all files in the specified folder.
    :param folder_path: Path to the folder
    :return: Total size in bytes
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if not os.path.islink(file_path):  # Skip symbolic links
                total_size += os.path.getsize(file_path)
    return total_size

def format_size(size_in_bytes):
    """
    Formats the size in bytes to a human-readable format (e.g., MB, GB).
    :param size_in_bytes: Size in bytes
    :return: Formatted size string
    """
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    index = 0
    while size_in_bytes >= 1024 and index < len(suffixes) - 1:
        size_in_bytes /= 1024.0
        index += 1
    return f"{size_in_bytes:.2f} {suffixes[index]}"

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    total_bytes = get_folder_size(folder_path)
    formatted_size = format_size(total_bytes)
    print(f"Total folder size: {formatted_size}")
