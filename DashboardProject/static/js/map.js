var highPin = L.icon({
    iconUrl: '../static/images/pin_high.png',
    iconSize: [25, 40]
});
var medPin = L.icon({
    iconUrl: '../static/images/pin_medium.png',
    iconSize: [25, 40]
});
var lowPin = L.icon({
    iconUrl: '../static/images/pin_low.png',
    iconSize: [25, 40]
});

var display_pins = [];
const cityAQI = [];

for (var i = 0; i < cityCoord.length / 4; i++) {
    var cityId = cityCoord[i * 4];
    var cityName = cityCoord[i * 4 + 1];
    var lat = cityCoord[i * 4 + 2];
    var long = cityCoord[i * 4 + 3];

    var icon = highPin;
    // if (AQI > 70) {
    //     icon = highPin;
    // }
    // else if (AQI > 40) {
    //     icon = medPin;
    // }
    // else {
    //     icon = lowPin;
    // }

    row = [cityName, lat, long, icon];
    display_pins.push(row);
}

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

// AK 
var mapAK = L.map('mapAK', {
    center: [64, -154],
    zoom: 3
});
mapAK.setMaxBounds(mapAK.getBounds());
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
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    minZoom: 6,
    maxZoom: 9
}).addTo(mapHI);

window.alert(display_pins.length)
for (var i = 0; i < display_pins.length; i++) {
    var cityName = display_pins[i][0];
    lat = Number(display_pins[i][1]);
    long = Number(display_pins[i][2]);
    icon = display_pins[i][3]

    var marker = L.marker([lat, long], { icon: icon }).addTo(mapUS)
        .bindPopup(
            '<div id="pin_content">' + cityName + '<br>('
            + lat + ', ' + long + ')</div>'
            + '<form action="analysis" method="post">'
            + '<input type="hidden" value="' + cityName + '" name="city">'
            + '<input type="hidden" value="' + lat + '" name="latitude">'
            + '<input type="hidden" value="' + long + '" name="longitude">'
            + '<input type="submit" value="Go to Analysis">'
            + '</form></div>'
        );
    var marker2 = L.marker([lat, long], { icon: icon }).addTo(mapAK)
        .bindPopup(
            '<div id="pin_content">' + cityName + '<br>('
            + lat + ', ' + long + ')</div>'
            + '<form action="analysis" method="post">'
            + '<input type="hidden" value="' + cityName + '" name="city">'
            + '<input type="hidden" value="' + lat + '" name="latitude">'
            + '<input type="hidden" value="' + long + '" name="longitude">'
            + '<input type="submit" value="Go to Analysis">'
            + '</form></div>'
        );
    var marker3 = L.marker([lat, long], { icon: icon }).addTo(mapHI)
        .bindPopup(
            '<div id="pin_content">' + cityName + '<br>('
            + lat + ', ' + long + ')</div>'
            + '<form action="analysis" method="post">'
            + '<input type="hidden" value="' + cityName + '" name="city">'
            + '<input type="hidden" value="' + lat + '" name="latitude">'
            + '<input type="hidden" value="' + long + '" name="longitude">'
            + '<input type="submit" value="Go to Analysis">'
            + '</form></div>'
        );
}