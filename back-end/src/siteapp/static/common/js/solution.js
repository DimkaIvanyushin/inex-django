$(document).ready(function () {
    $('.carousel').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        mobileFirst:true,
        autoplaySpeed: 2000,
        prevArrow: "<i class='fas fa-chevron-left prev slick-prev'></i>",
        nextArrow: "<i class='fas fa-chevron-right next slick-next'></i>",
        responsive: [
            {
                breakpoint: 600,
                settings: {
                    settings: "unslick"
                }
            }
        ]
    });
});