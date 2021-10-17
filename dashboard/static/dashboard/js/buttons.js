$(document).ready(function(){
    var t = false;
    $('#more').click( function () {
        var x = $('.dash_card:gt(0)').css('display');
        if(t === false) {

            $('.dash_card:gt(5)').animate({
                opacity: 1
            },500, function(){
                $(".dash_card:gt(5)").css({display: x});
            });
            t = true;
            $('#more').text("Показать меньше направлений");
        }
        else {

            $(".dash_card:gt(5)").animate({
                opacity: 0
            }, 500, function(){
                $(".dash_card:gt(5)").hide();
            });
            t = false;
            $('#more').text("Показать больше направлений");
        }

    });
});
