import glob
import re
import os

files = glob.glob('e:/OfficeDownloads_/MayJuneWebsite/Fan_Fiction_Writing_Community/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    content = re.sub(r'(?<=class=)[\'"]([^\'"]*?)bg-dark text-white([^\'"]*?)[\'"]', r'\"\1\2\"', content)
    
    content = content.replace('<p class=\"text-light\">', '<p class=\"text-muted\">')
    content = content.replace('<p class=\"text-light', '<p class=\"text-muted')
    content = content.replace('<p class=\"fst-italic text-light flex-grow-1\">', '<p class=\"fst-italic text-muted flex-grow-1\">')
    content = content.replace('bg-dark text-white', '')
    
    if original != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {os.path.basename(filepath)}')
