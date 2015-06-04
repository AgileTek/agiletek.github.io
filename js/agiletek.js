/**
 * Created by stevenrossiter on 03/06/2015.
 */

$(function(){

    $("#overview").click(function(){
        Reveal.toggleOverview();
    });
    Reveal.addEventListener( 'slidechanged', function( event ) {
        $('.nav-link').css("background-color", "");
    $("#h-"+event.indexh).css("background-color", "rgba(255,255,255,0.3)");
} );
});