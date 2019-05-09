<!DOCTYPE html>
<head>
</head>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js">
// scripti indirdim</script>


<script>/*
$(document).ready(function(){
    $("#container").hover(function(){
	   alert("kutu açıldı");
	   });
});*/
$(document).ready(function(){
  $("#container").mouseenter(function(){
  $("getir").hide();});
 $("#container").mouseleave(function(){
  $("getir").show();});
 $("#getir").click(function(){
	 $("#container").slideDown("fast");
 });
  $("#getir").click(function(){
	 $("#container").animate({opacity:"0.1"});
 })
})
</script>
<style>
#container{
    width:200px;
	height:200px;
	background-color:red;
	}
</style>
<body>

<div id="container">
</div>
<button id="getir"></button>

</body>
</html>