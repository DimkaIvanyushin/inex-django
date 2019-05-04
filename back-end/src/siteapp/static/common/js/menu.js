var flag = false;
var $button_search = $('span.nav-item.search i');
var $input = $("#search-input");
var $search_container = $('.search-container .resoult');

$button_search.click(function () {

    if (!flag) {
        //$(this).removeClass('fa-search').addClass('fa-circle-notch fa-spin');
        $(this).css('transform', 'scale(0)');

        setTimeout(function () {
            $button_search.addClass('fa-times');
            $button_search.css('transform', 'scale(1)');
        }, 300);

        $('input#search-input').css('right', '0');
        flag = !flag;
    } else {
        $('.box-resoult').remove();
        $search_container.removeClass('visible');
        $input.val('');

        $button_search.css('transform', 'scale(0)');

        setTimeout(function () {
            $button_search.removeClass('fa-times');
            $button_search.css('transform', 'scale(1)');
        }, 300);

        $('input#search-input').css('right', '-100%');
        flag = !flag;
    }
});

$input.autocomplete({
    source: function (request, response) {

        if ($input.val().length > 2) {
            $.ajax({
                url: "/api/search/all",
                dataType: "json",
                data: {
                    search_query: request.term
                },
                success: function (data) {

                    $('.box-resoult').remove();

                    $search_container.addClass('visible');
                    $search_container.css('top', 0);

                    if (data.length == 0) {
                        var $box = $("<div>").addClass('box-resoult');
                        $box.append('<span class="ml-2">Продукция не найдена.</span>');

                        $search_container.prepend($box);

                    } else {
                        data.forEach(function (element) {
                            var $box = $("<div>").addClass('box-resoult');
                            $box.append('<img src="' + element.image + '"  class="rounded-circle mr-2" width="50px" height="50px" alt="' + element.title + '">');

                            var $div = $("<div>")
                            $div.append('<a class="title" href="' + element.title_href + '">' + element.title + '</a>');
                            $div.append('<a class="category" href="' + element.category_href + '">' + element.category + '</a>');

                            $box.append($div)
                            $search_container.prepend($box);
                        });
                    }
                    $box = $("<div>").addClass('box-resoult');
                    $box.append('<a class="ml-2 small text-muted " href="/search/show"> Расширенный поиск </a>');
                    $search_container.append($box);

                }
            });
        } else {
            $search_container.removeClass('visible');
            $search_container.css('top', '-30px');
            $('.box-resoult').remove();
        }
    }
});

var line_content = $('.line_content');
var left_li = $('.mega-menu-container .left ul li.navigation a');

left_li.hover(function (e) {
    var pos_x = $(this).attr('in');
    left_li.removeClass('active');
    $(this).addClass('active');

    line_content.css('top', '-' + pos_x + 'px');
});

$('.left_icon_menu').click(function(){

    $(this).toggleClass('open');

    if($(this).hasClass('open')){
        $(this).find('i').removeClass('fa-bars').addClass('fa-times');
    } else {
        $(this).find('i').removeClass('fa-times').addClass('fa-bars');
    }

});


$('li.nav-item.mobile-dropdown a').click(function () {
    $(this).parent().find('.dropdown-menu-mobile').toggle();
});

$('.dropdown-menu-mobile .group-product').click(function () {
    $(this).find('.items').toggle();
    
});
