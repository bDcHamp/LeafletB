import os
import zipfile
from pathlib import Path
from datetime import datetime

# Patterns to exclude
EXCLUDE_PATTERNS = {
    'venv/',
    'venv\\',
    '__pycache__',
    '.env',
    '.git/',
    '.git\\',
    '.gitignore',
    '.vscode/',
    '.vscode\\',
    '.idea/',
    '.idea\\',
    '*.pyc',
    '*.pyo',
    '*.pyd',
    '*.so',
    '*.sqlite3',
    '*.sqlite3-bak',
    '*.log',
    'debug.log',
    'livingarchive.log',
    'livingarchive.pid',
    'prodlivingarchive.log',
    'nohup.out',
    'test.log',
    'media/',
    'media\\',
    'staticfiles/',
    'staticfiles\\',
    '.DS_Store',
    'Thumbs.db'
}

def should_exclude(path):
    """Check if the path should be excluded based on patterns"""
    path_str = str(path)
    return any(
        exclude in path_str or 
        path_str.endswith(exclude.rstrip('/').rstrip('\\')) or
        (exclude.startswith('*.') and path_str.endswith(exclude[1:]))
        for exclude in EXCLUDE_PATTERNS
    )

def create_zip():
    # Get current directory
    current_dir = Path.cwd()
    
    # Create zip filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    zip_filename = f'LeafletBuild_{timestamp}.zip'
    
    # Create a new zip file
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(current_dir):
            # Convert to Path objects
            root_path = Path(root)
            
            # Remove directories we want to exclude
            dirs[:] = [d for d in dirs if not should_exclude(root_path / d)]
            
            # Add files that shouldn't be excluded
            for file in files:
                file_path = root_path / file
                if not should_exclude(file_path):
                    # Get the relative path
                    relative_path = file_path.relative_to(current_dir)
                    print(f"Adding: {relative_path}")
                    zipf.write(file_path, relative_path)
    
    print(f"\nZip file created: {zip_filename}")
    print(f"Location: {current_dir / zip_filename}")
    print("\nRemember to tell your friend to:")
    print("1. Create a new virtual environment")
    print("2. Create their own .env file")
    print("3. Run migrations")
    print("4. Create a superuser account")

if __name__ == '__main__':
    create_zip()