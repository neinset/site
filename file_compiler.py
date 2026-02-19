import os
import re

# ===== USER SETTINGS =====
folder_path = r"C:\Users\User\site\images\boards\phase-1"
start_number = 0     # If you want to start at 002, use integer 2
padding = 3           # 3 → 003 format
# =========================

def extract_leading_number(filename):
    match = re.match(r'^(\d+)', filename)
    return int(match.group(1)) if match else None

# Get PNG files
files = [f for f in os.listdir(folder_path) if f.lower().endswith(".png")]

# Keep only files starting with digits
numbered_files = []
for f in files:
    num = extract_leading_number(f)
    if num is not None:
        numbered_files.append((f, num))

# Sort by leading numeric value
numbered_files.sort(key=lambda x: x[1])

# ---- Pass 1: Rename to temporary names ----
temp_files = []
for i, (filename, _) in enumerate(numbered_files):
    old_path = os.path.join(folder_path, filename)
    temp_name = f"__temp__{i}.png"
    temp_path = os.path.join(folder_path, temp_name)
    os.rename(old_path, temp_path)
    temp_files.append(temp_name)

# ---- Pass 2: Rename sequentially ----
for i, temp_name in enumerate(temp_files):
    new_number = start_number + 1 + i
    new_filename = f"{new_number:0{padding}d}.png"

    old_path = os.path.join(folder_path, temp_name)
    new_path = os.path.join(folder_path, new_filename)

    os.rename(old_path, new_path)

print("Renaming complete.")
