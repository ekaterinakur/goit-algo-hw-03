from pathlib import Path
import shutil
import sys

def copy_files(src_dir, dest_dir='dist'):
    try:
        Path(dest_dir).mkdir(parents=True, exist_ok=True)

        for item in Path(src_dir).iterdir():
            if item.is_dir():
                copy_files(item, dest_dir)
            elif item.is_file():
                file_extension = item.suffixes[-1]
								
                ext_dir = Path(dest_dir) / file_extension[1:]
                ext_dir.mkdir(parents=True, exist_ok=True)

                new_file_path = ext_dir / item.name

                shutil.copy2(item, new_file_path)
                print(f"Copied '{item.name}' to '{ext_dir}'")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_directory = None

    if len(sys.argv) < 2:
        print("Usage: python test_1.py source_directory [destination_directory]")

        use_test_dir = input("Do you want to use test dirs? (y/n) ")
        if use_test_dir == 'y':
            test_directory = 'test_dir'
        else:
            sys.exit(1)

    source_directory = test_directory if bool(test_directory) else Path(sys.argv[1])
    destination_directory = Path(sys.argv[2]) if len(sys.argv) > 2 else 'dist'

    copy_files(source_directory, destination_directory)
