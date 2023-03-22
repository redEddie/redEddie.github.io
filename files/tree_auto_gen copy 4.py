import os
from html import escape


def add_css(html):
    togglecss = "#toggle-folder { cursor: pointer; font-weight: bold; text-decoration: underline;}"
    html += togglecss
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


# 기본 html 구조 설정
html = "<html>"
html += "<css>"
add_css(html)
html += "</css>"

# 파일트리 만들기 시작
startpath = "../"
exclude_this_files = ".DS_Store"
html = list_files(html, startpath, exclude_this_files)
# print(html)

html += "</html>"

# html 파일 만들기
folder_path = "./"
with open(os.path.join(folder_path, "index.html"), "w") as f:
    f.write(html)
