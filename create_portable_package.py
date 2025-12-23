#!/usr/bin/env python3
"""
Create a portable package of the Smart Expense Visualizer
This script prepares the project for USB transfer
"""

import os
import shutil
import zipfile
from pathlib import Path
import sys

def create_portable_package():
    """Create a portable package of the project"""
    
    print("🚀 Creating Portable Smart Expense Visualizer Package...")
    print("=" * 60)
    
    # Get current directory
    current_dir = Path(__file__).parent.absolute()
    package_name = "SmartExpenseVisualizer_Portable"
    package_dir = current_dir / package_name
    
    # Files and directories to include
    include_items = [
        "app.py",
        "requirements.txt",
        "setup_portable.bat",
        "run_app.bat", 
        "setup_portable.sh",
        "run_app.sh",
        "PORTABLE_README.md",
        "portable_config.py",
        "activate_env.bat",
        "components/",
        "features/",
        "utils/",
        "data/",
        "reports/",
        "assets/",
        "chatbot/",
        "cloud/",
        "ml/",
        "ocr/",
    ]
    
    # Files and directories to exclude
    exclude_items = [
        "__pycache__/",
        "*.pyc",
        "*.pyo",
        "*.pyd",
        ".git/",
        ".gitignore",
        "myenv/",  # Virtual environment (will be recreated)
        "smart_expense_visualizer/",  # Duplicate folder
        "create_portable_package.py",
        "test_data_integration.py",
        "*.log",
        ".DS_Store",
        "Thumbs.db",
    ]
    
    print(f"📁 Creating package directory: {package_dir}")
    
    # Remove existing package directory
    if package_dir.exists():
        shutil.rmtree(package_dir)
    
    # Create package directory
    package_dir.mkdir(exist_ok=True)
    
    # Copy files and directories
    copied_items = []
    for item in include_items:
        src_path = current_dir / item
        dst_path = package_dir / item
        
        if src_path.exists():
            if src_path.is_file():
                # Copy file
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_path, dst_path)
                copied_items.append(item)
                print(f"✅ Copied file: {item}")
            elif src_path.is_dir():
                # Copy directory
                shutil.copytree(src_path, dst_path, ignore=shutil.ignore_patterns(*exclude_items))
                copied_items.append(item)
                print(f"✅ Copied directory: {item}")
        else:
            print(f"⚠️  Not found: {item}")
    
    # Create a simple launcher script
    launcher_content = '''@echo off
echo ========================================
echo Smart Expense Visualizer - Portable
echo ========================================
echo.
echo This is a portable version of the Smart Expense Visualizer.
echo.
echo First time setup:
echo 1. Run setup_portable.bat
echo 2. Then run run_app.bat
echo.
echo For detailed instructions, see PORTABLE_README.md
echo.
pause
'''
    
    launcher_path = package_dir / "START_HERE.bat"
    with open(launcher_path, 'w') as f:
        f.write(launcher_content)
    
    print(f"✅ Created launcher: START_HERE.bat")
    
    # Create ZIP package
    zip_name = f"{package_name}.zip"
    zip_path = current_dir / zip_name
    
    print(f"\n📦 Creating ZIP package: {zip_name}")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_dir):
            for file in files:
                file_path = Path(root) / file
                arc_path = file_path.relative_to(package_dir)
                zipf.write(file_path, arc_path)
    
    # Calculate sizes
    package_size = sum(f.stat().st_size for f in package_dir.rglob('*') if f.is_file())
    zip_size = zip_path.stat().st_size
    
    print("\n" + "=" * 60)
    print("🎉 Portable Package Created Successfully!")
    print("=" * 60)
    print(f"📁 Package directory: {package_dir}")
    print(f"📦 ZIP file: {zip_path}")
    print(f"📊 Package size: {package_size / (1024*1024):.1f} MB")
    print(f"📦 ZIP size: {zip_size / (1024*1024):.1f} MB")
    print(f"📋 Items copied: {len(copied_items)}")
    
    print("\n🚀 Next Steps:")
    print("1. Copy the ZIP file to your USB drive")
    print("2. Extract it on any computer with Python installed")
    print("3. Run setup_portable.bat (Windows) or ./setup_portable.sh (Mac/Linux)")
    print("4. Run run_app.bat (Windows) or ./run_app.sh (Mac/Linux)")
    
    print("\n📖 For detailed instructions, see PORTABLE_README.md")
    
    return package_dir, zip_path

if __name__ == "__main__":
    try:
        package_dir, zip_path = create_portable_package()
        print(f"\n✅ Success! Package ready at: {zip_path}")
    except Exception as e:
        print(f"\n❌ Error creating package: {e}")
        sys.exit(1)
