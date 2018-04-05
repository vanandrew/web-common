// fade-in page
$(document).ready(function(){$(".pagefade").css({"filter":"brightness(1)","-webkit-filter":"brightness(1)"});});
// fade-out page
$(".nav-link").click(function(event){event.preventDefault();$(".pagefade").css({"filter":"brightness(0)","-webkit-filter":"brightness(0)"});setTimeout(function() { window.location.href = event.target.href; },1100);});
