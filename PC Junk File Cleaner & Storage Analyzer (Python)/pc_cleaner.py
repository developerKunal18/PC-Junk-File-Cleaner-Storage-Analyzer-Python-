import os
import shutil
from pathlib import Path

JUNK_PATHS = [
    Path.home() / "AppData/Local/Temp",     # Windows temp
    Path("/tmp"),                           # Linux/macOS temp
    Path.home() / ".cache",                 # User cache
]

def get_size(start_path):
    total = 0
    for dirpath, _, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total += os.path.getsize(fp)
    return total

def format_size(size):
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def scan_junk():
    print("\n🔎 Scanning for junk files...\n")
    total = 0
    for p in JUNK_PATHS:
        if p.exists():
            folder_size = get_size(p)
            print(f"{p} → {format_size(folder_size)}")
            total += folder_size
    print(f"\n🧹 Total junk detected: {format_size(total)}")
    return total

def clean_junk():
    print("\n🧹 Cleaning junk...\n")
    for p in JUNK_PATHS:
        if p.exists():
            try:
                shutil.rmtree(p)
                p.mkdir(parents=True, exist_ok=True)
                print(f"✔ Cleared {p}")
            except Exception:
                print(f"⚠ Skipped (permission denied): {p}")
    print("\n✨ Cleanup complete!")

def menu():
    while True:
        print("\n🧹 PC Cleaner & Storage Analyzer")
        print("1️⃣ Scan Junk Files")
        print("2️⃣ Clean Junk Files")
        print("3️⃣ Exit")

        choice = input("\nChoose: ").strip()
        if choice == "1":
            scan_junk()
        elif choice == "2":
            clean_junk()
        elif choice == "3":
            print("\n👋 Goodbye! Stay optimized!")
            break
        else:
            print("❌ Invalid Option!")

if __name__ == "__main__":
    menu()
