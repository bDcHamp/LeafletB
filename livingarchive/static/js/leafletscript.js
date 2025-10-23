// Wait until DOM is ready (important in Django templates)
document.addEventListener("DOMContentLoaded", function () {

    // Check if map container exists
    const mapContainer = document.getElementById("map");
    if (!mapContainer) {
        console.error("Map container not found!");
        return;
    }

    // Initialize the Leaflet map centered on West Arnhem Land
    const map = L.map("map", { attributionControl: false }).setView([-12.4, 134.3], 8);

    // Use OpenStreetMap tiles (visible base layer)
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 18,
        attribution: "© OpenStreetMap contributors",
    }).addTo(map);

    // Define your marker
    const markerData = {
        name: "Mandilbareng / Mardbabay",
        coordinates: [-12.4, 134.3],
        videoUrl: "/cms/mandilbareng-mardbabay-a-living-cultural-landscape/",
        description:
            "The rock art at Mandilbareng (Mardbabay) in Western Arnhem Land is part of a living cultural landscape. It connects people, ancestors, animals, and seasons. Elders and families maintain and restore these places, ensuring that knowledge continues across generations.",
    };

    // Create the marker
    const marker = L.marker(markerData.coordinates).addTo(map);

    // Create the popup content
    const popupContent = `
        <div id="content">
            <h2 style="font-size:150%;" class="firstHeading">${markerData.name}</h2>
            <div id="bodyContent">
                <p style="font-size:130%;">${markerData.description}</p>
                <p><a href="${markerData.videoUrl}" target="_blank" style="color:#0078A8;text-decoration:none;">Read more →</a></p>
            </div>
        </div>
    `;

    marker.bindPopup(popupContent, { minWidth: 400 });
});
