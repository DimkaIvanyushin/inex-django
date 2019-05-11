$(document).ready(function () {
    $('.carousel').slick({
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
});