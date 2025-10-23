#!/usr/bin/env python3
"""
Simple launcher for the Article Research Tool
"""

import subprocess
import sys
import os

if __name__ == "__main__":
    main_file = os.path.join("src", "main.py")
    cmd = [sys.executable, "-m", "streamlit", "run", main_file, "--server.port", "8501"]
    subprocess.run(cmd)
