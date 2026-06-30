import glob

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The user wants 'New Story' buttons to be the same size
    content = content.replace('class="btn btn-primary-custom fw-bold shadow-sm px-4"', 'class="btn btn-primary-custom fw-bold shadow-sm btn-dash-action"')
    content = content.replace('class="btn btn-sm btn-primary-custom px-3"', 'class="btn btn-primary-custom btn-dash-action"') # user-messages.html Compose

    # Recent stories actions
    content = content.replace('class="btn btn-sm btn-outline-primary fw-bold"', 'class="btn btn-outline-primary fw-bold btn-dash-action"')
    content = content.replace('class="btn btn-sm btn-light"', 'class="btn btn-light btn-dash-action"')
    content = content.replace('class="btn btn-sm btn-primary-custom fw-bold"', 'class="btn btn-primary-custom fw-bold btn-dash-action"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filepath in glob.glob('e:/OfficeDownloads_/MayJuneWebsite/Fan_Fiction_Writing_Community/*.html'):
    if 'dashboard' in filepath or 'writer' in filepath or 'user' in filepath:
        process_file(filepath)
