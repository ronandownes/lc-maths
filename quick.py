#!/usr/bin/env python3
"""
LC Maths Quick Build & View3
Run this from anywhere - it handles everything automatically
"""

import subprocess
import sys
from pathlib import Path

# Configuration
PROJECT_DIR = Path(r"E:\maths\lc-maths")
PYTHON_PATH = Path(r"C:\Users\ronan\anaconda3\envs\pretext\python.exe")

def run_pretext_command(*args):
    """Run a pretext command"""
    cmd = [str(PYTHON_PATH), "-m", "pretext"] + list(args)
    print(f"Running: {' '.join(cmd)}")
    print("-" * 60)
    result = subprocess.run(cmd, cwd=PROJECT_DIR)
    print()
    return result.returncode

def main():
    """Main function"""
    
    # Check project exists
    if not PROJECT_DIR.exists():
        print(f"Error: Project directory not found: {PROJECT_DIR}")
        return 1
    
    if not (PROJECT_DIR / "project.ptx").exists():
        print(f"Error: project.ptx not found in {PROJECT_DIR}")
        return 1
    
    print("=" * 60)
    print("LC Maths - Quick Build & View")
    print("=" * 60)
    print(f"Project: {PROJECT_DIR}")
    print()
    
    # Simple menu
    print("Choose an option:")
    print("  1. Quick view (no rebuild) - FASTEST")
    print("  2. Build and view (default)")
    print("  3. Full rebuild (with asset generation)")
    print("  4. Build PDF")
    print()
    
    choice = input("Enter choice (1-4, or just press Enter for quick view): ").strip()
    
    # Default to quick view if no input
    if not choice:
        choice = "1"
    
    print()
    
    if choice == "1":
        # Just view - fastest option
        print("Opening existing build in browser...")
        run_pretext_command("view", "web")
        
    elif choice == "2":
        # Standard build and view
        print("Building web version...")
        returncode = run_pretext_command("build", "web", "--no-generate")
        if returncode == 0:
            print("✓ Build successful! Opening browser...")
            run_pretext_command("view", "web")
        else:
            print("✗ Build failed!")
            return 1
            
    elif choice == "3":
        # Full rebuild with assets
        print("Full rebuild with asset generation...")
        returncode = run_pretext_command("build", "web", "-g")
        if returncode == 0:
            print("✓ Build successful! Opening browser...")
            run_pretext_command("view", "web")
        else:
            print("✗ Build failed!")
            return 1
            
    elif choice == "4":
        # Build PDF
        print("Building PDF version...")
        run_pretext_command("build", "print")
        
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
