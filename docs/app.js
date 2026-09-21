// ==========================================================================
// AI Learning Lab - Documentation & Download Portal Logic
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
  initOSDetection();
  initOSTabs();
  initCopyButtons();
  initDocsScrollSpy();
  initDocsSearch();
});

// 1. Detect Operating System and Configure Hero CTA
function initOSDetection() {
  const userAgent = window.navigator.userAgent.toLowerCase();
  const heroDownloadBtn = document.getElementById('heroDownloadBtn');
  const detectedOSLabel = document.getElementById('detectedOSLabel');
  
  let detectedOS = 'windows';
  let osName = 'Windows';
  let downloadUrl = 'https://github.com/Rajdeep-Mudiar/AI_Learning_Desktop_App/releases/latest/download/AI-Learning-Lab-Setup-x64.exe';
  let fileExt = '.exe';

  if (userAgent.indexOf('mac') !== -1 || userAgent.indexOf('darwin') !== -1) {
    detectedOS = 'macos';
    osName = 'macOS';
    downloadUrl = 'https://github.com/Rajdeep-Mudiar/AI_Learning_Desktop_App/releases/latest/download/AI-Learning-Lab-Universal.dmg';
    fileExt = '.dmg';
  } else if (userAgent.indexOf('linux') !== -1 || userAgent.indexOf('x11') !== -1) {
    detectedOS = 'linux';
    osName = 'Linux';
    downloadUrl = 'https://github.com/Rajdeep-Mudiar/AI_Learning_Desktop_App/releases/latest/download/AI-Learning-Lab-x86_64.AppImage';
    fileExt = '.AppImage';
  }

  // Update Hero CTA
  if (heroDownloadBtn) {
    heroDownloadBtn.href = downloadUrl;
    heroDownloadBtn.innerHTML = `
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
        <polyline points="7 10 12 15 17 10"></polyline>
        <line x1="12" y1="15" x2="12" y2="3"></line>
      </svg>
      Download for ${osName} (${fileExt})
    `;
  }

  if (detectedOSLabel) {
    detectedOSLabel.textContent = osName;
  }

  // Auto-activate corresponding tab
  switchOSTab(detectedOS);
}

// 2. OS Download Tabs Switcher
function initOSTabs() {
  const tabBtns = document.querySelectorAll('.os-tab-btn');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetOS = btn.getAttribute('data-os');
      switchOSTab(targetOS);
    });
  });
}

function switchOSTab(os) {
  // Update Buttons
  document.querySelectorAll('.os-tab-btn').forEach(btn => {
    if (btn.getAttribute('data-os') === os) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  // Update Panels
  document.querySelectorAll('.os-panel').forEach(panel => {
    if (panel.id === `panel-${os}`) {
      panel.classList.add('active');
    } else {
      panel.classList.remove('active');
    }
  });
}

// 3. 1-Click Copy to Clipboard
function initCopyButtons() {
  document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const textToCopy = btn.getAttribute('data-clipboard');
      if (!textToCopy) return;

      navigator.clipboard.writeText(textToCopy).then(() => {
        const originalHTML = btn.innerHTML;
        btn.innerHTML = `
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="20 6 9 17 4 12"></polyline>
          </svg>
          <span style="color: #10b981;">Copied!</span>
        `;
        setTimeout(() => {
          btn.innerHTML = originalHTML;
        }, 2000);
      });
    });
  });
}

// 4. ScrollSpy for Documentation Sidebar
function initDocsScrollSpy() {
  const articles = document.querySelectorAll('.docs-article');
  const navLinks = document.querySelectorAll('.docs-nav-link');

  if (!articles.length || !navLinks.length) return;

  window.addEventListener('scroll', () => {
    let currentId = '';
    articles.forEach(article => {
      const sectionTop = article.offsetTop - 120;
      if (window.scrollY >= sectionTop) {
        currentId = article.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${currentId}`) {
        link.classList.add('active');
      }
    });
  });
}

// 5. Documentation Live Search
function initDocsSearch() {
  const searchInput = document.getElementById('docsSearchInput');
  if (!searchInput) return;

  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase().trim();
    const articles = document.querySelectorAll('.docs-article');

    articles.forEach(article => {
      const text = article.textContent.toLowerCase();
      if (!query || text.includes(query)) {
        article.style.display = 'block';
      } else {
        article.style.display = 'none';
      }
    });
  });
}
