(function ($) {
    "use strict";

    $('.slick-inicio').slick({
        dots: true,
        infinite: true,
        autoplay: true,
        speed:2000,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        prevArrow:'<button class="arrow-slick-inicio prev-arrow-slick-inicio"><i class="zmdi zmdi-caret-left"></i></button>',
        nextArrow:'<button class="arrow-slick-inicio next-arrow-slick-inicio"><i class="zmdi zmdi-caret-right"></i></button>',
        dots: true,
    })


    $('.slick-empresas-asociadas').slick({
        dots: true,
        infinite: false,
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    })

})(jQuery)