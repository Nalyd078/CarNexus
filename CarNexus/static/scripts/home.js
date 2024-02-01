function addMerkenEventListeners() {

    let infoItems = document.querySelectorAll('.merk-item-info svg');

    infoItems.forEach(function (item) {
        item.addEventListener('mouseenter', function () {
            let tooltip = this.closest('.merk-item-info').querySelector('.tooltip');
            tooltip.style.visibility = 'visible';
            tooltip.style.opacity = 1;
            tooltip.style.transform = 'translateX(-50%) translateY(0px)';
        });
    
        item.addEventListener('mouseleave', function () {
            let tooltip = this.closest('.merk-item-info').querySelector('.tooltip');
            tooltip.style.visibility = 'hidden';
            tooltip.style.opacity = 0;
            tooltip.style.transform = 'translateX(-50%) translateY(10px)';
        });
    
        item.addEventListener('touchend', function () {
            let tooltip = this.closest('.merk-item-info').querySelector('.tooltip');
            setTimeout(function() {
                tooltip.style.visibility = 'hidden';
                tooltip.style.opacity = 0;
                tooltip.style.transform = 'translateX(-50%) translateY(10px)';
            }, 500);
        });
    });    

    document.querySelectorAll('.info-icon').forEach(item => {
        item.addEventListener('click', function () {
            merkInfo = JSON.parse(this.getAttribute('data-merkinfo'));
            openPopup(merkInfo);
            var leesMeerLink = document.getElementById('leesMeerLink');
            leesMeerLink.addEventListener('click', function(event) {
                event.preventDefault();
            });
        });
        
    });    

    document.getElementById('gridViewButton').addEventListener('click', function () {
        this.classList.toggle('toggle');
    });

}

function openPopup(merkInfo) {
    let bestaandePopup = document.querySelector('.popup');
    if (bestaandePopup) {
        bestaandePopup.remove();
    }

    const popup = document.createElement('div');
    popup.classList.add('popup');

    const popupInner = document.createElement('div');
    popupInner.classList.add('popup-inner');

    const popupContent = document.createElement('div');
    popupContent.classList.add('popup-content');

    const logoSrc = merkInfo && merkInfo.logo ? `/static/${merkInfo.logo}` : 'fallback-logo.png';
    console.log(merkInfo);
    popupContent.innerHTML = `
        <img src="${logoSrc}" alt="${merkInfo.merknaam} logo" class="popup-logo">
        <h2>${merkInfo.merknaam}</h2>
        <div class="text-image-container">
            <p style="margin: 0; margin-bottom: 13px; text-align: justify;" >
                <img src="/static/${merkInfo['1st_production_car']}" alt="Foto van de eerste productie auto van ${merkInfo.merknaam}" class="inline-image">
                ${merkInfo.merk_info.merk_beschrijving}
            </p>
        </div>
        <a href="#" id="leesMeerLink" class="leesMeerLink">Lees meer over ${merkInfo.merknaam}</a>
    `;

    const closeButton = document.createElement('span');
    closeButton.classList.add('popup-close');
    closeButton.innerHTML = '&times;';
    closeButton.style.cssText = 'position: absolute; top: 10px; right: 30px; cursor: pointer; font-size: 24px;';

    popupInner.appendChild(closeButton);
    popupInner.appendChild(popupContent);

    popup.appendChild(popupInner);

    document.body.appendChild(popup);

    popup.addEventListener('click', function (e) {
        if (e.target === this) {
            popup.remove(); 
        }
    });

    function startImageSlider() {
        const firstImageSrc = `/static/${merkInfo['1st_production_car']}`;
        const secondImageSrc = `/static/${merkInfo['recent_production_car']}`;
        const imageElement = document.querySelector('.inline-image');
        const imageAltBase = "Foto van de ";
        const imageTitles = [
            `${imageAltBase}eerste productie auto van ${merkInfo.merknaam}`,
            `${imageAltBase}meest recente productie auto van ${merkInfo.merknaam}`
        ];
        
        let showingFirstImage = false;
        let currentImageIndex = 1;
    
        function loadImage(src, callback) {
            const img = new Image();
            img.src = src;
            img.onload = callback;
        }
    
        function toggleImage() {
            showingFirstImage = !showingFirstImage;
            currentImageIndex = showingFirstImage ? 0 : 1;
            const nextImageSrc = showingFirstImage ? firstImageSrc : secondImageSrc;
            const nextImageAlt = imageTitles[currentImageIndex];
            const nextImageTitle = imageTitles[currentImageIndex];
    
            loadImage(nextImageSrc, function () {
                imageElement.src = nextImageSrc;
                imageElement.alt = nextImageAlt;
                imageElement.title = nextImageTitle;
                imageElement.classList.remove('fade-in');
                void imageElement.offsetWidth;
                imageElement.classList.add('fade-in');
            });
        }
    
        toggleImage();
    
        setInterval(toggleImage, 5000);
    }
        
    startImageSlider();

    closeButton.addEventListener('click', function(e) {
        e.stopPropagation();
        popup.remove();
    });
}

$(document).ready(function () {
    addMerkenEventListeners();
});
