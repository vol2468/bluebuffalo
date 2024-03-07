// Sample pins
var highPin = L.icon({
    iconUrl: '../images/pin_high.png',
    iconSize: [25, 40]
});
var medPin = L.icon({
    iconUrl: '../images/pin_medium.png',
    iconSize: [25, 40]
});
var lowPin = L.icon({
    iconUrl: '../images/pin_low.png',
    iconSize: [25, 40]
});

// US
var mapUS = L.map('mapUS', {
    center: [38, -94],
    zoom: 4
});
mapUS.setMaxBounds(mapUS.getBounds());

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    minZoom: 4,
    maxZoom: 9
}).addTo(mapUS);
var markerUS = L.marker([41, -111], { icon: highPin }).addTo(mapUS);

var moreInfoPagePopUS = L.marker([33.649874, -112.183847], { icon: highPin }).addTo(mapUS)
    .bindPopup('<div id="pin_content">Phoenix<br>(Lat, Long)</div>');


// AK 

var mapAK = L.map('mapAK', {
    center: [64, -154],
    zoom: 3
});
mapAK.setMaxBounds(mapAK.getBounds());
var marker2 = L.marker([62, -152], { icon: medPin }).addTo(mapAK);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    minZoom: 3,
    maxZoom: 9
}).addTo(mapAK);

// HI 
var mapHI = L.map('mapHI', {
    center: [20.58293690411966, -157.55602610564011],
    zoom: 6
});
mapHI.setMaxBounds(mapHI.getBounds());
var marker3 = L.marker([22, -159], { icon: lowPin }).addTo(mapHI);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    minZoom: 6,
    maxZoom: 9
}).addTo(mapHI);