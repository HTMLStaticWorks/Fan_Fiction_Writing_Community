import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Standard footer HTML (using X, Facebook, LinkedIn, Instagram)
footer_html = """  <footer class="footer-custom">
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

def update_footer(content):
    # Regex to find the footer block
    pattern = re.compile(r'  <footer class="footer-custom.*?>.*?</footer>', re.DOTALL)
    if pattern.search(content):
        return pattern.sub(footer_html, content)
    return content

# Dictionary of extended paragraphs for hero sections
extended_hero_texts = {
    'authors.html': 'Follow talented writers and never miss a new chapter. Discover incredible storytellers who bring your favorite characters and immersive worlds to life in completely new and exciting ways.',
    'explore-stories.html': 'Dive into thousands of fan-created stories across your favorite universes. Find your next great read, from action-packed adventures to heartwarming romances, all written by our passionate community.',
    'fandoms.html': 'Explore communities dedicated to your favorite books, movies, and shows. Connect with other fans, share your theories, and immerse yourself in the expansive universes you already love.',
    'contact.html': 'Have questions or need assistance? We are here to help. Reach out to our friendly support team, and we will get back to you as quickly as possible to ensure you have the best experience.',
    'about.html': 'Learn more about our mission, our dedicated team, and the vibrant community we are building together. We believe in the power of shared imagination and giving every writer a platform to shine.',
    'blog.html': 'Read the latest news, updates, and writing tips from our community. Stay informed about upcoming writing contests, platform features, and inspiring stories from fellow creators.',
    '404.html': 'Oops! The page you are looking for seems to have wandered off into another universe. Let us guide you back to the main hub so you can continue your reading adventure.',
    'coming-soon.html': 'We are working hard behind the scenes to bring you something amazing. Stay tuned for exciting new features and updates that will elevate your writing and reading experience.'
}

def update_hero(filename, content):
    if filename in ['index.html', 'home-2.html', 'blog-details.html', 'story-preview.html']:
        return content
        
    text = extended_hero_texts.get(filename, 'Explore our vast collection of content and join the community. Dive deeper into the stories you love and discover new favorites along the way.')
    
    # Try to find the hero paragraph. Usually it's: <p class="lead text-light...
    pattern = re.compile(r'(<p class="lead[^>]*>)(.*?)(</p>)', re.DOTALL)
    
    def replacer(match):
        p_tag = match.group(1)
        # update opacity class or style
        p_tag = re.sub(r'opacity-\d+', '', p_tag)
        if 'style="' in p_tag:
            p_tag = re.sub(r'style="([^"]*)"', r'style="\1 opacity: 0.7;"', p_tag)
        else:
            p_tag = p_tag.replace('class="', 'style="opacity: 0.7;" class="')
        
        return f'{p_tag}{text}{match.group(3)}'
        
    # We only want to replace the first paragraph in the hero section.
    new_content = pattern.sub(replacer, content, count=1)
    return new_content

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    new_content = update_footer(content)
    new_content = update_hero(f, new_content)
    
    if content != new_content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
