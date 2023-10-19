$(document).ready(function () {

    
    // Carousel de Air Quality
    let carouselIndex = 0;
    let carouselAnimDuration = 300
    let carouselAnimEnd = true
    
    $(".forecast-actions-buttons").click(function (e) { 
        if (carouselAnimEnd) {
            carouselAnimEnd = false;
            idButton = e["currentTarget"]["id"]
            if (idButton == "forecast-actions-button-next" && carouselIndex <= 17) {
                carouselIndex ++;
            }
            else if (idButton == "forecast-actions-button-previous" && carouselIndex > 0){
                carouselIndex --;
            }
            
            
            $("#forecast-carousel-main").fadeOut(0);
            $("#forecast-carousel-main").css("transform", `translateX(calc(-4.166% * ${carouselIndex}))`);
            $("#forecast-carousel-main").fadeIn(carouselAnimDuration);
            
            if (carouselIndex <= 0 || carouselIndex >= 18) {
                $(this).prop("disabled", true);;
            }
            else {
                $(".forecast-actions-buttons").prop("disabled", false);
            }
            
            setTimeout(() => {  
                carouselAnimEnd = true;
            }, carouselAnimDuration);
        }
    });
    

    $('#search-box-text').on('input', function(){
        var text = $(this).val();
        $.ajax({
            type: "POST",
            url: "/r",
            data: { text: text },
            dataType: "json",
            success: function(response) {
                $("#search-autocomplete-div").empty();
                response.text.forEach(element => {
                    $("#search-autocomplete-div").append(`<input name="place_autocomplete" type="submit" class="search-autocomplete-div-submit" value="${element}">`);
                });
            }
        });
    });

    $("#layout-search-show").click(function (e) { 
        $("#search").css("display", "flex");
        $('#search-box-text').focus();
        $(".weather-sections").css("opacity", "60%");
    });
    
    $("#search-exit").click(function (e) { 
        searchExit();
    });

    function searchExit() {
        $("#search").css("display", "none");
        $(".weather-sections").css("opacity", "100%");
    }

    $("#search-box-text").blur(function (e) {
        setTimeout(() => {
            searchExit();
        }, 100);
    });

    $("#search-box-text").on("keydown", function (e) {
        if (e.originalEvent.key == "Enter"){
            $('.search-autocomplete-div-submit:first').click();
        }
    });
});
