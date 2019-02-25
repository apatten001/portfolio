jQuery(function ($) {

    'use strict';

    // --------------------------------------------------------------------
    // PreLoader
    // --------------------------------------------------------------------

    (function () {
        $('#preloader').delay(200).fadeOut('slow');
    }());


 $(document).ready(function() {
      $('.progress .progress-bar').css("width",
                function() {
                    return $(this).attr("aria-valuenow") + "%";
                }
        )
    });
      $("h1").click(function(){
    $("#icon").animate({left: '250px'});
  });
}); // JQuery end