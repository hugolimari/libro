// Lógica de interacción para LectuVault
document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('searchInput');
  const searchBtn = document.getElementById('searchBtn');
  const booksGrid = document.getElementById('booksGrid');
  const noResults = document.getElementById('noResults');
  const bookCards = document.querySelectorAll('.book-card');

  // Buscador en tiempo real
  function executeSearch() {
    const query = searchInput.value.trim().toLowerCase();
    let visibleCount = 0;

    bookCards.forEach(card => {
      const title = card.getAttribute('data-title') || '';
      if (query === '' || title.includes(query)) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    if (visibleCount === 0) {
      noResults.style.display = 'block';
    } else {
      noResults.style.display = 'none';
    }
  }

  searchInput.addEventListener('input', executeSearch);
  searchBtn.addEventListener('click', executeSearch);

  // Cerrar modales con tecla ESC
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeModals();
    }
  });

  // Cerrar al hacer clic en el fondo oscuro
  document.querySelectorAll('.modal-backdrop').forEach(modal => {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeModals();
      }
    });
  });
});

// Filtro rápido por texto desde los tags
window.filterBook = function(term) {
  const searchInput = document.getElementById('searchInput');
  searchInput.value = term;
  searchInput.dispatchEvent(new Event('input'));
  
  const dest = document.getElementById('destacados');
  if (dest) {
    dest.scrollIntoView({ behavior: 'smooth' });
  }
};

// Filtro por categorías
window.filterCategory = function(cat) {
  // Actualizar botones de píldora
  document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
  event.target.classList.add('active');

  const bookCards = document.querySelectorAll('.book-card');
  const noResults = document.getElementById('noResults');
  let visibleCount = 0;

  bookCards.forEach(card => {
    const cardCat = card.getAttribute('data-category');
    if (cat === 'todos' || cardCat === cat) {
      card.style.display = 'flex';
      visibleCount++;
    } else {
      card.style.display = 'none';
    }
  });

  noResults.style.display = visibleCount === 0 ? 'block' : 'none';
};

// Resetear búsqueda
window.resetSearch = function() {
  const searchInput = document.getElementById('searchInput');
  searchInput.value = '';
  searchInput.dispatchEvent(new Event('input'));
  document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
  document.querySelector('.pill').classList.add('active');
};

// Abrir ficha técnica detallada de Make More Money
window.openBookDetails = function() {
  closeModals();
  const modal = document.getElementById('detailsModal');
  if (modal) {
    modal.classList.add('open');
  }
};

// Abrir modal de descarga de servidores
window.openDownloadModal = function() {
  closeModals();
  const modal = document.getElementById('downloadModal');
  
  // Restablecer vistas internas del modal
  document.getElementById('serverSelectorView').style.display = 'block';
  document.getElementById('countdownView').style.display = 'none';
  document.getElementById('readyView').style.display = 'none';
  
  if (modal) {
    modal.classList.add('open');
  }
};

// Iniciar proceso de cuenta regresiva de descarga
let countdownInterval = null;
window.startDownloadProcess = function(serverName) {
  document.getElementById('serverSelectorView').style.display = 'none';
  const countdownView = document.getElementById('countdownView');
  countdownView.style.display = 'block';

  let timeLeft = 4;
  const numElem = document.getElementById('countdownNumber');
  const statusElem = document.getElementById('countdownStatus');
  const progressFill = document.getElementById('progressBarFill');

  numElem.textContent = timeLeft;
  progressFill.style.width = '20%';

  if (countdownInterval) clearInterval(countdownInterval);

  countdownInterval = setInterval(() => {
    timeLeft--;
    numElem.textContent = timeLeft;
    
    if (timeLeft === 3) {
      statusElem.textContent = `Conectando con ${serverName}...`;
      progressFill.style.width = '50%';
    } else if (timeLeft === 2) {
      statusElem.textContent = 'Validando bloque de descifrado y hash MD5...';
      progressFill.style.width = '75%';
    } else if (timeLeft === 1) {
      statusElem.textContent = 'Enlace seguro generado sin publicidad.';
      progressFill.style.width = '95%';
    } else if (timeLeft <= 0) {
      clearInterval(countdownInterval);
      progressFill.style.width = '100%';
      showReadyDownload();
    }
  }, 950);
};

// Mostrar pantalla de enlace listo y disparar descarga automática
function showReadyDownload() {
  document.getElementById('countdownView').style.display = 'none';
  document.getElementById('readyView').style.display = 'block';

  // Simulación de disparo de descarga automática
  setTimeout(() => {
    const downloadLink = document.getElementById('directDownloadBtn');
    if (downloadLink) {
      // Disparar clic para descargar el archivo
      const clickEvent = new MouseEvent('click', {
        view: window,
        bubbles: true,
        cancelable: true
      });
      downloadLink.dispatchEvent(clickEvent);
    }
  }, 800);
}

// Abrir modal de DMCA creíble para libros cebo
window.openDmcaModal = function(bookTitle) {
  closeModals();
  const modal = document.getElementById('dmcaModal');
  const titleElem = document.getElementById('dmcaTitle');
  const msgElem = document.getElementById('dmcaMessage');

  titleElem.textContent = `Enlace No Disponible: ${bookTitle}`;
  msgElem.innerHTML = `El servidor donde se alojaba <strong>"${bookTitle}"</strong> ha sido desactivado temporalmente debido a una reclamación DMCA automática o saturación de ancho de banda.`;

  if (modal) {
    modal.classList.add('open');
  }
};

// Aviso DMCA general
window.openDmcaNotice = function() {
  closeModals();
  const modal = document.getElementById('dmcaModal');
  const titleElem = document.getElementById('dmcaTitle');
  const msgElem = document.getElementById('dmcaMessage');

  titleElem.textContent = 'Política de Propiedad Intelectual & DMCA';
  msgElem.innerHTML = 'LectuVault respeta los derechos de autor conforme a la ley 17 U.S.C. § 512. Ningún archivo con copyright es alojado por nuestros servidores centrales; los nodos P2P se sincronizan de forma descentralizada. Para solicitar la retirada de un enlace, contacte a dmca@lectuvault.org.';

  if (modal) {
    modal.classList.add('open');
  }
};

// Cerrar todos los modales
window.closeModals = function() {
  if (countdownInterval) clearInterval(countdownInterval);
  document.querySelectorAll('.modal-backdrop').forEach(modal => {
    modal.classList.remove('open');
  });
};

// Ir al libro destacado de Gavin Ross desde un aviso de error
window.goToFeatured = function() {
  closeModals();
  openBookDetails();
};
