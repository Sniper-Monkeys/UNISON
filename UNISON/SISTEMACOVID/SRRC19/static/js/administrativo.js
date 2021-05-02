$(document).ready(function (){
   $('.secciones .info').hide();
   $('.secciones .info:first').show();

  $('ul.tabs li a').click(function(){

      $('.secciones .info').hide();
      var activeTab = $(this).attr('href');
      $(activeTab).show();
      return false;

  });

});
