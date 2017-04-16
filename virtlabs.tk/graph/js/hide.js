$(document).ready(function(){
    $(".hidden").hide();
	
	$("#s1").click(function(){
        $("#hide1").slideToggle();
    });
	
	$("#hide_button").click(function(){
		$("#left_panel").setAttribute("width", "30px");
		
	});
});