#!/usr/bin/env python3
"""
Quick rebuild script for LC Maths PreTeXt book
Run this from the lc-maths directory
"""

import subprocess
import sys
from pathlib import Path

# Path to the PreTeXt Python environment
PYTHON_PATH = r"C:\Users\ronan\anaconda3\envs\pretext\python.exe"

def run_command(cmd):
    """Run a command and display output"""
    print(f"Running: {' '.join(cmd)}")
    print("-" * 60)
    result = subprocess.run(cmd, capture_output=False, text=True)
    print()
    return result.returncode

def main():
    """Main rebuild function"""
    
    # Check we're in the right directory
    if not Path("project.ptx").exists():
        print("Error: project.ptx not found!")
        print("Make sure you're running this from E:\\maths\\lc-maths")
        return 1
    
    print("=" * 60)
    print("LC Maths PreTeXt Book Builder")
    print("=" * 60)
    print()
    
    # Ask what to build
    print("What would you like to do?")
    print("  1. Build web (HTML)")
    print("  2. Build web and view")
    print("  3. Build print (PDF)")
    print("  4. Just view existing web build")
    print()
    
    choice = input("Enter choice (1-4, default=2): ").strip() or "2"
    
    if choice == "1":
        # Build web only
        run_command([PYTHON_PATH, "-m", "pretext", "build", "web"])
        
    elif choice == "2":
        # Build and view
        returncode = run_command([PYTHON_PATH, "-m", "pretext", "build", "web"])
        if returncode == 0:
            print("Build successful! Opening browser...")
            run_command([PYTHON_PATH, "-m", "pretext", "view", "web"])
        else:
            print("Build failed. Not opening browser.")
            
    elif choice == "3":
        # Build PDF
        run_command([PYTHON_PATH, "-m", "pretext", "build", "print"])
        
    elif choice == "4":
        # Just view
        run_command([PYTHON_PATH, "-m", "pretext", "view", "web"])
        
    else:
        print(f"Invalid choice: {choice}")
        return 1
    
    print()
    print("=" * 60)
    print("Done!")
    print("=" * 60)
    return 0

if __name__ == "__main__":
    sys.exit(main())
