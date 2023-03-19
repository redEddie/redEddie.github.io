import os
from html import escape


def list_files(startpath):
    """
    폴더 내의 모든 파일을 트리 형식으로 출력하는 함수
    """
    html = "<ul>"
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = "&nbsp;&nbsp;" * 4 * level
        html += "{}<li>{}{}/</li>".format(indent,
                                          "&#x1F4C1;&nbsp;", escape(os.path.basename(root)))
        subindent = "&nbsp;&nbsp;" * 4 * (level + 1)
        for file in files:
            html += "{}<li>{}{}</li>".format(subindent,
                                             "&#x1F4C4;&nbsp;", escape(file))
    html += "</ul>"
    return html


# 사용 예시
startpath = "."
html = list_files(startpath)
print(html)
