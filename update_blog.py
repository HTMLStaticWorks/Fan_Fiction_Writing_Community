import os
import re

path = r'e:\OfficeDownloads_\MayJuneWebsite\Fan_Fiction_Writing_Community\blog.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the content inside <div class="container py-5">
# Find <div class="container py-5">
start_idx = content.find('<div class="container py-5">')
end_idx = content.find('<!-- Footer -->')

if start_idx != -1 and end_idx != -1:
    new_section = """<div class="container py-5">
    
    <div class="mb-5">
      <h2 class="h3 mb-4">Featured Story</h2>
      <div class="card border-0 shadow-sm bg-dark text-white p-0 overflow-hidden" style="border-radius: 15px;">
        <div class="row g-0">
          <div class="col-md-4">
            <img src="assets/images/Echoes of Andromeda.jfif" class="img-fluid rounded-start h-100 object-fit-cover" alt="Featured Story">
          </div>
          <div class="col-md-8">
            <div class="card-body p-4 p-md-5 d-flex flex-column h-100 justify-content-center">
              <div class="mb-3">
                <span class="badge bg-primary me-2">Sci-Fi</span>
                <span class="badge bg-secondary">Featured</span>
              </div>
              <h3 class="card-title text-white mb-3">Echoes of Andromeda</h3>
              <p class="card-text text-light opacity-75 mb-4">A continuation of the beloved series where the crew faces a new unknown threat from the deep cosmos. This story has captivated thousands with its deep world-building and character development.</p>
              <div class="mt-auto">
                 <a href="story-preview.html" class="btn btn-primary-custom">Read Story</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <h2 class="h3 mb-4">Latest News</h2>
    <div class="row g-4 mb-5">
      <div class="col-md-4">
        <div class="story-card h-100 d-flex flex-column">
          <img src="assets/images/blog.png" alt="Blog Image">
          <div class="story-card-body d-flex flex-column flex-grow-1">
            <span class="badge-custom mb-2 d-inline-block">Writing Tips</span>
            <h3 class="story-card-title h5"><a href="blog-details.html" style="color: inherit;">How to Build Tension in Your Chapters</a></h3>
            <p class="story-card-text flex-grow-1">Learn the key pacing techniques to keep your readers hooked.</p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="story-card h-100 d-flex flex-column">
          <img src="assets/images/scifi.png" alt="Blog Image">
          <div class="story-card-body d-flex flex-column flex-grow-1">
            <span class="badge-custom mb-2 d-inline-block">Community</span>
            <h3 class="story-card-title h5"><a href="blog-details.html" style="color: inherit;">Monthly FanFic Contest Winners</a></h3>
            <p class="story-card-text flex-grow-1">Announcing the winners of our Sci-Fi themed writing contest.</p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="story-card h-100 d-flex flex-column">
          <img src="assets/images/fantasy.png" alt="Blog Image">
          <div class="story-card-body d-flex flex-column flex-grow-1">
            <span class="badge-custom mb-2 d-inline-block">Updates</span>
            <h3 class="story-card-title h5"><a href="blog-details.html" style="color: inherit;">New Dashboard Features</a></h3>
            <p class="story-card-text flex-grow-1">We just rolled out new analytics features for our writers.</p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="story-card h-100 d-flex flex-column">
          <div class="bg-secondary opacity-50 w-100 d-flex justify-content-center align-items-center" style="height: 200px; border-radius: 12px 12px 0 0;">
            <i class="ph-fill ph-megaphone text-white" style="font-size: 4rem;"></i>
          </div>
          <div class="story-card-body d-flex flex-column flex-grow-1">
            <span class="badge-custom mb-2 d-inline-block">Platform</span>
            <h3 class="story-card-title h5"><a href="blog-details.html" style="color: inherit;">Server Upgrades Scheduled</a></h3>
            <p class="story-card-text flex-grow-1">Important information regarding the upcoming maintenance downtime.</p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="story-card h-100 d-flex flex-column">
           <div class="bg-primary opacity-75 w-100 d-flex justify-content-center align-items-center" style="height: 200px; border-radius: 12px 12px 0 0;">
            <i class="ph-fill ph-users text-white" style="font-size: 4rem;"></i>
          </div>
          <div class="story-card-body d-flex flex-column flex-grow-1">
            <span class="badge-custom mb-2 d-inline-block">Community</span>
            <h3 class="story-card-title h5"><a href="blog-details.html" style="color: inherit;">Author Spotlight: SpaceWriter99</a></h3>
            <p class="story-card-text flex-grow-1">An exclusive interview with one of our top sci-fi contributors.</p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="story-card h-100 d-flex flex-column">
           <div class="bg-dark text-white w-100 d-flex justify-content-center align-items-center" style="height: 200px; border-radius: 12px 12px 0 0;">
            <i class="ph-fill ph-notebook text-white" style="font-size: 4rem;"></i>
          </div>
          <div class="story-card-body d-flex flex-column flex-grow-1">
            <span class="badge-custom mb-2 d-inline-block">Writing Tips</span>
            <h3 class="story-card-title h5"><a href="blog-details.html" style="color: inherit;">Developing Complex Antagonists</a></h3>
            <p class="story-card-text flex-grow-1">Move past one-dimensional villains with these character building exercises.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
"""
    new_content = content[:start_idx] + new_section + "\n  " + content[end_idx:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated blog.html")
else:
    print("Could not find sections in blog.html")
