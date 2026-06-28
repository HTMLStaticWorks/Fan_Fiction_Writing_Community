import os
directory = r'E:\OfficeDownloads_\MayJuneWebsite\Fan_Fiction_Writing_Community'

files = ['authors.html','explore-stories.html','index.html','home-2.html','story-preview.html','fandoms.html']
for file in files:
    path = os.path.join(directory, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update logo sources
    content = content.replace('assets/images/marvel_logo.png', 'assets/images/marvel_logo_v2.png')
    content = content.replace('assets/images/dc_logo.png', 'assets/images/dc_logo_v2.png')
    
    # 2. Fix the tiny inline logo styles
    old_style_small = 'style="height: 14px; width: 14px; margin-right: 4px; border-radius: 50%; object-fit: cover;"'
    new_style_small = 'style="height: 20px; width: auto; margin-right: 6px; object-fit: contain; vertical-align: middle;"'
    content = content.replace(old_style_small, new_style_small)
    
    # 3. Fix index.html specific fandom badge size
    old_style_idx = 'class="rounded-circle mb-2" style="width: 40px; height: 40px; object-fit: cover;"'
    new_style_idx = 'class="mb-2" style="height: 40px; width: auto; object-fit: contain;"'
    content = content.replace(old_style_idx, new_style_idx)
    
    # 4. Fix fandoms.html specific badge size
    old_style_fandom = 'style="width: 48px; height: 48px; object-fit: contain;"'
    new_style_fandom = 'style="height: 48px; width: auto; object-fit: contain;"'
    content = content.replace(old_style_fandom, new_style_fandom)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
