import sys
import subprocess

def import_library(library_name, package_name=None):
    """Dynamically import a library, installing it if needed"""
    if package_name is None:
        package_name = library_name
    try:
        return __import__(library_name)
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", package_name], check=True)
        return __import__(library_name)

def format_exc(e):
    """Format exception for display"""
    import traceback
    return f"Error: {type(e).__name__}: {str(e)}\n{traceback.format_exc()}"
