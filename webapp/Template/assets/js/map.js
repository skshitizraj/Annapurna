$(document).ready(function () {
    console.log("sdfasd");

    var map = L.map('mapid',{
        minZoom:8,
    });
    map.setView([28.2957487, 83.8123341], 8);

    osm = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    });
                
    googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
    });
    googleHybrid = L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',{
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
    });
    var googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
    }).addTo(map);
    googleTerrain = L.tileLayer('http://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',{
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
    });
    mapboxTiles = L.tileLayer('https://api.mapbox.com/styles/v1/skshitiz1/cjvosths00oqu1cln1v7765pf/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1Ijoic2tzaGl0aXoxIiwiYSI6ImNqcmJ2czBjODBhMTgzeWxwM2t1djJuaXUifQ.wlFktg-soH3B_pqVyJj2Ig')
    
    // var mapboxTiles = L.tileLayer('https://api.mapbox.com/styles/v1/skshitiz1/cjvosths00oqu1cln1v7765pf/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1Ijoic2tzaGl0aXoxIiwiYSI6ImNqcmJ2czBjODBhMTgzeWxwM2t1djJuaXUifQ.wlFktg-soH3B_pqVyJj2Ig').addTo(map);
    
    var baseLayers = {
                    "OpenStreetMap": osm,
                    "Google Streets": googleStreets,
                    "Google Hybrid": googleHybrid,
                    "Google Satellite": googleSat,
                    "Google Terrain": googleTerrain,
                    "Mapbox Tiles": mapboxTiles
                };
                
    layerswitcher = L.control.layers(baseLayers, {}, {collapsed: true}).addTo(map);

    $.getJSON("http://127.0.0.1:8000/api/annapurna", function (data) {
        console.log('from tera baje');
        var dataLayer=L.geoJson(data,{
            style: countriesStyle,
            onEachFeature: onEachFeature,
        }).addTo(map);

        function countriesStyle(feature) {
            return {
                fillColor: " #ffff01 ",
                fillOpacity: 1,
                color: '#172f76',
                opacity: 1,
                weight: 2,
            }
        }
        
        function onEachFeature(feature, layer) {
            layer.on({
                mouseover: function () {
                    this.setStyle({
                        'fillOpacity':0,
                    });
                },
                mouseout: function () {
                    this.setStyle({
                        'fillColor': ' #ffff01 ',
                        'fillOpacity':1,
                    });
                }
            });
         }
        map.fitBounds(dataLayer.getBounds());
      });
    // var marker = L.marker([28.2096, 83.9856]).addTo(map);
    // marker.on('click', function(){
    //     document.getElementById('toHide').style.display='none';
    //     var element = document.createElement("toShow");
    //     document.getElementById("sidebar").appendChild(element);
    //     }
    // );
    // marker.on('click', function(){
    //     document.getElementById('toHide').style.display='none';
    //     document.getElementById('popup').style.display='block';
    //     }
    // );
});
