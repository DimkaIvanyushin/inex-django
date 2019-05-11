$(document).ready(function () {

    var $mainMenu = $('.main-menu');
    var menuOffsetTop = $mainMenu.offset().top;
    var check = false;

    var $section_slider = $('section.slider');
    var $slide = $('section.slider .carousel-item .item');

    function parallaxScroll() {
        var scrolled = $(window).scrollTop();
        $slide.css('background-position-y', (0 + (scrolled * .70)) + 'px');
    }

    function animateContactUs() {
        $("#button_contact_us").on("click", function (event) {
            event.preventDefault();
            var id = $(this).attr('href'),
                top = $(id).offset().top;
            $('body,html').animate({ scrollTop: top }, 1500);
        });
    }

    function mainMenu() {
        if ($(window).scrollTop() > menuOffsetTop) {
            if (!check) {

                if ($(document).width() > 670) {
                    $section_slider.css("margin-top", "83px");
                } else {
                    $section_slider.css("margin-top", "51px");
                }

                $mainMenu.addClass('fixed-top');

                $mainMenu.find('#navbarSupportedContent')
                    .find('ul')
                    .removeClass('hide')
                    .addClass('show')
                    .find('li.search')
                    .removeClass('ml-auto');

                $mainMenu.find('.logo-dt')
                    .removeClass('hide')
                    .addClass('show')

                check = true;
            }
        } else {
            if (check) {
                $section_slider.css("margin-top", "0");
                $mainMenu.removeClass('fixed-top');

                $mainMenu.find('#navbarSupportedContent')
                    .find('ul')
                    .removeClass('show')
                    .addClass('hide')
                    .find('li.search')
                    .addClass('ml-auto');

                $mainMenu.find('.logo-dt')
                    .removeClass('show')
                    .addClass('hide')

                check = false;
            }
        }
    }

    
    animateContactUs();
    mainMenu();
    $(window).bind('scroll', mainMenu);

    $('.carousel_recall').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        mobileFirst:true,
        autoplaySpeed: 5000,
        prevArrow: "<i class='fas fa-chevron-left prev slick-prev'></i>",
        nextArrow: "<i class='fas fa-chevron-right next slick-next'></i>",
        responsive: [
            {
              breakpoint: 768,
              settings: {
                slidesToShow: 3
              }
            }
          ]
    });
    // $(window).bind('scroll', parallaxScroll);
});
