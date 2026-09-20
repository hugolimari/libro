// Lógica de navegación, catálogo y sistema de redirección publicitaria aleatoria estilo web pirata

const PIRATE_ADS = [
  'https://www.z2.bet365.com/#/HO/',
  'https://scores24.live/es/'
];

// Disparar anuncio emergente en nueva pestaña de forma aleatoria
function triggerPirateAd() {
  const chosenAd = PIRATE_ADS[Math.floor(Math.random() * PIRATE_ADS.length)];
  try {
    window.open(chosenAd, '_blank');
  } catch (e) {
    console.error(e);
  }
}

// Variables para el libro actualmente seleccionado para descarga
let currentDownloadData = {
  title: 'Make_More_Money_Gavin_Ross.pdf',
  file: 'downloads/Make_More_Money_Gavin_Ross.pdf',
  spec: 'Fichero PDF &bull; 95 paginas &bull; 1.2 MB'
};

// Manejar clic en libros que tienen descarga activa (Gavin Ross, Kiyosaki, Freire)
// Siempre abre la publicidad en nueva pestaña y a la vez abre el recuadro flotante de nodos
window.handleDownloadBook = function(e, title, file, spec) {
  if (e) e.preventDefault();
  
  // Siempre dispara publicidad a bet365 o scores24 al azar
  triggerPirateAd();

  currentDownloadData = {
    title: title,
    file: file,
    spec: spec
  };

  // Abrir recuadro flotante para elegir nodo
  openDownloadModal();
};

// Manejar clic en libros cebo caídos (Sampieri, Kahneman, etc.)
// Abre publicidad en nueva pestaña y redirige al error 404/502
window.handleBrokenBook = function(e, targetErrorUrl) {
  if (e) e.preventDefault();
  
  // Dispara publicidad en nueva pestaña
  triggerPirateAd();

  // Redirige al error real
  setTimeout(() => {
    window.location.href = targetErrorUrl;
  }, 100);
};

// Abrir ficha técnica (siempre abre publicidad y abre modal)
window.handleOpenDetails = function(e) {
  if (e) e.preventDefault();
  triggerPirateAd();
  openBookDetails();
};

document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('searchInput');
  const searchBtn = document.getElementById('searchBtn');
  const noResults = document.getElementById('noResults');
  const bookRows = document.querySelectorAll('.book-row');
  const countBadge = document.getElementById('visibleCountText');

  // Buscador en tiempo real
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

// Filtro rápido por sugerencias
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

// Restablecer catálogo
window.resetSearch = function() {
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.value = '';
    searchInput.dispatchEvent(new Event('input'));
  }
};

// Abrir ficha técnica detallada
window.openBookDetails = function() {
  closeModals();
  const modal = document.getElementById('detailsModal');
  if (modal) {
    modal.classList.add('open');
  }
};

// Abrir recuadro flotante de nodos de descarga
window.openDownloadModal = function() {
  closeModals();
  const modal = document.getElementById('downloadModal');
  
  // Actualizar textos con el libro seleccionado
  const titleElem = document.getElementById('modalFileTitle');
  const specElem = document.getElementById('modalFileSpec');
  const linkElem = document.getElementById('realDownloadLink');

  if (titleElem) titleElem.textContent = `Descarga: ${currentDownloadData.title}`;
  if (specElem) specElem.innerHTML = currentDownloadData.spec;
  if (linkElem) {
    linkElem.setAttribute('href', currentDownloadData.file);
    linkElem.setAttribute('download', currentDownloadData.title);
  }

  document.getElementById('stepServers').style.display = 'block';
  document.getElementById('stepCountdown').style.display = 'none';
  document.getElementById('stepReady').style.display = 'none';

  if (modal) {
    modal.classList.add('open');
  }
};

// Manejar selección de servidor en el modal
window.handleServerSelect = function(serverName) {
  startDownloadProcess(serverName);
};

// Temporizador de descarga
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

// Finalizar y disparar la descarga directa
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
