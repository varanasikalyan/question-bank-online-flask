jQuery(document).ready(function(){
    var x1 = 1;
    var y1 = 2;
    var x2 = 1;
    var y2 = 9;
    var imageUrl  = "../static/images/welcome/welcome" + Math.floor(Math.random() * ((y1-x1)+1) + x1) + "_" + Math.floor(Math.random() * ((y2-x2)+1) + x2) + ".jpg";
    $("#splashScreen").css('background-image', 'url(' + imageUrl + ')');
});