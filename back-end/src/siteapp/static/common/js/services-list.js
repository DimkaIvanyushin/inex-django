$(document).ready(function () {

    var $breadcrumbs = $('section.breadcrumbs');

    var $navbar = $('.navbar');

    $navbar.addClass('fixed-top').find('.logo-dt').addClass('show')
    $navbar.addClass('fixed-top').find('.navbar-nav').addClass('show')


    $(window).bind('scroll', function (e) {
        parallaxScroll();
    });

    function parallaxScroll() {
        var scrolled = $(window).scrollTop();
        $breadcrumbs.css('background-position-y', (0 + (scrolled * .70)) + 'px');
    }
});