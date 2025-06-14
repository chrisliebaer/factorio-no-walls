#!/usr/bin/env python3
"""
Build script for Factorio mod compatible with mods.factorio.com
Creates a zip file excluding .git and other unnecessary files.
"""

import os
import json
import zipfile
import sys
from pathlib import Path

def get_mod_info():
    """Read mod info from info.json"""
    try:
        with open("info.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: info.json not found. Make sure you're running this from the mod directory.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing info.json: {e}")
        sys.exit(1)

def should_exclude(path):
    """Check if a file or directory should be excluded from the zip"""
    exclude_patterns = {
        ".git",
        ".gitignore",
        "__pycache__",
        "*.pyc",
        "build_mod.py",
        "*.zip",
    }
    
    path_str = str(path)
    path_name = path.name
    
    # Check if any exclude pattern matches
    for pattern in exclude_patterns:
        if pattern.startswith("*."):
            # Wildcard pattern
            if path_name.endswith(pattern[1:]):
                return True
        elif pattern in path_str or path_name == pattern:
            return True
    
    return False

def create_mod_zip():
    """Create the mod zip file"""
    mod_info = get_mod_info()
    mod_name = mod_info["name"]
    mod_version = mod_info["version"]
    
    zip_filename = f"{mod_name}_{mod_version}.zip"
    
    print(f"Building mod: {mod_name} v{mod_version}")
    print(f"Output file: {zip_filename}")
    
    # Remove existing zip if it exists
    if os.path.exists(zip_filename):
        os.remove(zip_filename)
        print(f"Removed existing {zip_filename}")
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through all files in the current directory
        for root, dirs, files in os.walk('.'):
            # Remove excluded directories from dirs list to prevent walking into them
            dirs[:] = [d for d in dirs if not should_exclude(Path(root) / d)]
            
            for file in files:
                file_path = Path(root) / file
                
                # Skip excluded files
                if should_exclude(file_path):
                    continue
                
                # Create archive path (remove leading ./ or .\)
                archive_path = str(file_path).replace('.\\', '').replace('./', '')
                
                # Add file to zip
                zipf.write(file_path, f"{mod_name}/{archive_path}")
                print(f"Added: {archive_path}")
    
    print(f"\nMod zip created successfully: {zip_filename}")
    print(f"Ready for upload to mods.factorio.com")

if __name__ == "__main__":
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    create_mod_zip()
