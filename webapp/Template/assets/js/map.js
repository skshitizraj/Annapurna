$(document).ready(function () {
    // console.log("sdfasd");

    var map = L.map('mapid',{
        minZoom:10.5,
    });
    map.setView([28.2957487, 83.8123341], 10.5);

    osm = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    });
                
    var googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
    }).addTo(map);
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
    mapboxTiles = L.tileLayer('https://api.mapbox.com/styles/v1/skshitiz1/cjvosths00oqu1cln1v7765pf/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1Ijoic2tzaGl0aXoxIiwiYSI6ImNqcmJ2czBjODBhMTgzeWxwM2t1djJuaXUifQ.wlFktg-soH3B_pqVyJj2Ig')
    
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
        // console.log('from');
        var dataLayer=L.geoJson(data,{
            style:{
                fillColor: " #172f76 ",
                fillOpacity: 0.9,
                color:"#ffffff",
                opacity: 1,
                weight: 2,
            },
            onEachFeature:function(feature, layer) {
                layer.on({
                    mouseover: function () {
                        this.setStyle({
                            'fillOpacity':0.3,
                        });
                    },
                    mouseout: function () {
                        this.setStyle({
                            // 'fillColor': ' #ffff01 ',
                            'fillColor': ' #172f76 ',
                            'fillOpacity':0.9,
                        });
                    },
                    click: function (event) {
                        if (event.target==layer){
                            // console.log("hello");
                            document.getElementById('toHide').style.display='none';
                            document.getElementById('popup').innerHTML="<a class=\"nav-link rightside\" function=\"cross\">Cancel<i class=\"la la-close\"></i></a>";

                            var tableContent=document.createElement("TableContent");
                            var tableTitle=document.createElement("TableTitle");    
                            var table=document.createElement("Table");
                            var crossmarker=document.createElement("crossmark");
                            // crossmarker.setAttribute("class","la la-close rightside");
                            tableTitle.setAttribute("class","card border rounded card-header backgroundcolourcss h5");
                            // tableTitle.appendChild(crossmarker);
                            var text1 = document.createTextNode("Annapurna RM");
                            tableTitle.appendChild(text1);
                            table.setAttribute("class","table table-bordered table-hover");
    
                            table.innerHTML+="<table><tbody><tr><td><strong>Ward Number</strong></td><td>"+feature.properties.new_ward_n+"</td></tr><tr><td><strong>District</strong></td><td>"+feature.properties.district+"</td></tr><tr><td><strong>Area (sq.km.)</strong></td><td>"+feature.properties.area_sqkm+"</td></tr></tbody></table>";
    
                            tableContent.appendChild(tableTitle);
                            tableContent.appendChild(table);
                            document.getElementById("popup").appendChild(tableContent);
                        }
                    }
                });
                layer.bindTooltip(String(feature.properties.new_ward_n), {permanent:true,direction:'center',className: 'wardClassName'});
            },
        }).addTo(map);
        map.fitBounds(dataLayer.getBounds());
    })
});
