filepath = 'e:/OfficeDownloads_/MayJuneWebsite/Fan_Fiction_Writing_Community/home-2.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('class="text-white text-decoration-none hover-primary"', 'class="text-body text-decoration-none hover-primary"')
content = content.replace('card-text text-light', 'card-text text-muted')
content = content.replace('card-title h4 mt-2 text-white', 'card-title h4 mt-2 text-body')
content = content.replace('fst-italic text-light', 'fst-italic text-muted')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated home-2.html')
