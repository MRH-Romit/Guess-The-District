const map = L.map('map').setView([23.685, 90.3563], 7);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Generate a random color
function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

fetch('bangladesh_geojson_adm2_64_districts_zillas.json')
  .then(res => res.json())
  .then(data => {
    L.geoJSON(data, {
      style: () => ({
        color: '#000000', // border color
        weight: 1,
        fillOpacity: 0.6,
        fillColor: getRandomColor()
      }),
      onEachFeature: () => {} // No popup or label
    }).addTo(map);
  });
