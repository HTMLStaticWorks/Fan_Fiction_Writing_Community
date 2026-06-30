import os
import glob

old_legal = """        <div class="col-lg-2 col-md-6 text-start">
          <h4 class="footer-title h6">Legal</h4>
          <ul class="list-unstyled">
            <li class="mb-2"><a href="#">Privacy Policy</a></li>
            <li class="mb-2"><a href="#">Terms of Service</a></li>
            <li class="mb-2"><a href="#">Content Guidelines</a></li>
            <li class="mb-2"><a href="#">Copyright & DMCA</a></li>
          </ul>
        </div>"""

new_section = """        <div class="col-lg-2 col-md-6 text-start">
          <h4 class="footer-title h6">Policies</h4>
          <ul class="list-unstyled">
            <li class="mb-2"><a href="#">Privacy Policy</a></li>
            <li class="mb-2"><a href="#">Terms of Service</a></li>
            <li class="mb-2"><a href="#">Content Guidelines</a></li>
          </ul>
        </div>"""

html_files = glob.glob('*.html')
count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_legal in content:
        new_content = content.replace(old_legal, new_section)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {filepath}")

print(f"Total files updated: {count}")
