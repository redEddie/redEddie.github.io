import os


def create_index_html(folder_path):
    with open(os.path.join(folder_path, "index.html"), "w") as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html>\n")
        f.write("<head>\n")
        f.write("<title>{}</title>\n".format(os.path.basename(folder_path)))
        f.write("<script>\n")
        f.write('function toggle(element) {\n')
        f.write('  var ul = element.parentElement.querySelector("ul");\n')
        f.write('  if (ul) {\n')
        f.write('    if (ul.style.display === "none") {\n')
        f.write('      ul.style.display = "block";\n')
        f.write('      element.innerHTML = "&#9660; " + element.innerHTML.slice(2);\n')
        f.write('    } else {\n')
        f.write('      ul.style.display = "none";\n')
        f.write('      element.innerHTML = "&#9658; " + element.innerHTML.slice(2);\n')
        f.write('    }\n')
        f.write('  }\n')
        f.write('}\n')
        f.write("</script>\n")
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
                folder_name = os.path.basename(root)
                f.write(
                    '<li>{}<span onclick="toggle(this)">&#9658; {}</span>\n'.format(indent, folder_name))
                f.write('{}  <ul style="display:none">\n'.format(indent))
            subindent = "&emsp;" * 4 * (level + 1)
            for file in files:
                file_path = os.path.join(root, file)
                f.write(
                    '<li>{}<a href="{}">{}</a></li>\n'.format(subindent, file_path, file))
            if level != 0:
                f.write('{}</ul>\n'.format(indent))
                f.write('{}</li>\n'.format(indent))
        f.write("</ul>\n")
        f.write("</body>\n")
        f.write("</html>")
    print("index.html created at", os.path.abspath(folder_path))


folder_path = "./files/"
create_index_html(folder_path)
