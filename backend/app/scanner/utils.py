import os


def get_all_files(target_dir, extensions=None):
    files_list = []

    for root, _, files in os.walk(target_dir):
        for file in files:
            if extensions:
                if any(file.endswith(ext) for ext in extensions):
                    files_list.append(os.path.join(root, file))
            else:
                files_list.append(os.path.join(root, file))

    return files_list