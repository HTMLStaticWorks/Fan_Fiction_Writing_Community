import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Replace navbar-expand-lg with navbar-expand-xl in all HTML files
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if 'navbar-expand-lg' in content:
        new_content = content.replace('navbar-expand-lg', 'navbar-expand-xl')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated navbar in {f}")

# Append CSS for portrait hero section adjustment
css_file = 'assets/css/style.css'
with open(css_file, 'r', encoding='utf-8') as file:
    css_content = file.read()

portrait_css = """
/* Hero section adjustments for tall/portrait screens */
@media (orientation: portrait) and (min-width: 768px) {
  section[style*="min-height: calc(100vh - 76px)"] {
    min-height: 50vh !important;
  }
}
"""

if "orientation: portrait" not in css_content:
    with open(css_file, 'a', encoding='utf-8') as file:
        file.write(portrait_css)
    print("Added portrait media query to style.css")
