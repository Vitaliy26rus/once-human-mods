let modsData = null;
fetch('data.json')
  .then(res => res.json())
  .then(data => { modsData = data; renderTable(); });

const tableBody = document.querySelector('#modTable tbody');
const searchInput = document.getElementById('search');
const langSelect = document.getElementById('lang');

searchInput.addEventListener('input', renderTable);
langSelect.addEventListener('change', renderTable);

function renderTable() {
  if(!modsData) return;
  const query = searchInput.value.toLowerCase();
  const lang = langSelect.value;
  tableBody.innerHTML = '';
  modsData.mods.forEach(mod => {
    const name = mod.name[lang].toLowerCase();
    if(name.includes(query)) {
      const containers = mod.containers.map(cid => {
        const c = modsData.containers.find(x => x.id===cid);
        return c ? c.name[lang] : cid;
      }).join(', ');
      const tr = document.createElement('tr');
      tr.innerHTML = `<td>${mod.name[lang]}</td>
                      <td>${mod.category}</td>
                      <td>${mod.tier.join(', ')}</td>
                      <td>${mod.effect[lang]}</td>
                      <td>${containers}</td>`;
      tableBody.appendChild(tr);
    }
  });
}