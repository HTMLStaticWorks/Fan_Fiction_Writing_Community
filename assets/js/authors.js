
document.addEventListener('DOMContentLoaded', () => {
    const authorsPerPage = 6;
    const authorItems = Array.from(document.querySelectorAll('.author-item'));
    const paginationContainer = document.querySelector('.pagination');
    
    // --- Follow Button Logic ---
    authorItems.forEach(item => {
        const btn = item.querySelector('button');
        const handleEl = item.querySelector('.text-muted.small.mb-3');
        if (btn && handleEl) {
            const handle = handleEl.innerText.replace('@', '').trim();
            btn.dataset.author = handle;
            
            // Check session storage
            const isFollowing = sessionStorage.getItem(`follow_${handle}`) === 'true';
            if (isFollowing) {
                btn.innerText = 'Following';
                btn.classList.remove('btn-outline-primary-custom');
                btn.classList.add('btn-primary-custom');
            }
            
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const currentlyFollowing = sessionStorage.getItem(`follow_${handle}`) === 'true';
                
                if (currentlyFollowing) {
                    // Unfollow
                    sessionStorage.setItem(`follow_${handle}`, 'false');
                    btn.innerText = 'Follow';
                    btn.classList.add('btn-outline-primary-custom');
                    btn.classList.remove('btn-primary-custom');
                } else {
                    // Follow
                    sessionStorage.setItem(`follow_${handle}`, 'true');
                    btn.innerText = 'Following';
                    btn.classList.remove('btn-outline-primary-custom');
                    btn.classList.add('btn-primary-custom');
                }
            });
        }
    });

    if (!paginationContainer || authorItems.length === 0) return;
    
    const totalPages = Math.ceil(authorItems.length / authorsPerPage);
    let currentPage = 1;

    function renderAuthors(page) {
        const start = (page - 1) * authorsPerPage;
        const end = start + authorsPerPage;
        
        authorItems.forEach((item, index) => {
            if (index >= start && index < end) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
        
        renderPagination(page);
    }

    function renderPagination(page) {
        paginationContainer.innerHTML = '';
        
        // Prev
        const prevLi = document.createElement('li');
        prevLi.className = `page-item ${page === 1 ? 'disabled' : ''}`;
        prevLi.innerHTML = `<a class="page-link" href="#" data-page="${page - 1}">Previous</a>`;
        paginationContainer.appendChild(prevLi);
        
        // Pages
        for (let i = 1; i <= totalPages; i++) {
            const pageLi = document.createElement('li');
            pageLi.className = `page-item ${i === page ? 'active' : ''}`;
            pageLi.innerHTML = `<a class="page-link" href="#" data-page="${i}">${i}</a>`;
            paginationContainer.appendChild(pageLi);
        }
        
        // Next
        const nextLi = document.createElement('li');
        nextLi.className = `page-item ${page === totalPages ? 'disabled' : ''}`;
        nextLi.innerHTML = `<a class="page-link" href="#" data-page="${page + 1}">Next</a>`;
        paginationContainer.appendChild(nextLi);
        
        // Attach events
        paginationContainer.querySelectorAll('.page-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const p = parseInt(e.target.getAttribute('data-page'));
                if (p >= 1 && p <= totalPages) {
                    currentPage = p;
                    renderAuthors(currentPage);
                    window.scrollTo({ top: document.getElementById('authorsGrid').offsetTop - 100, behavior: 'smooth' });
                }
            });
        });
    }

    renderAuthors(currentPage);
});
