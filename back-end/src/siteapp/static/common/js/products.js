$(document).ready(function () {

    var $box = $('.box-images');
    var offer_icon = $('a.offer_icon i');

    function addItem(th) {
        var id = th.attr("id");
        var url = '/products/item/add/' + id;
        var icon =  th.find('i');

        icon.css('transform', 'scale(0)');

        $.get(url, function (data) { 
        }).done(function () {

            offer_icon.addClass('animated').addClass('rubberBand');
          
            setTimeout(function(){    
                icon.css('transform', 'scale(1)');
                icon.removeClass('fa-plus').addClass('far fa-check-circle')
                offer_icon.removeClass('animated').removeClass('rubberBand');
            },600)
            
        }).fail(function () {
            console.log("error");
        });
    }

    function removeItem(th) {

        var id = th.attr("id");
        var url = '/products/item/remove/' + id;
        var icon =  th.find('i');

        icon.css('transform', 'scale(0)');

        $.get(url, function (data) {                
        }).done(function () {

            offer_icon.addClass('animated').addClass('rubberBand');  

            setTimeout(function(){
                icon.css('transform', 'scale(1)');
                icon.removeClass('far fa-check-circle').addClass('fa-plus');
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
                icon.removeClass('fa-plus').addClass('far fa-check-circle')
            }
        });
    }

    $box.click(function () {

        var clicked = $(this).attr('clicked');

        if (clicked == 'false'){
            addItem($(this));
            $(this).attr('clicked','true')
        } else {
            removeItem($(this));
            $(this).attr('clicked','false')
        }

    })

    showItems();
});