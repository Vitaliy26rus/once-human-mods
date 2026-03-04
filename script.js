const jsonUrl = "data.json";
let data, lang = "ru";

async function loadData() {
  const res = await fetch(jsonUrl);
  data = await res.json();
  renderTable();
}

function renderTable() {
  const columns = data.ui_labels.columns;
  const headerRow = document.getElementById("table-header");
  headerRow.innerHTML = "";
  ["name", "mod", "container", "description", "source"].forEach(col => {
    const th = document.createElement("th");
    th.textContent = columns[col][lang];
    headerRow.appendChild(th);
  });

  document.getElementById("table-title").textContent = data.ui_labels.table_title[lang];

  const tbody = document.getElementById("table-body");
  tbody.innerHTML = "";

  // Оружие
  data.weapons.forEach(w => {
    w.mods.forEach(m => {
      const tr = document.createElement("tr");
      const cells = [
        w.name[lang],
        m.name[lang],
        m.source,
        "",
        ""
      ];
      cells.forEach(c => { const td = document.createElement("td"); td.textContent = c; tr.appendChild(td); });
      tbody.appendChild(tr);
    });
  });

  // Броня
  data.armor.forEach(a => {
    a.mods.forEach(m => {
      const tr = document.createElement("tr");
      const cells = [
        a.name[lang],
        m.name[lang],
        m.source,
        "",
        ""
      ];
      cells.forEach(c => { const td = document.createElement("td"); td.textContent = c; tr.appendChild(td); });
      tbody.appendChild(tr);
    });
  });
}

document.getElementById("lang-select").addEventListener("change", e => {
  lang = e.target.value;
  renderTable();
});

loadData();