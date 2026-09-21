// ==========================================================================
// AI Learning Lab - Dynamic Documentation & Release Portal Logic
// ==========================================================================

const GITHUB_REPO = 'Rajdeep-Mudiar/AI_Learning_Desktop_App';
const GITHUB_API_LATEST_RELEASE = `https://api.github.com/repos/${GITHUB_REPO}/releases/latest`;
const FALLBACK_VERSION = 'v1.0.4';

let currentReleaseData = null;

document.addEventListener('DOMContentLoaded', () => {
  initOSTabs();
  initCopyButtons();
  initDocsScrollSpy();
  initDocsSearch();
  fetchLatestRelease();
});

// 1. Fetch Latest GitHub Release Dynamically from GitHub API
async function fetchLatestRelease() {
  try {
    const response = await fetch(GITHUB_API_LATEST_RELEASE);
    if (!response.ok) {
      throw new Error(`GitHub API returned status ${response.status}`);
    }
    const release = await response.json();
    currentReleaseData = release;
    updatePageWithRelease(release);
  } catch (error) {
    console.warn('Could not fetch live GitHub release, using fallback configuration:', error);
    // Use fallback tag
    updateVersionBadges(FALLBACK_VERSION);
    initOSDetection(null);
  }
}

// 2. Update Page Elements with Live Release Info
function updatePageWithRelease(release) {
  const tagName = release.tag_name || FALLBACK_VERSION;
  const publishedDate = release.published_at ? new Date(release.published_at).toLocaleDateString(undefined, { year: 'numeric', month: 'short', day: 'numeric' }) : '';
  const assets = release.assets || [];

  // Update Version Badges & Labels across the page
  updateVersionBadges(tagName, publishedDate);

  // Parse Asset URLs from GitHub Release
  const assetMap = parseReleaseAssets(assets, tagName);

  // Update Download Cards and Links
  updateDownloadLinks(assetMap);

  // Initialize OS Detection with dynamic URLs
  initOSDetection(assetMap);
}

function updateVersionBadges(version, dateStr = '') {
  document.querySelectorAll('.version-badge-val').forEach(el => {
    el.textContent = version;
  });

  const heroBadge = document.getElementById('heroVersionBadge');
  if (heroBadge) {
    heroBadge.textContent = `Version ${version} Live ${dateStr ? '• Released ' + dateStr : ''} — 28 Courses & 5 Complete Engineering Tracks`;
  }
}

function parseReleaseAssets(assets, tagName) {
  const assetMap = {
    // Windows
    winExe: null,
    winMsi: null,
    winZip: null,
    // macOS
    macDmgUniversal: null,
    macDmgArm: null,
    macDmgIntel: null,
    // Linux
    linuxAppImage: null,
    linuxDeb: null,
    linuxRpm: null,
  };

  assets.forEach(asset => {
    const name = asset.name.toLowerCase();
    const url = asset.browser_download_url;
    const sizeMb = (asset.size / (1024 * 1024)).toFixed(1);

    if (name.endsWith('.exe')) {
      assetMap.winExe = { url, name: asset.name, size: `${sizeMb} MB` };
    } else if (name.endsWith('.msi')) {
      assetMap.winMsi = { url, name: asset.name, size: `${sizeMb} MB` };
    } else if (name.includes('windows') && name.endsWith('.zip')) {
      assetMap.winZip = { url, name: asset.name, size: `${sizeMb} MB` };
    } else if (name.endsWith('.dmg')) {
      if (name.includes('aarch64') || name.includes('arm64')) {
        assetMap.macDmgArm = { url, name: asset.name, size: `${sizeMb} MB` };
      } else if (name.includes('x64') || name.includes('x86_64')) {
        assetMap.macDmgIntel = { url, name: asset.name, size: `${sizeMb} MB` };
      } else {
        assetMap.macDmgUniversal = { url, name: asset.name, size: `${sizeMb} MB` };
      }
    } else if (name.endsWith('.appimage')) {
      assetMap.linuxAppImage = { url, name: asset.name, size: `${sizeMb} MB` };
    } else if (name.endsWith('.deb')) {
      assetMap.linuxDeb = { url, name: asset.name, size: `${sizeMb} MB` };
    } else if (name.endsWith('.rpm')) {
      assetMap.linuxRpm = { url, name: asset.name, size: `${sizeMb} MB` };
    }
  });

  // Fallbacks to latest download URLs if assets array was empty (draft or source-only tag)
  const baseDownload = `https://github.com/${GITHUB_REPO}/releases/download/${tagName}`;
  if (!assetMap.winExe) assetMap.winExe = { url: `${baseDownload}/AI-Learning-Lab-Setup-x64.exe`, size: 'Recommended' };
  if (!assetMap.winMsi) assetMap.winMsi = { url: `${baseDownload}/AI-Learning-Lab-x64.msi`, size: 'Enterprise' };
  if (!assetMap.winZip) assetMap.winZip = { url: `${baseDownload}/AI-Learning-Lab-Portable-x64.zip`, size: 'Portable' };

  if (!assetMap.macDmgUniversal) assetMap.macDmgUniversal = { url: `${baseDownload}/AI-Learning-Lab-Universal.dmg`, size: 'Universal' };
  if (!assetMap.macDmgArm) assetMap.macDmgArm = { url: `${baseDownload}/AI-Learning-Lab-aarch64.dmg`, size: 'Apple Silicon' };
  if (!assetMap.macDmgIntel) assetMap.macDmgIntel = { url: `${baseDownload}/AI-Learning-Lab-x64.dmg`, size: 'Intel' };

  if (!assetMap.linuxAppImage) assetMap.linuxAppImage = { url: `${baseDownload}/AI-Learning-Lab-x86_64.AppImage`, size: 'Universal' };
  if (!assetMap.linuxDeb) assetMap.linuxDeb = { url: `${baseDownload}/ai-learning-lab_amd64.deb`, size: 'Debian/Ubuntu' };
  if (!assetMap.linuxRpm) assetMap.linuxRpm = { url: `${baseDownload}/ai-learning-lab.x86_64.rpm`, size: 'Fedora/RHEL' };

  return assetMap;
}

