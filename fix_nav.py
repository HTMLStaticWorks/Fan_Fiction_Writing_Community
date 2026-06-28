import re
import os

directory = r'e:\OfficeDownloads_\MayJuneWebsite\Fan_Fiction_Writing_Community'

pattern = r'<li class="nav-item dropdown">\s*<a class="nav-link dropdown-toggle[^"]*" href="#" id="communityDropdown".*?Community\s*</a>\s*<ul class="dropdown-menu" aria-labelledby="communityDropdown">\s*<li><a class="dropdown-item[^"]*" href="blog\.html">Community News</a></li>\s*<li><a class="dropdown-item[^"]*" href="story-preview\.html">Featured Story</a></li>\s*</ul>\s*</li>'

def repl(match):
    m = match.group(0)
    if 'active' in m:
        return '<li class="nav-item"><a class="nav-link active" href="blog.html">Community</a></li>'
    return '<li class="nav-item"><a class="nav-link" href="blog.html">Community</a></li>'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        path = os.path.join(directory, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, num = re.subn(pattern, repl, content, flags=re.DOTALL)
        
        # Replace "Community News" in footer or anywhere else outside the nav as just "Community" or "Community News" is fine too, but let's change it.
        # Actually in footer: <li class="mb-2"><a href="blog.html">Community News</a></li>
        # Let's change it to Community
        new_content = new_content.replace('<a href="blog.html">Community News</a>', '<a href="blog.html">Community</a>')
        
        if num > 0 or new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Updated {filename}")

print(f"Total updated: {count}")
