$(document).ready(function () {
    // console.log("sdfasd");

    var map = L.map('mapid',{
        minZoom:10.5,
        preferCanvas:true,
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
    
    var printProvider = L.print.Provider({
        method: 'GET',
        url: ' http://path/to/mapfish/print',
        autoLoad: true,
        dpi: 90
     });
     
     var printControl = L.control.print({
        provider: printProvider
     });        
     map.addControl(printControl);
       




    var baseLayers = {
                    "OpenStreetMap": osm,
                    "Google Streets": googleStreets,
                    "Google Hybrid": googleHybrid,
                    "Google Satellite": googleSat,
                    "Google Terrain": googleTerrain,
                    "Mapbox Tiles": mapboxTiles
                };
                
    layerswitcher = L.control.layers(baseLayers, {}, {collapsed: true}).addTo(map);
    // const ee = require('@google/earthengine');
    // ee.data.authenticateViaPrivateKey('data/privatekey.json');
    // ee.initialize();

<<<<<<< HEAD
    $.getJSON("http://127.0.0.1:8000/api/ward/all", function (data) {
=======
    $.getJSON("http://127.0.0.1:8000/api/ward/all/", function (data) {
>>>>>>> 5e7b0ce4c26cafe8af0bafbf6ac30e52c220fdce
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
                            document.getElementById('popup').innerHTML="";

                            var tableContent=document.createElement("TableContent");
                            var tableTitle=document.createElement("TableTitle");    
                            var table=document.createElement("Table");
                            var tableOuter=document.createElement("Tableouter");
                            var crossmarker=document.createElement("i");
                            crossmarker.setAttribute("class","la la-close");
                            crossmarker.setAttribute("id","close");
                            tableOuter.setAttribute("class","card-body d-table");
                            tableContent.setAttribute("class","card border rounded");
                            tableTitle.setAttribute("class","card-header text-white backgroundcolourcss h5");
                            var text1 = document.createTextNode("Annapurna RM");
                            tableTitle.appendChild(text1);
                            table.setAttribute("class","table-responsive table-borderless table table-hover fontSize");
    
                            table.innerHTML+="<table><thead class=\"text-left\"><tr></tr></thead><tbody><tr><td>Ward Number</td><td>"+feature.properties.new_ward_n+"</td></tr><tr><td>District</td><td>"+feature.properties.district+"</td></tr><tr><td>Area (sq.km.)</td><td>"+feature.properties.area_sqkm+"</td></tr></tbody></table>";
    
                            tableContent.appendChild(tableTitle);
                            tableOuter.appendChild(table);
                            tableContent.appendChild(tableOuter);
                            document.getElementById("popup").appendChild(crossmarker);
                            document.getElementById("popup").appendChild(tableContent);

                            document.getElementById("close").onclick=function(){
                                // console.log("hello there");
                                document.getElementById("popup").innerHTML="";
                                document.getElementById("toHide").style.display="block";
                            }
                        }
                    }
                });
                layer.bindTooltip(String(feature.properties.new_ward_n), {permanent:true,direction:'center',className: 'wardClassName'});
            },
        }).addTo(map);
        map.fitBounds(dataLayer.getBounds());
    })
});
