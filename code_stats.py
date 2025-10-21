import os
from collections import defaultdict

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def scan_directory(directory):
    stats = defaultdict(lambda: {'files': 0, 'lines': 0})
    total_files = 0
    total_lines = 0

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower() or 'no_ext'

            total_files += 1
            lines = count_lines_in_file(file_path)
            total_lines += lines

            stats[ext]['files'] += 1
            stats[ext]['lines'] += lines

    return stats, total_files, total_lines

def print_stats(stats, total_files, total_lines):
    print("\n📊 Code Stats Summary 📊\n")
    print(f"Total Files: {total_files}")
    print(f"Total Lines: {total_lines}\n")

    print("{:<10} {:<10} {:<10}".format("EXT", "FILES", "LINES"))
    print("-" * 30)
    for ext, data in sorted(stats.items(), key=lambda x: x[1]['lines'], reverse=True):
        print("{:<10} {:<10} {:<10}".format(ext, data['files'], data['lines']))

if __name__ == "__main__":
    folder = input("📁 Enter the path to your project folder: ").strip()
    if not os.path.exists(folder):
        print("❌ Folder not found.")
    else:
        stats, total_files, total_lines = scan_directory(folder)
        print_stats(stats, total_files, total_lines)
