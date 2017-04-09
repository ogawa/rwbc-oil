jQuery(function($) {
  "use strict";
	
	$(window).load(function(){
   		$("#sticky-menubar").sticky({ topSpacing: 0 });
	});
	
   /* ----------------------------------------------------------- */
   /*  Contact map 
   /* ----------------------------------------------------------- */
    var map;
        map = new GMaps({
          div: '#map',
          lat: 35.6041965,
          lng: 139.6838597,
          scrollwheel: true,
          panControl: true,
          zoomControl: true,
        });

        map.addMarker({
          lat: 35.6041965,
          lng: 139.6838597,
        });

   /* ----------------------------------------------------------- */
   /*  Scroll
   /* ----------------------------------------------------------- */
	$('a[href^=#]').click(function() {
      var speed = 500;
      var href= $(this).attr("href");
      var target = $(href == "#" || href == "" ? 'html' : href);
      var position = target.offset().top;
      $('body,html').animate({scrollTop:position}, speed, 'swing');
      return false;
   });

});



$(document).ready(function() {
    $("#news-slider").owlCarousel({
        items : 3,
        itemsDesktop:[1199,2],
        itemsDesktopSmall:[980,2],
        itemsMobile : [650,1],
        pagination:false,
        navigationText:false,
        autoPlay:true
    });
});
