import glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'col-md-4' in content:
        # replace col-md-4 with col-12 col-sm-6 col-md-4
        content = re.sub(r'\bcol-md-4\b', 'col-12 col-sm-6 col-md-4', content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
            print(f"Updated {f}")
