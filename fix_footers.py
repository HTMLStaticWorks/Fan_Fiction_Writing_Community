import sys

footer = """  <footer class="footer-custom">
    <div class="container">
      <div class="row g-4">
        <div class="col-lg-4 col-md-6 text-start">
          <a class="navbar-brand mb-3 justify-content-start" href="index.html">
            <i class="ph-fill ph-book-open-text me-2 text-primary" style="font-size: 1.5rem;"></i>
            FanFicHub
          </a>
          <p class="text-muted">Empowering writers to share their imagination with readers around the world.</p>
          <div class="d-flex gap-3 mt-4">
            <a href="#" class="text-muted hover-primary" aria-label="Facebook"><i class="ph-fill ph-facebook-logo fs-4"></i></a>
            <a href="#" class="text-muted hover-primary" aria-label="LinkedIn"><i class="ph-fill ph-linkedin-logo fs-4"></i></a>
            <a href="#" class="text-muted hover-primary" aria-label="Instagram"><i class="ph-fill ph-instagram-logo fs-4"></i></a>
            <a href="#" class="text-muted hover-primary" aria-label="X"><i class="ph-fill ph-x-logo fs-4"></i></a>
          </div>
        </div>
        <div class="col-lg-2 col-md-6 text-start">
          <h4 class="footer-title h6">Quick Links</h4>
          <ul class="list-unstyled">
            <li class="mb-2"><a href="about.html">About Us</a></li>
            <li class="mb-2"><a href="blog.html">Community</a></li>
            <li class="mb-2"><a href="contact.html">Support</a></li>
          </ul>
        </div>
        <div class="col-lg-2 col-md-6 text-start">
          <h4 class="footer-title h6">Legal</h4>
          <ul class="list-unstyled">
            <li class="mb-2"><a href="#">Privacy Policy</a></li>
            <li class="mb-2"><a href="#">Terms of Service</a></li>
          </ul>
        </div>
        <div class="col-lg-4 col-md-6 text-start">
          <h4 class="footer-title h6">Newsletter</h4>
          <p class="text-muted small">Subscribe to get the latest writing tips and updates.</p>
          <form class="d-flex flex-column flex-sm-row gap-2 needs-validation" novalidate>
            <input type="email" class="form-control form-control-custom" placeholder="Your email address" required>
            <button class="btn btn-primary-custom" type="submit">Subscribe</button>
          </form>
        </div>
      </div>
      <div class="bottom-bar">
        &copy; 2026 FanFicHub. All rights reserved.
      </div>
    </div>
  </footer>"""

for filename in ['explore-stories.html', 'fandoms.html', 'authors.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_idx = content.find('<footer class="footer-custom">')
    if start_idx == -1: continue
    end_idx = content.find('</footer>', start_idx) + len('</footer>')
    
    new_content = content[:start_idx] + footer + content[end_idx:]
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
