import datetime
import os
from html import escape


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


def add_css(main_text, startpath):
    # css를 추가하는 함수 for toggle
    add_css = ""
    l = 0
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        k = 0
        for file in files:
            add_css += "#toggle-folder-{}-{} {{cursor: pointer; font-weight: bold; text-decoration: underline;}}\n".format(
                l, k)
            k += 1
            # print(str(k) + css)
        l += 1
    css_in_text = main_text

    css_in_text += add_css
    print(css_in_text)
    print("======== css done =========")
    return css_in_text


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
