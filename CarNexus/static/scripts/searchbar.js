$(document).ready(function() {
    
    function markeerGeselecteerdeOptie() {
        var geselecteerdeTekst = $('.dropdown-selected').text().trim().replace('Sorteer op ', '');
        $('.dropdown-options .option').each(function() {
            if ($(this).text() === geselecteerdeTekst) {
                $(this).addClass('selected');
            } else {
                $(this).removeClass('selected');
            }
        });
    }

    function toggleDropdown() {
        var $categoryDropdown = $('.category-dropdown');
        var $dropdownOptions = $('.dropdown-options');
        $dropdownOptions.toggle();
        $categoryDropdown.toggleClass('active');
        if (!$dropdownOptions.is(':visible')) {
            $categoryDropdown.removeClass('active');
        }
        markeerGeselecteerdeOptie();
    }

    markeerGeselecteerdeOptie();

    $('.dropdown-selected').click(function(event) {
        $('.dropdown-options').toggle();
        markeerGeselecteerdeOptie();
        $('.category-dropdown').css('border-radius', $('.dropdown-options').is(':visible') ? '5px 5px 0 0' : '5px');
        $('.category-dropdown').toggleClass('active', $('.dropdown-options').is(':visible'));
        if (!$('.dropdown-options').is(':visible')) {
            $('.category-dropdown').removeClass('active');
        }
        event.stopPropagation();
    });

    $('.dropdown-options .option').click(function() {
        var text = $(this).text();
        $('.dropdown-selected').html('Sorteer op <span class="highlight">' + text + '</span>');
        $('#categorySelect').val($(this).data('value'));
        $('.dropdown-options').hide();
        $('.category-dropdown').css('border-radius', '5px');
        $('.category-dropdown').removeClass('active');
        
        if (text === "Populariteit") {
            merken.sort(function(first, second) {
                return second.populariteitscore - first.populariteitscore;
            });
        }
        else if (text === "Alfabetisch") {
            merken.sort(function(first, second) {
                return first.merknaam.localeCompare(second.merknaam);
            });
        }
        else if (text === "Land van herkomst") {
            merken.sort(function(first, second) {
                return first.herkomst.localeCompare(second.herkomst);
            });
        }

        $(".merk-lijst").empty();

        fetch('http://localhost:5000/get_svg/info_icon.svg')
        .then(response => response.text())
        .then(icon => {
            info_icon = icon;
        })

        let fetchPromises = merken.map(merk => 
            fetch('http://localhost:5000/get_svg/' + merk.landvlag)
            .then(response => response.text())
            .then(vlag => {
                return { merk, vlag };
            })
        );

        Promise.all(fetchPromises).then(results => {
            results.forEach(({ merk, vlag }) => {
                $(".merk-lijst").append(`
                    <div class="merk-item">
                        <div class="img-placeholder">
                            <img src="/static/${merk.logo}" alt="${merk.merknaam} Car Brand Logo ©">
                        </div>
                        <p>${merk.merknaam}</p>
                        <p>${merk.production}</p>
                        <div class="merk-item-info">
                            ${vlag}
                            <span class="tooltip">Land van herkomst:<br>${merk.herkomst}</span>
                        </div>
                        <div class="info-icon" data-merkinfo='${JSON.stringify(merk)}'>
                            ${info_icon}
                        </div>
                    </div>
                `);
            });
            addMerkenEventListeners();
        });        
    });    

    $(document).click(function(event) {
        if (!$(event.target).closest('.category-dropdown').length) {
            $('.dropdown-options').hide();
            $('.category-dropdown').removeClass('active');
        }
    });

    $("#gridViewButton").click(function() {
        $("#grid-icon-1-container, #grid-icon-2-container").toggle();
    });
});