function updateDownloadLinks(assetMap) {
  // Helper to bind link and size
  const bindLink = (elemId, sizeElemId, asset) => {
    const el = document.getElementById(elemId);
    if (el && asset) {
      el.href = asset.url;
    }
    const sizeEl = document.getElementById(sizeElemId);
    if (sizeEl && asset && asset.size) {
      sizeEl.textContent = asset.size;
    }
  };

  bindLink('link-win-exe', 'size-win-exe', assetMap.winExe);
  bindLink('link-win-msi', 'size-win-msi', assetMap.winMsi);
  bindLink('link-win-zip', 'size-win-zip', assetMap.winZip);
  bindLink('btn-win-main', null, assetMap.winExe);

  bindLink('link-mac-universal', 'size-mac-universal', assetMap.macDmgUniversal);
  bindLink('link-mac-arm', 'size-mac-arm', assetMap.macDmgArm);
  bindLink('link-mac-intel', 'size-mac-intel', assetMap.macDmgIntel);
  bindLink('btn-mac-main', null, assetMap.macDmgUniversal || assetMap.macDmgArm);

  bindLink('link-linux-appimage', 'size-linux-appimage', assetMap.linuxAppImage);
  bindLink('link-linux-deb', 'size-linux-deb', assetMap.linuxDeb);
  bindLink('link-linux-rpm', 'size-linux-rpm', assetMap.linuxRpm);
  bindLink('btn-linux-main', null, assetMap.linuxAppImage);
}

// 3. Detect Operating System and Configure Hero CTA
function initOSDetection(assetMap) {
  const userAgent = window.navigator.userAgent.toLowerCase();
  const heroDownloadBtn = document.getElementById('heroDownloadBtn');
  
  let detectedOS = 'windows';
  let osName = 'Windows';
  let downloadUrl = assetMap ? assetMap.winExe?.url : `https://github.com/${GITHUB_REPO}/releases/latest/download/AI-Learning-Lab-Setup-x64.exe`;
  let fileExt = '.exe';

  if (userAgent.indexOf('mac') !== -1 || userAgent.indexOf('darwin') !== -1) {
    detectedOS = 'macos';
    osName = 'macOS';
    downloadUrl = assetMap ? (assetMap.macDmgUniversal?.url || assetMap.macDmgArm?.url) : `https://github.com/${GITHUB_REPO}/releases/latest/download/AI-Learning-Lab-Universal.dmg`;
    fileExt = '.dmg';
  } else if (userAgent.indexOf('linux') !== -1 || userAgent.indexOf('x11') !== -1) {
    detectedOS = 'linux';
    osName = 'Linux';
    downloadUrl = assetMap ? assetMap.linuxAppImage?.url : `https://github.com/${GITHUB_REPO}/releases/latest/download/AI-Learning-Lab-x86_64.AppImage`;
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

  // Auto-activate corresponding tab
  switchOSTab(detectedOS);
}

// 4. OS Download Tabs Switcher
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
  document.querySelectorAll('.os-tab-btn').forEach(btn => {
    if (btn.getAttribute('data-os') === os) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  document.querySelectorAll('.os-panel').forEach(panel => {
    if (panel.id === `panel-${os}`) {
      panel.classList.add('active');
    } else {
      panel.classList.remove('active');
    }
  });
}

// 5. 1-Click Copy to Clipboard
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

// 6. ScrollSpy for Documentation Sidebar
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

// 7. Documentation Live Search
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
