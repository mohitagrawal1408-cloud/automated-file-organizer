import os

def create_test_environment():
    folder_name = "test_folder"
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # A list of fake files representing a messy Downloads folder
    dummy_files = [
        "biology_notes.txt", 
        "monthly_budget.csv", 
        "final_report.pdf",
        "profile_pic.jpg", 
        "website_logo.png", 
        "project_presentation.pptx",
        "podcast_episode.mp3", 
        "funny_cat_video.mp4", 
        "game_installer.exe",
        "backup_files.zip", 
        "weird_file.unknown"
    ]

    print(f"Creating test environment in '{folder_name}'...\n")

    # Generate each fake file
    for filename in dummy_files:
        file_path = os.path.join(folder_name, filename)
        
        # Open the file in 'write' mode to create it, write a tiny bit of text, and close it
        with open(file_path, 'w') as f:
            f.write("This is a dummy file for testing purposes.")
            
        print(f"📄 Created: {filename}")

    print("\n✅ Test folder is ready! You can now run your organizer script.")

if __name__ == "__main__":
    create_test_environment()
