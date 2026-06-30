import glob, re

# The standard footer that all pages should have
standard_footer = """  <footer class="footer-custom">
    <div class="container">
      <div class="row g-4">
        <div class="col-lg-4 col-md-6 mb-4 mb-lg-0 text-start">
          <a class="navbar-brand mb-3 justify-content-start" href="index.html">
            <i class="ph-fill ph-book-open-text me-2 text-primary" style="font-size: 1.5rem;"></i>
            FanFicHub
          </a>
          <p class="text-muted"><bdi>Empowering writers to share their imagination with readers around the world.</bdi></p>
          <div class="d-flex gap-3 mt-4">
            <a href="#" class="text-muted hover-primary" aria-label="Facebook"><i class="ph-fill ph-facebook-logo fs-4"></i></a>
            <a href="#" class="text-muted hover-primary" aria-label="LinkedIn"><i class="ph-fill ph-linkedin-logo fs-4"></i></a>
            <a href="#" class="text-muted hover-primary" aria-label="Instagram"><i class="ph-fill ph-instagram-logo fs-4"></i></a>
            <a href="#" class="text-muted hover-primary" aria-label="X"><i class="ph-fill ph-x-logo fs-4"></i></a>
          </div>
        </div>
        <div class="col-lg-2 col-md-6 mb-4 mb-lg-0 text-start">
          <h4 class="footer-title h6">Quick Links</h4>
          <ul class="list-unstyled p-0">
            <li class="mb-2"><a href="about.html">About Us</a></li>
            <li class="mb-2"><a href="blog.html">Community</a></li>
            <li class="mb-2"><a href="contact.html">Support</a></li>
          </ul>
        </div>
        <div class="col-lg-2 col-md-6 mb-4 mb-lg-0 text-start">
          <h4 class="footer-title h6">Explore</h4>
          <ul class="list-unstyled p-0">
            <li class="mb-2"><a href="explore-stories.html">Top Stories</a></li>
            <li class="mb-2"><a href="fandoms.html">Trending Fandoms</a></li>
            <li class="mb-2"><a href="authors.html">Popular Authors</a></li>
          </ul>
        </div>
        <div class="col-lg-4 col-md-6 mb-4 mb-lg-0 text-start">
          <h4 class="footer-title h6">Newsletter</h4>
          <p class="text-muted small"><bdi>Subscribe to get the latest writing tips and updates.</bdi></p>
          <form class="d-flex flex-column flex-sm-row gap-2 needs-validation" novalidate>
            <input type="email" class="form-control form-control-custom" placeholder="Enter Email" required>
            <button class="btn btn-primary-custom" type="submit">Subscribe</button>
          </form>
        </div>
      </div>
      <div class="bottom-bar">
        <bdi>&copy; 2026 FanFicHub. All rights reserved.</bdi>
      </div>
    </div>
  </footer>"""

files = glob.glob('e:/OfficeDownloads_/MayJuneWebsite/Fan_Fiction_Writing_Community/*.html')
count = 0

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace the entire footer block
    match = re.search(r'(\s*)<footer\s+class="footer-custom"[^>]*>.*?</footer>', content, re.DOTALL)
    if match:
        old_footer = match.group(0)
        if old_footer.strip() != standard_footer.strip():
            new_content = content.replace(old_footer, "\n" + standard_footer)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Updated: {filepath.split('/')[-1]}")

print(f"\nTotal files updated: {count}")
