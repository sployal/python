import os
import mimetypes

def get_file_category(file_path):
    """
    Determines the category of a file based on its MIME type.
    :param file_path: Path to the file
    :return: Category (e.g., 'PDF', 'Video', 'MP3', 'Word', 'Picture')
    """
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type:
        main_type, _ = mime_type.split('/')
        return main_type.capitalize()
    return "Unknown"

def categorize_files(folder_path):
    """
    Categorizes files in the specified folder.
    :param folder_path: Path to the folder
    :return: Dictionary with file categories as keys and lists of file names as values
    """
    categorized_files = {}
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            category = get_file_category(file_path)
            categorized_files.setdefault(category, []).append(filename)
    return categorized_files

def display_categorized_files(categorized_files):
    """
    Displays categorized files in a vertical format with numbering.
    :param categorized_files: Dictionary with file categories and lists of file names
    """
    print("File Categories:")
    for i, (category, files) in enumerate(categorized_files.items(), start=1):
        print(f"{i}. {category}:")
        for j, file_name in enumerate(files, start=1):
            print(f"   {j}. {file_name}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    categorized_files = categorize_files(folder_path)
    display_categorized_files(categorized_files)
