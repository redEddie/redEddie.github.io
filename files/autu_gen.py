import os


def create_folder_tree(folder_path):
    tree_html = ''
    for root, dirs, files in os.walk(folder_path):
        level = root.replace(folder_path, '').count(os.sep)
        indent = '&nbsp;&nbsp;&nbsp;' * 2 * (level)
        tree_html += '{}<i>{}/</i><br>'.format(indent, os.path.basename(root))
        sub_indent = '&nbsp;&nbsp;&nbsp;' * 2 * (level + 1)
        for f in files:
            tree_html += '{}{}<br>'.format(sub_indent, f)
    with open('folder_tree.html', 'w') as f:
        f.write(tree_html)
    print('HTML file successfully created!')


# folder_path = input('Enter folder path: ')
folder_path = "./files/"
create_folder_tree(folder_path)
