#!/usr/bin/env python3

import os
import subprocess

# Run the data cleaning script
print("Running data cleaning...\n")
subprocess.run(["python3", "main_transactions.py"], check=True)

# Check if cleaned dataset was created
if os.path.exists("main_transactions.csv"):
    print("\nCleaned dataset found. Continuing to campaigns_metrics.py...\n")
    subprocess.run(["python3", "campaigns_metrics.py"], check=True)
else:
    print("Error: main_transactions.csv not found. Make sure main_transactions.py completed successfully.")
