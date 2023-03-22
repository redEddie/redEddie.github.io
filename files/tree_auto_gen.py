import os
from html import escape


def add_css(html, startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        k = 0
        for file in files:
            toggle_css = "#toggle-folder-{}-{} { cursor: pointer; font-weight: bold; text-decoration: underline;}".format(
                level, k)
            html += toggle_css
            k += 1
    return html


def list_files(html, startpath, exclude_this_files):
    """
    폴더 내의 모든 파일을 트리 형식으로 출력하는 함수
    """
    html = html
    html += "<ul>"
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = "&nbsp;&nbsp;" * 4 * level
        html += "<div>{}{}{}/</div>".format(indent,
                                            "&#x1F4C1;&nbsp;", escape(os.path.basename(root)))
        # 파일은 제외할 키워드가 포함되면 html리스트에 표시되지 않음.
        subindent = "&nbsp;&nbsp;" * 4 * (level + 1)
        for file in files:
            for key in exclude_this_files:
                if key in file:
                    continue
                else:
                    html += "<div>{}{}{}</div>".format(subindent,
                                                       "&#x1F4C4;&nbsp;", escape(file))
    html += "</ul>"
    return html


# main starts
html = "<html>"

# 파일트리 시작점, 생성점 지정
startpath = "./files/"
exclude_this_files = [".DS_Store"]

# css 추가
html += "<css>"
add_css(html, startpath)
html += "</css>"
# 본문
html += "<body>"
html = list_files(html, startpath, exclude_this_files)
html += "</body>"

# main ended
html += "</html>"

# html 파일 만들기
folder_path = "./files/"
with open(os.path.join(folder_path, "index.html"), "w") as f:
    f.write(html)

print("===========================")
print("index.html starts at", os.path.abspath(startpath))
print("index.html created at", os.path.abspath(folder_path))
print("===========================")
