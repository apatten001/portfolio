jQuery(function ($) {

    'use strict';

    // --------------------------------------------------------------------
    // PreLoader
    // --------------------------------------------------------------------

    (function () {
        $('#preloader').delay(200).fadeOut('slow');
    }());

$('.footer').hide()


 $(document).ready(function() {
      $('.progress .progress-bar').css("width",
                function() {
                    return $(this).attr("aria-valuenow") + "%";
                }
        )
    });

$( document ).hover(function() {
  $( ".social-icon" ).toggle( "bounce", { times: 3 }, "slow" );
});

}); // JQuery end