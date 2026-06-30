import re

path = 'e:/OfficeDownloads_/MayJuneWebsite/Fan_Fiction_Writing_Community/authors.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

count = 1
def repl(m):
    global count
    res = 'src="assets/images/auth/' + str(count) + '.png"'
    count += 1
    return res

new_text = re.sub(r'src="assets/images/[^"]+"', repl, text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Replaced', count - 1, 'images.')
