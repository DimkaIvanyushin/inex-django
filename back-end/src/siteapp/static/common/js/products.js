$(document).ready(function () {

    var $box = $('.box-images');
    var offer_icon = $('a.offer_icon i');

    function addItem(id, icon, url) {

        icon.css('transform', 'scale(0)');
        $.get(url, function (data) { 
        }).done(function () {

            offer_icon.addClass('animated').addClass('rubberBand');
          
            setTimeout(function(){    
                icon.css('transform', 'scale(1)');
                icon.removeClass('fa-cart-plus').addClass('far fas fa-trash-alt')
                offer_icon.removeClass('animated').removeClass('rubberBand');
            },600)
            
        }).fail(function () {
            console.log("error");
        });
    }

    function removeItem(id, icon, url) {

        icon.css('transform', 'scale(0)');

        $.get(url, function (data) {                
        }).done(function () {

            offer_icon.addClass('animated').addClass('rubberBand');  

            setTimeout(function(){
                icon.css('transform', 'scale(1)');
                icon.removeClass('fas fa-trash-alt').addClass('fas fa-cart-plus');
                offer_icon.removeClass('animated').removeClass('rubberBand');
            },600)
                
        }).fail(function () {
            console.log("error");
        });
    }

    function showItems() {
        $('.box-images').each(function( index ) {
            var clicked = $(this).attr('clicked');
            var icon =  $(this).find('i');

            if (clicked == 'true'){
                icon.removeClass('fas fa-cart-plus').addClass('fas fa-trash-alt')
            }
        });
    }

    $box.click(function () {

        var clicked = $(this).attr('clicked');
        var id = $(this).attr("id");
        var icon =  $(this).find('i');
        var url = '';

        if (clicked == 'false'){
            url = '/products/item/add/' + id;
            addItem(id, icon, url);

            $(this).parent().find('i.check-product').addClass('fas fa-check');
            $(this).attr('clicked','true')
        } else {
            url = '/products/item/remove/' + id;
            removeItem(id, icon, url);

            $(this).parent().find('i.check-product').removeClass('fas fa-check');
            $(this).attr('clicked','false')
        }

    })

    showItems();
});