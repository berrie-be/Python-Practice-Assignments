import sys, os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python my_script.py <argument1> <argument2>")
        sys.exit(1)

arg1 = sys.argv[1]
arg2 = sys.argv[2]

src_dir = arg1
des_dir = arg2

if not (os.path.exists(src_dir) and os.path.exists(des_dir)):
    raise Exception("Source or Destination path doesnt exist")

else:
    folder_path = src_dir
    entries = os.listdir(folder_path)

    for entry in entries:
        full_src_path = os.path.join(folder_path, entry)
        if os.path.isfile(full_src_path):
            full_dest_path = os.path.join(des_dir,entry)
            with open(full_src_path, 'r') as f:
                content = f.read()
                with open(full_dest_path, 'w') as file:
                    file.write(content)
        else:
            continue


