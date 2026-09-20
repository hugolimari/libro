// Lógica de navegación e interacción de LectuLibros.org

document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('searchInput');
  const searchBtn = document.getElementById('searchBtn');
  const noResults = document.getElementById('noResults');
  const bookRows = document.querySelectorAll('.book-row');
  const countBadge = document.getElementById('visibleCountText');

  // Función de búsqueda
  function executeSearch() {
    const query = searchInput.value.trim().toLowerCase();
    let visibleCount = 0;

    bookRows.forEach(row => {
      const dataTitle = (row.getAttribute('data-title') || '').toLowerCase();
      if (query === '' || dataTitle.includes(query)) {
        row.style.display = 'flex';
        visibleCount++;
      } else {
        row.style.display = 'none';
      }
    });

    if (countBadge) {
      countBadge.textContent = `${visibleCount} libro${visibleCount === 1 ? '' : 's'} en lista`;
    }

    if (visibleCount === 0) {
      noResults.style.display = 'block';
    } else {
      noResults.style.display = 'none';
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', executeSearch);
  }
  if (searchBtn) {
    searchBtn.addEventListener('click', executeSearch);
  }

  // Cerrar modales con tecla Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeModals();
    }
  });

  // Cerrar modal al hacer clic en el fondo gris
  document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
        closeModals();
      }
    });
  });
});

// Filtro rápido desde los enlaces de sugerencias
window.filterBook = function(term) {
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.value = term;
    searchInput.dispatchEvent(new Event('input'));
  }
  const catalogo = document.getElementById('catalogo');
  if (catalogo) {
    catalogo.scrollIntoView({ behavior: 'smooth' });
  }
};

// Filtro por categorías
window.filterCategory = function(cat) {
  const searchInput = document.getElementById('searchInput');
  if (searchInput) searchInput.value = '';

  const bookRows = document.querySelectorAll('.book-row');
  const noResults = document.getElementById('noResults');
  const countBadge = document.getElementById('visibleCountText');
  let visibleCount = 0;

  bookRows.forEach(row => {
    const rowCat = row.getAttribute('data-category');
    if (cat === 'todos' || rowCat === cat) {
      row.style.display = 'flex';
      visibleCount++;
    } else {
      row.style.display = 'none';
    }
  });

  if (countBadge) {
    countBadge.textContent = `${visibleCount} libro${visibleCount === 1 ? '' : 's'} en lista`;
  }

  if (visibleCount === 0) {
    noResults.style.display = 'block';
  } else {
    noResults.style.display = 'none';
  }

  const catalogo = document.getElementById('catalogo');
  if (catalogo) {
    catalogo.scrollIntoView({ behavior: 'smooth' });
  }
};

// Restablecer catálogo completo
window.resetSearch = function() {
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.value = '';
    searchInput.dispatchEvent(new Event('input'));
  }
};

// Abrir ficha detallada del libro de Gavin Ross
window.openBookDetails = function() {
  closeModals();
  const modal = document.getElementById('detailsModal');
  if (modal) {
    modal.classList.add('open');
  }
};

// Abrir modal de descarga y selección de servidor
window.openDownloadModal = function() {
  closeModals();
  const modal = document.getElementById('downloadModal');
  
  // Reestablecer vistas internas
  document.getElementById('stepServers').style.display = 'block';
  document.getElementById('stepCountdown').style.display = 'none';
  document.getElementById('stepReady').style.display = 'none';

  if (modal) {
    modal.classList.add('open');
  }
};

// Iniciar temporizador de descarga
let dlTimer = null;
window.startDownloadProcess = function(serverName) {
  document.getElementById('stepServers').style.display = 'none';
  const stepCountdown = document.getElementById('stepCountdown');
  stepCountdown.style.display = 'block';

  let seconds = 3;
  const numElem = document.getElementById('countdownNumber');
  const msgElem = document.getElementById('countdownMessage');
  const barElem = document.getElementById('barFill');

  numElem.textContent = seconds;
  barElem.style.width = '25%';

  if (dlTimer) clearInterval(dlTimer);

  dlTimer = setInterval(() => {
    seconds--;
    numElem.textContent = seconds;

    if (seconds === 2) {
      msgElem.textContent = `Conectando con ${serverName}...`;
      barElem.style.width = '60%';
    } else if (seconds === 1) {
      msgElem.textContent = 'Generando cabecera de transferencia binaria...';
      barElem.style.width = '90%';
    } else if (seconds <= 0) {
      clearInterval(dlTimer);
      barElem.style.width = '100%';
      triggerFinishDownload();
    }
  }, 900);
};

// Finalizar y disparar la descarga directa al navegador
function triggerFinishDownload() {
  document.getElementById('stepCountdown').style.display = 'none';
  document.getElementById('stepReady').style.display = 'block';

  setTimeout(() => {
    const link = document.getElementById('realDownloadLink');
    if (link) {
      const evt = new MouseEvent('click', {
        view: window,
        bubbles: true,
        cancelable: true
      });
      link.dispatchEvent(evt);
    }
  }, 600);
}

// Cerrar todos los modales
window.closeModals = function() {
  if (dlTimer) clearInterval(dlTimer);
  document.querySelectorAll('.modal-overlay').forEach(modal => {
    modal.classList.remove('open');
  });
};
