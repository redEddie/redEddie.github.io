import os


def create_index_html(folder_path):
    with open(os.path.join(folder_path, "index.html"), "w") as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html>\n")
        f.write("<head>\n")
        f.write("<title>{}</title>\n".format(os.path.basename(folder_path)))
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("<ul>\n")
        for root, dirs, files in os.walk(folder_path):
            level = root.replace(folder_path, '').count(os.sep)
            indent = "&emsp;" * 4 * (level)
            if level == 0:
                parent_dir = os.path.dirname(os.path.abspath(folder_path))
                f.write('<li><a href="{}">../</a></li>\n'.format(parent_dir))
            else:
                f.write('{}<li>{}</li>\n'.format(indent, os.path.basename(root)))
            subindent = "&emsp;" * 4 * (level + 1)
            for file in files:
                file_path = os.path.join(root, file)
                f.write(
                    '{}<li><a href="{}">{}</a></li>\n'.format(subindent, file_path, file))
        f.write("</ul>\n")
        f.write("</body>\n")
        f.write("</html>")
    print("index.html created at", os.path.abspath(folder_path))


folder_path = "./"
create_index_html(folder_path)
