import datetime
import os
from html import escape


def list_files(html, startpath, exclude_this_files):
    """
    폴더 내의 모든 파일을 트리 형식으로 출력하는 함수
    """
    html = html
    html += "<ul>"
    l = 0
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = "&nbsp;&nbsp;" * 4 * level
        html += '<div id = "toggle_folder_{}" > {}{}{}/</div>\n'.format(l, indent,
                                                                        "&#x1F4C1;&nbsp;", escape(os.path.basename(root)))
        # 파일은 제외할 키워드가 포함되면 html리스트에 표시되지 않음.
        subindent = "&nbsp;&nbsp;" * 4 * (level + 1)
        # k = 0
        html += '<div id = "folder_content_{}" style="display:none;">\n'.format(
                l)
        for file in files:
            for key in exclude_this_files:
                if key in file:
                    continue
                else:
                    if escape(os.path.basename(root)) == "":
                        html += '<a href = ".{}/{}">'.format(
                            escape(os.path.basename(root)), escape(file))
                    else:
                        html += '<a href = "./{}/{}">'.format(
                            escape(os.path.basename(root)), escape(file))
                    html += '{}{}{}\n'.format(subindent,
                                              "&#x1F4C4;&nbsp;", escape(file))
                    html += '</a> </br>'
            # k += 1
        html += '</div>\n'
        l += 1
    html += "</ul>"
    return html


def add_css(main_text, startpath):
    # css를 추가하는 함수 for toggle
    add_css = ""
    l = 0
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        add_css += "#toggle_folder_{} {{cursor: pointer; font_weight: bold; text_decoration: underline;}}\n".format(
            l)
        l += 1
    css_in_text = main_text

    css_in_text += add_css
    print(css_in_text)
    print("======== css done =========")
    return css_in_text


def add_script(html, startpath):
    html = html
    l = 0
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        html += 'var toggleFolder_{} = document.getElementById("toggle_folder_{}");\n'.format(
            l, l)
        html += 'var folderContent_{} = document.getElementById("folder_content_{}");\n'.format(
                l, l)
        html += 'toggleFolder_{}.addEventListener("click", function() {}\n'.format(
            l, "{")
        html += 'if (folderContent_{}.style.display === "none") {}\n'.format(l, "{")
        html += 'folderContent_{}.style.display = "block"\n'.format(l)
        html += '}\n'
        html += 'else {\n'
        html += 'folderContent_{}.style.display = "none"\n'.format(l)
        html += '}\n'
        html += '});\n'
        l += 1

    return html


print("========{}=======".format(datetime.datetime.now()))
# main starts
main_text = "<html>"

# 파일트리 시작점, 생성점 지정
startpath = "./files/"
exclude_this_files = [".DS_Store"]


# css 추가
main_text += "<style>"
main_text = add_css(main_text, startpath)
main_text += "</style>"
# 본문
main_text += "<body>"
main_text = list_files(main_text, startpath, exclude_this_files)
main_text += "</body>"
# javascript 추가
main_text += "<script>"
main_text = add_script(main_text, startpath)
main_text += "</script>"

# main ended
main_text += "</html>"

# html 파일 만들기
folder_path = "./files/"
with open(os.path.join(folder_path, "index.html"), "w") as f:
    f.write(main_text
            )

print("===========================")
print("index.html starts at", os.path.abspath(startpath))
print("index.html created at", os.path.abspath(folder_path))
print("===========================")


'''
// Get the toggle_folder element
var toggleFolder = document.getElementById("toggle_folder");

// Get the folder_content element
var folderContent = document.getElementById("folder_content");

// Add an event listener for the toggle_folder element
toggleFolder.addEventListener("click", function() {
    // If the folder_content element is hidden, show it
    if (folderContent.style.display === "none") {
        folderContent.style.display = "block";
    }
    // If the folder_content element is visible, hide it
    else {
        folderContent.style.display = "none";
    }
});
'''


'''
<script>
    // Get all elements with the toggle_folder class
    var toggleFolders = document.querySelectorAll(".toggle_folder");

    // Add event listeners to all toggle_folder elements
    toggleFolders.forEach(function (toggleFolder) {
        // Get the next sibling element with the folder_content class
        var folderContent = toggleFolder.nextElementSibling;

        // Add an event listener for the toggle_folder element
        toggleFolder.addEventListener("click", function () {
            // If the folder_content element is hidden, show it
            if (folderContent.style.display === "none") {
                folderContent.style.display = "block";
            }
            // If the folder_content element is visible, hide it
            else {
                folderContent.style.display = "none";
            }
        });
    });
</script>'''
