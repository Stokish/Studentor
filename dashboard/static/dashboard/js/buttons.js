$(document).ready(function(){
    var t = false;
    if( $('.dash_card').length <= 6){
        $('#more').hide()
    }

    $('#more').click( function () {
        var x = $('.dash_card:gt(0)').css('display');

        if(t === false) {

            $('.dash_card:gt(5)').animate({
                opacity: 1
            },200, function(){
                $(".dash_card:gt(5)").css({display: x});
            });
            t = true;
            if($('#more').attr("data") == "направления") {
                $('#more').text("Показать меньше направлений");
            }
            else {
                $('#more').text("Показать меньше курсов");
            }
        }
        else {

            $(".dash_card:gt(5)").animate({
                opacity: 0
            }, 400, function(){
                $(".dash_card:gt(5)").hide();
            });
            t = false;

            if($('#more').attr("data") == "направления") {
                $('#more').text("Показать больше направлений");
            }
            else {
                $('#more').text("Показать больше курсов");
            }

        }

    });
});
