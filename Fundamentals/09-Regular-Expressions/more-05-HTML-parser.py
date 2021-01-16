import re
text = input()

title_pattern = r'(?<=<title>).*?(?=</title>)'
title = re.findall(title_pattern, text)

raw_content_pattern = r'(?<=<body>).*?(?=</body>)'
raw_content = re.findall(raw_content_pattern, text)
raw_content = ''.join(raw_content)

content = re.sub(r'(<[^<>]*>)|(\\.)', '', raw_content)

print(f"Title: {''.join(title)}")
print(f"Content: {content}")