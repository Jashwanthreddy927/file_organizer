import os
import shutil
import streamlit as st

# Define file extensions for categorization
file_categories = {
    'Documents': ['.txt', '.pdf', '.docx', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Others': []  # For any file type that doesn't fit in the above categories
}

def organize_files(directory_path):
    files = os.listdir(directory_path)
    logs = []
    
    for file in files:
        file_path = os.path.join(directory_path, file)
        
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            categorized = False
            
            for category, extensions in file_categories.items():
                if file_extension in extensions:
                    category_folder = os.path.join(directory_path, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, file))
                    logs.append(f"Moved: {file} to {category}/")
                    categorized = True
                    break
            
            if not categorized:
                other_folder = os.path.join(directory_path, 'Others')
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))
                logs.append(f"Moved: {file} to Others/")
    
    return logs

def main():
    st.title("📂 File Organizer")
    st.write("Organize your files into categories based on their types.")
    
    directory_path = st.text_input("Enter the folder path:")
    
    if directory_path and os.path.isdir(directory_path):
        st.success(f"Selected Folder: {directory_path}")
        
        if st.button("Organize Files"):
            logs = organize_files(directory_path)
            st.write("### File Organization Log:")
            st.text_area("Logs", "\n".join(logs), height=300)
            st.success("File organization completed successfully!")
    else:
        st.warning("Please enter a valid folder path.")

if __name__ == "__main__":
    main()
