$(document).ready(function () {
    console.log("sdfasd");

    var map = L.map('mapid',{
        minZoom:10.5,
    });
    map.setView([28.2957487, 83.8123341], 11);
    // console.log(scale);
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
    googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
    });
    googleTerrain = L.tileLayer('http://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',{
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
    });

    var mapboxTiles = L.tileLayer('https://api.mapbox.com/styles/v1/skshitiz1/cjvosths00oqu1cln1v7765pf/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1Ijoic2tzaGl0aXoxIiwiYSI6ImNqcmJ2czBjODBhMTgzeWxwM2t1djJuaXUifQ.wlFktg-soH3B_pqVyJj2Ig').addTo(map);
    var baseLayers = {
                    "OpenStreetMap": osm,
                    "Google Streets": googleStreets,
                    "Google Hybrid": googleHybrid,
                    "Google Satellite": googleSat,
                    "Google Terrain": googleTerrain,
                    "Mapbox Tiles": mapboxTiles
                };
                
                // map.addLayer(osm);
    layerswitcher = L.control.layers(baseLayers, {}, {collapsed: true}).addTo(map);
    var base= new L.geoJson.ajax("assests/data/annapurna.geojson", { 
        console.log("from inside");
              });
    base.addto(map);
    });
                  