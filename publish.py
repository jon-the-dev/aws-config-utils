#!/usr/bin/env python3
"""Script to help with publishing to PyPI."""

import subprocess
import sys
import os


def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"\n{description}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error: {description} failed")
        print(f"Command: {cmd}")
        print(f"Error output: {result.stderr}")
        return False
    
    print(f"✓ {description} completed successfully")
    if result.stdout.strip():
        print(result.stdout)
    return True


def main():
    """Main publishing workflow."""
    print("AWS Config Utils - PyPI Publishing Script")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("setup.py") or not os.path.exists("aws_config_utils"):
        print("Error: Please run this script from the project root directory")
        return 1
    
    # Clean previous builds
    if not run_command("rm -rf build/ dist/ *.egg-info/", "Cleaning previous builds"):
        return 1
    
    # Run tests
    if not run_command("python -m pytest tests/ -v", "Running tests"):
        print("Warning: Tests failed. Continue anyway? (y/N)")
        if input().lower() != 'y':
            return 1
    
    # Build the package
    if not run_command("python -m build", "Building package"):
        return 1
    
    # Check the package
    if not run_command("python -m twine check dist/*", "Checking package"):
        return 1
    
    print("\n" + "=" * 50)
    print("Package built successfully!")
    print("\nNext steps:")
    print("1. Test upload to TestPyPI:")
    print("   python -m twine upload --repository testpypi dist/*")
    print("\n2. If test upload works, upload to PyPI:")
    print("   python -m twine upload dist/*")
    print("\n3. Install and test:")
    print("   pip install aws-config-utils")
    print("   aws-config-utils --help")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
