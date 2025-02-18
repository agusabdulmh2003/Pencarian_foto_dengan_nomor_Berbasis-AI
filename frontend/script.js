function searchPhotos() {
    const bibNumber = document.getElementById("bibNumber").value;
    if (!bibNumber) {
        alert("Masukkan nomor dada terlebih dahulu!");
        return;
    }

    fetch(`http://localhost:5000/search?number=${bibNumber}`)
        .then(response => response.json())
        .then(data => {
            const gallery = document.getElementById("gallery");
            gallery.innerHTML = ""; // Kosongkan galeri sebelumnya
            
            if (data.length === 0) {
                gallery.innerHTML = "<p>Tidak ada foto ditemukan.</p>";
            } else {
                data.forEach(url => {
                    const img = document.createElement("img");
                    img.src = url;
                    gallery.appendChild(img);
                });
            }
        })
        .catch(error => console.error("Error fetching photos:", error));
}
