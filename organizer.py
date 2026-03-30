import os
import shutil

def organize_directory(target_dir):
    # 1. Define categories and their corresponding file extensions
    categories = {
        "Images": ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
        "Archives": ['.zip', '.rar', '.tar', '.gz'],
        "Media": ['.mp4', '.mp3', '.mkv', '.wav'],
        "Executables": ['.exe', '.msi', '.dmg']
    }

    # Create a reverse mapping for easy lookup (e.g., '.jpg' -> 'Images')
    extension_map = {}
    for category, extensions in categories.items():
        for ext in extensions:
            extension_map[ext] = category

    # 2. Verify the target directory actually exists
    if not os.path.exists(target_dir):
        print(f"Error: The directory '{target_dir}' does not exist.")
        return

    print(f"Scanning directory: {target_dir}...\n")

    # 3. Loop through every item in the target directory
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)

        # Skip if the item is a folder (we only want to move files)
        if os.path.isdir(file_path):
            continue

        # Get the file extension and convert to lowercase for consistency
        name, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Determine the category, default to "Others" if not in our list
        category = extension_map.get(file_extension, "Others")

        # Create the path for the new category folder
        category_dir = os.path.join(target_dir, category)

        # Create the folder if it doesn't already exist
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)

        # Define where the file is going to be moved
        destination_path = os.path.join(category_dir, filename)

        # 4. EDGE CASE: What if a file with the same name already exists there?
        if os.path.exists(destination_path):
            # We solve this by appending '_copy' to the filename
            new_filename = f"{name}_copy{file_extension}"
            destination_path = os.path.join(category_dir, new_filename)
            print(f"⚠️  Duplicate found! Renaming '{filename}' to '{new_filename}'")

        # 5. Move the file
        try:
            shutil.move(file_path, destination_path)
            print(f"✅ Moved: {filename} -> {category}/")
        except Exception as e:
            print(f"❌ Could not move {filename}. Error: {e}")

    print("\n🎉 Organization complete!")

if __name__ == "__main__":
    # ⚠️ IMPORTANT SAFETY STEP: 
    # For your first test, do NOT use your real Downloads folder.
    # Create a folder named 'test_folder' in the same place as this script,
    # put some random copy-pasted files in it, and run the script to watch it work.
    
    folder_to_organize = "./test_folder" 
    
    organize_directory(folder_to_organize)
