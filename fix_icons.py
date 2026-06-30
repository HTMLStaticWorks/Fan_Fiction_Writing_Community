import sys

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'writer-stories.html' in filepath:
        content = content.replace('Fandom: My Hero Academia &nbsp;\ufffd&nbsp;', 'Fandom: My Hero Academia &nbsp;&bull;&nbsp;')
        content = content.replace('Fandom: Harry Potter &nbsp;\ufffd&nbsp;', 'Fandom: Harry Potter &nbsp;&bull;&nbsp;')
        content = content.replace('Fandom: Original Work &nbsp;\ufffd&nbsp;', 'Fandom: Original Work &nbsp;&bull;&nbsp;')
        content = content.replace('Fandom: Demon Slayer &nbsp;\ufffd&nbsp;', 'Fandom: Demon Slayer &nbsp;&bull;&nbsp;')
        
        # Cover emojis
        content = content.replace('<div style=\"font-size:3rem;line-height:1;\">\ufffd\ufffd</div>', '<div style=\"font-size:3rem;line-height:1;\">&#x1F9B8;</div>')
        content = content.replace('<div style=\"font-size:3rem;line-height:1;\">\ufffd</div>', '<div style=\"font-size:3rem;line-height:1;\">&#x26A1;</div>')
        content = content.replace('\ufffd\ufffd', '&#x1F4D6;')
        content = content.replace('\ufffd', '&#x1F4D6;')
        
    elif 'writer-earnings.html' in filepath:
        content = content.replace('<div style=\"font-size:2.5rem\">\ufffd\ufffd</div>', '<div style=\"font-size:2.5rem\">&#x1F3C6;</div>')
        content = content.replace('<div style=\"font-size:2.5rem\">??</div>', '<div style=\"font-size:2.5rem\">&#x1F3C6;</div>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_file('e:/OfficeDownloads_/MayJuneWebsite/Fan_Fiction_Writing_Community/writer-stories.html')
fix_file('e:/OfficeDownloads_/MayJuneWebsite/Fan_Fiction_Writing_Community/writer-earnings.html')
print('Fixed files successfully')
