    
 $(window).load(function () {
     var table = $('#example').DataTable({
         "scrollX": true,
         "language": {
             "lengthMenu": "প্রত্যেক পেজ এ _MENU_ টি তথ্য দেখাবে",
             "zeroRecords": "কিছুই পাই নাই , দুঃখিত ",
             "info": "সকল পেজ এ তথ্য দেখাবে",
             "infoEmpty": "আর তথ্য নেই",
             "infoFiltered": "(filtered from _MAX_ total records)",
             "search": "অনুসন্ধান:",
             "paginate": {
                 "first": "প্রথম",
                 "last": "শেষ",
                 "next": "পরবর্তী",
                 "previous": "পূর্বে"
             },
         },

     });

     /*$('#example tbody')
     .on( 'mouseenter', 'td', function () {
         var colIdx = table.cell(this).index().column;

         $( table.cells().nodes() ).removeClass( 'highlight' );
         $( table.column( colIdx ).nodes() ).addClass( 'highlight' );
     } ); */

     all_date_fileds = document.querySelectorAll('.vDateField');
     all_date_fileds.forEach(function(dateItem) {
         dateItem.parentNode.classList.add("input-group");
       });


 });

 /* add swiper slide  */
//  var swiper = new Swiper('swiper_1', {
//      spaceBetween: 30,
//      centeredSlides: true,
//      autoplay: {
//          delay: 10000,
//          disableOnInteraction: false,
//      },
//      pagination: {
//          el: '.swiper-pagination',
//          clickable: true,
//      },
//      navigation: {
//          nextEl: '.swiper-button-next',
//          prevEl: '.swiper-button-prev',
//      },
//  });


 /* vertical loop */
 /* $('.org-info1').verticalLoop({
     delay: 2000,
     order: 'asc'
 }); */

 //setTimeout(function () {
 //$('.org-info1').verticalLoop('autoPause');
 ///}, 10 * 1000);


 var verticalLoop = new VerticalLoop('.org-info2', {
     delay: 3000,
     order: 'desc',
     oninitend: function (res) {
         //console.log(res);
     }
 });


 

