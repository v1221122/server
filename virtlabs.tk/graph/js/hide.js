$(document).ready(function(){
    $(".hidden").hide();
	
	$(".section").each(function(){
		$(this).click(function(){
			$(this).find(".hidden").slideToggle();
		});
    });
	
	$("#hide_button").click(function(){
		$("#left_panel").setAttribute("width", "30px");
		
	});
});