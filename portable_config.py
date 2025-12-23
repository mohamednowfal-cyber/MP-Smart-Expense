"""
Portable configuration for Smart Expense Visualizer
Handles different operating systems and paths
"""

import os
import sys
import platform
from pathlib import Path

def get_portable_config():
    """Get configuration based on the current system"""
    
    # Get the directory where the script is located
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        base_dir = Path(sys._MEIPASS)
    else:
        # Running as script
        base_dir = Path(__file__).parent.absolute()
    
    config = {
        'base_dir': base_dir,
        'data_dir': base_dir / 'data',
        'reports_dir': base_dir / 'reports',
        'assets_dir': base_dir / 'assets',
        'os_name': platform.system().lower(),
        'python_version': sys.version_info,
    }
    
    # Create directories if they don't exist
    for dir_name in ['data_dir', 'reports_dir', 'assets_dir']:
        dir_path = config[dir_name]
        dir_path.mkdir(exist_ok=True)
    
    return config

def get_tesseract_path():
    """Get Tesseract OCR path based on operating system"""
    system = platform.system().lower()
    
    if system == 'windows':
        # Common Windows paths for Tesseract
        possible_paths = [
            r'C:\Program Files\Tesseract-OCR\tesseract.exe',
            r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
            r'C:\Users\{}\AppData\Local\Tesseract-OCR\tesseract.exe'.format(os.getenv('USERNAME', '')),
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
                
        # If not found, return None (will use system PATH)
        return None
        
    elif system == 'darwin':  # macOS
        possible_paths = [
            '/usr/local/bin/tesseract',
            '/opt/homebrew/bin/tesseract',
            '/usr/bin/tesseract',
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
                
        return None
        
    else:  # Linux and others
        # Try common Linux paths
        possible_paths = [
            '/usr/bin/tesseract',
            '/usr/local/bin/tesseract',
            '/snap/bin/tesseract',
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
                
        return None

def setup_environment():
    """Setup environment variables for portable operation"""
    config = get_portable_config()
    
    # Set Tesseract path if found
    tesseract_path = get_tesseract_path()
    if tesseract_path:
        os.environ['TESSDATA_PREFIX'] = str(Path(tesseract_path).parent)
        # Add to PATH if not already there
        current_path = os.environ.get('PATH', '')
        if str(Path(tesseract_path).parent) not in current_path:
            os.environ['PATH'] = f"{Path(tesseract_path).parent};{current_path}"
    
    return config

# Auto-setup when imported
PORTABLE_CONFIG = setup_environment()

# Export commonly used paths
DATA_DIR = PORTABLE_CONFIG['data_dir']
REPORTS_DIR = PORTABLE_CONFIG['reports_dir']
ASSETS_DIR = PORTABLE_CONFIG['assets_dir']
BASE_DIR = PORTABLE_CONFIG['base_dir']
