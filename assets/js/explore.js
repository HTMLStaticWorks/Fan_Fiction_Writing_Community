document.addEventListener('DOMContentLoaded', () => {
  const applyBtn = document.getElementById('applyFiltersBtn');
  const allCards = Array.from(document.querySelectorAll('.story-item'));
  const resultsCount = document.getElementById('resultsCount');
  const paginationControls = document.getElementById('paginationControls');
  
  let currentPage = 1;
  const cardsPerPage = 4;
  let filteredCards = [...allCards];

  const fandomMap = {
    'fandomMarvel': 'marvel',
    'fandomHP': 'hp',
    'fandomNaruto': 'naruto',
    'fandomOnePiece': 'onepiece',
    'fandomStarWars': 'starwars',
    'fandomLOTR': 'lotr',
    'fandomDC': 'dc',
    'fandomST': 'st',
    'fandomPJ': 'pj',
    'fandomMHA': 'mha'
  };


  function applyFilters() {
const selectedFandoms = Object.keys(fandomMap)
      .filter(id => {
        const el = document.getElementById(id);
        return el && el.checked;
      })
      .map(id => fandomMap[id]);

    filteredCards = allCards.filter(card => {
      const cardFandom = card.getAttribute('data-fandom') || '';
      return selectedFandoms.length === 0 || selectedFandoms.some(f => cardFandom.includes(f));
    });

    currentPage = 1;
    renderPagination();
    renderCards();
    if (resultsCount) {
      resultsCount.textContent = filteredCards.length;
    }
  }

  function renderCards() {
    allCards.forEach(card => card.style.display = 'none');
    
    const startIndex = (currentPage - 1) * cardsPerPage;
    const endIndex = startIndex + cardsPerPage;
    
    const cardsToShow = filteredCards.slice(startIndex, endIndex);
    cardsToShow.forEach(card => card.style.display = 'block');
  }

  function renderPagination() {
    if (!paginationControls) return;
    
    const totalPages = Math.ceil(filteredCards.length / cardsPerPage);
    paginationControls.innerHTML = '';

    if (totalPages <= 1) {
      return; // No pagination needed
    }

    // Prev Button
    const prevLi = document.createElement('li');
    prevLi.className = `page-item ${currentPage === 1 ? 'disabled' : ''}`;
    prevLi.innerHTML = `<a class="page-link" href="#" data-page="prev">Previous</a>`;
    paginationControls.appendChild(prevLi);

    // Page numbers
    for (let i = 1; i <= totalPages; i++) {
      const pageLi = document.createElement('li');
      pageLi.className = `page-item ${currentPage === i ? 'active' : ''}`;
      pageLi.innerHTML = `<a class="page-link" href="#" data-page="${i}">${i}</a>`;
      paginationControls.appendChild(pageLi);
    }

    // Next Button
    const nextLi = document.createElement('li');
    nextLi.className = `page-item ${currentPage === totalPages ? 'disabled' : ''}`;
    nextLi.innerHTML = `<a class="page-link" href="#" data-page="next">Next</a>`;
    paginationControls.appendChild(nextLi);
  }

  if (paginationControls) {
    paginationControls.addEventListener('click', (e) => {
      e.preventDefault();
      if (e.target.tagName !== 'A') return;
      
      const pageAction = e.target.getAttribute('data-page');
      const totalPages = Math.ceil(filteredCards.length / cardsPerPage);

      if (pageAction === 'prev' && currentPage > 1) {
        currentPage--;
      } else if (pageAction === 'next' && currentPage < totalPages) {
        currentPage++;
      } else if (!isNaN(pageAction)) {
        currentPage = parseInt(pageAction);
      } else {
        return;
      }

      renderPagination();
      renderCards();
    });
  }


  const selectAllBtn = document.getElementById('selectAllBtn');
  const clearAllBtn = document.getElementById('clearAllBtn');

  if (selectAllBtn) {
    selectAllBtn.addEventListener('click', () => {
      Object.keys(fandomMap).forEach(id => {
        const el = document.getElementById(id);
        if (el) el.checked = true;
      });
      applyFilters();
    });
  }

  if (clearAllBtn) {
    clearAllBtn.addEventListener('click', () => {
      Object.keys(fandomMap).forEach(id => {
        const el = document.getElementById(id);
        if (el) el.checked = false;
      });
      applyFilters();
    });
  }

  if (applyBtn) {
    applyBtn.addEventListener('click', (e) => {
      e.preventDefault();
      applyFilters();
    });
  }

  // Initial render (no filters applied by default so it shows first page of all cards)
  applyFilters();
});
