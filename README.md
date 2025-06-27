# RAM Stress Test 💾

A simple Python script to stress test your computer’s RAM by continuously allocating large chunks of memory.

# ✨ Features
Repeatedly allocate large strings to consume RAM

Customize chunk size and delay between allocations via command-line arguments

Handles out-of-memory errors and user interruptions gracefully

# 🛠 Requirements
Python 3.x

# 🚀 Usage
Run the script with default settings (allocates 1 GB chunks as fast as possible):

python ram_stress_test.py

Command-line options
-s, --size : Size in bytes of each memory chunk to allocate. Default is 1000000000 (1 GB)

-d, --delay : Delay in seconds between allocations. Default is 0 (no delay)

# 🛑 How to stop the script
Press Ctrl+C (or Cmd+C on Mac) in the terminal to stop the test safely.

The script also stops automatically if it runs out of memory and raises a MemoryError.


# Examples:

Allocate 100 MB chunks without delay:

python ram_stress_test.py -s 100000000

Allocate 500 MB chunks with 1 second delay between each allocation:

python ram_stress_test.py -s 500000000 -d 1

# ⚠️ Warning
This script will use a large amount of RAM and may cause your system to slow down, freeze, or crash. Use with caution and at your own risk.

# 📜 Disclaimer
For educational and testing purposes only. Do not use this script for malicious or harmful activities.



