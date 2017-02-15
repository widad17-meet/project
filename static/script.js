$('.carousel').carousel({
  interval: 6000,
  pause: "false"
});
$(document).ready(function(){       
   var scroll_start = 0;
   var startchange = $('.nav');
   var offset = startchange.offset();
   $(document).scroll(function() { 
      scroll_start = $(this).scrollTop();
      if(scroll_start > offset.top) {
          $('.nav').css('background-color', 'rgba(34,34,34,0.9)');
       } else {
          $('.nav').css('background-color', 'transparent');
       }
   });
});