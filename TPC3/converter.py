import re
import os
import webbrowser

def check_heading(line : str) -> str:
    pattern = re.compile(r'^\s*(#{1,6})\s+(.*)$')
    match = pattern.match(line)
    if match:
        level = len(match.group(1))
        heading = match.group(2)
        return re.sub(pattern, f'<h{level}>{heading}</h{level}>', line)
    return line

def check_bold(line : str) -> str:
    pattern = re.compile(r'\*\*(.*)\*\*')
    return re.sub(pattern, r'<b>\1</b>', line)

def check_italic(line : str) -> str:
    pattern = re.compile(r'(?<!\*)\*(?!\*)(.*)(?<!\*)\*(?!\*)')
    return re.sub(pattern, r'<i>\1</i>', line)

def check_list(line : str, checking_list : bool) -> (bool, str):
    pattern = re.compile(r'^\s*\d+\.\s+(.*)$')
    match = pattern.match(line)

    if match:
        list_item = match.group(1)
        line = re.sub(pattern, f'<li>{list_item}</li>', line)
        if not checking_list:
            checking_list = True
            line = '<ol>\n' + line 
    else:
        if checking_list:
            checking_list = False
            line = '</ol>\n' + line
    
    return checking_list, line

def check_link(line : str) -> str:
    pattern = re.compile(r'(?<!!)\[(.*)\]\((.*)\)')
    return re.sub(pattern, r'<a href="\2">\1</a>', line)

def check_image(line : str) -> str:
    pattern = re.compile(r'!\[(.*)\]\((.*)\)')
    return re.sub(pattern, r'<img src="\2" alt="\1"/>', line)

def markdown_to_html(markdown_text : str) -> str:
    html_lines = []
    checking_list = False
    lines = markdown_text.split('\n')
    for line in lines:
        html_line = check_heading(line)
        html_line = check_italic(html_line)
        html_line = check_bold(html_line)
        checking_list, html_line = check_list(html_line, checking_list)
        html_line = check_link(html_line)
        html_line = check_image(html_line)
        
        html_lines.append(html_line)

    return '\n'.join(html_lines)


def main():
    markdown_text = """
    # Header 1
    ## Header 2
    ### Header 3

    This is a **bold** text and this is an *italic* text.

    1. First item
    2. Second item

    Here is a [link](https://example.com).

    Here is an image: ![alt text](image.jpg)
    """

    html_output = markdown_to_html(markdown_text)
    print(html_output)
    print('')
    
    op = input('Open the HTML file in the browser? (y/n): ')
    if op.lower() == 'y':
        path = os.path.abspath('temp.html')
        url = 'file://' + path

        with open(path, 'w') as f:
            f.write(html_output)
        webbrowser.open(url)

if __name__ == '__main__':
    main()