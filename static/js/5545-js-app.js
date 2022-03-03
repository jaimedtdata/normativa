var $jq = jQuery.noConflict();
$jq(function(){

    $jq('a.gOpenMenu').click(function(){
        $jq('.gMenuPrincipal').fadeToggle();
    });
        
    gHeightBodyFunction();
    gTabWrapperHeight();

    $jq(window).resize(function(){
        gHeightBodyFunction();
        gTabWrapperHeight();
    });

	//gTab
    $jq('.gTabBusqueda a').click(function(){
        var option = $jq(this).attr('id');
 
        $jq('.gTabBusqueda a').removeClass('active');
        $jq(this).addClass('active');

        $jq('.gTabContent').hide();
        $jq('.gTabContent').removeClass('gActive');
        $jq('#'+option+'-content').addClass('gActive');
        $jq('#'+option+'-content').fadeIn();
        
        gTabWrapperHeight();

        $jq('#panResultado').hide();
        
    });

    //gOpcionBuscar
    $jq('a.gSubArea1').click(function(){
        $jq('a.gSubArea1 h5,a.gSubArea1 h4').removeClass('gFondoCircleGris');
        $jq(this).children('h5').addClass('gFondoCircleGris');
        $jq(this).children('h4').addClass('gFondoCircleGris');
    });
    
    $jq('a.gSubArea2').click(function(){
        $jq('a.gSubArea2 h5,a.gSubArea2 h4').removeClass('gFondoCircleNaranja');
        $jq(this).children('h5').addClass('gFondoCircleNaranja');
        $jq(this).children('h4').addClass('gFondoCircleNaranja');
    });
    
    $jq('a.gSubArea3').click(function(){
        $jq('a.gSubArea3 h5,a.gSubArea3 h4').removeClass('gFondoCircleAmarilo');
        $jq(this).children('h5').addClass('gFondoCircleAmarilo');
        $jq(this).children('h4').addClass('gFondoCircleAmarilo');
    });
    
    $jq('a.gSubArea4').click(function(){
        $jq('a.gSubArea4 h5,a.gSubArea4 h4').removeClass('gFondoCircleRojo');
        $jq(this).children('h5').addClass('gFondoCircleRojo');
        $jq(this).children('h4').addClass('gFondoCircleRojo');
    });
    
    $jq('a.gSubArea5').click(function(){
        $jq('a.gSubArea5 h5,a.gSubArea5 h4').removeClass('gFondoCircleAmarilo2');
        $jq(this).children('h5').addClass('gFondoCircleAmarilo2');
        $jq(this).children('h4').addClass('gFondoCircleAmarilo2');
    });

    $jq('a.gAvanzadaClick').click(function(){
       $jq('.gAvanzada').slideToggle();
    });

    $jq('.gResultadosClick').click(function(){
    
        $jq('.gResultados').slideDown();
        $jq('html, body').animate({
            scrollTop: ($jq('.gResultados').offset().top)-20
        }, 800);
    });

    $jq('a.gSubArea').click(function(){
        var opcion = $jq(this).attr('id');
        document.getElementById('FormListado1:txtTextoBusqueda').setAttribute("placeholder",  $jq(this).children("h5").html()+"..."); //place holder
        
        $jq('a.gSubArea h5,a.gSubArea h4').removeClass('gColorBlanco');
        $jq('a.gSubArea h5,a.gSubArea h4').removeClass('gColorBlanco');
        $jq(this).children('h4,h5').addClass('gColorBlanco');
        $jq(this).children('h4,h5').addClass('gColorBlanco');       
    });

});

function gHeightBodyFunction(){
    var gHeightWindow = $jq(window).height();
    var gHeightBody = $jq('.gContenido').height();
    var gHeightCalc = gHeightWindow-$jq('.gHeader').height()-$jq('.gFooter').height()-60;

    if(gHeightBody < gHeightWindow){
        $jq('.gContenido').attr('style','min-height:'+gHeightCalc+'px;');
    }
}

function submitByEnter(e) {
     if (e.keyCode == 13) { 
         document.getElementById("FormListado1:b_RealizaBusqueda").click();
         return false; 
     }else{ 
         return true; 
     } 
 }
 
function gTabWrapperHeight(){
    $gHeight = $jq('.gWrapperTab').children('.gActive').height();
    $jq('.gWrapperTab').height($gHeight);
}
