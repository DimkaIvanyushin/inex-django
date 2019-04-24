$(document).ready(function () {

    var $mainMenu = $('.main-menu');
    var menuOffsetTop = $mainMenu.offset().top;
    var check = false;

    var $section_slider = $('section.slider');
    var $slide = $('section.slider .carousel-item .item');

    function parallaxScroll() {
        var scrolled = $(window).scrollTop();
        $slide.css('background-position-y', (0 + (scrolled * .50)) + 'px');
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

                $section_slider.css("top", "77px");
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
                $section_slider.css("top", "0");
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

    var $search_container = $('.search-container .resoult');

    $("#search-input").autocomplete({
        source: function (request, response) {
            $.ajax({
                url: "/api/search/all",
                dataType: "json",
                data: {
                    search_query: request.term
                },
                success: function (data) {
                    data.forEach( function(element) {

                        // console.log(element);
                    });
                }
            });
        }
    });

    animateContactUs();
    $(window).bind('scroll', mainMenu);
    // $(window).bind('scroll', parallaxScroll);
});

/* <div class="box-resoult">
    <img src="http://localhost:8080/media/images/solutions/ant-rozetsky-272965-unsplash_vDzNOU4.jpg.255x300_q85_crop-center.jpg "  class="mr-3 mt-1" width="50px" height="50px" alt="#">
    <div>
        <a class="title" href="#">Контроллер для средних сетей автоматизации ULC-03</a>
        <a class="category" href="#">Контроллеры</a>
    </div>
</div> */