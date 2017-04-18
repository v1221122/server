function check(){
	function parse_section(){
		var params = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
		var values = params[0].split('=');
		var value = values[2];
		return value;
	};
	
	function parse_task(){
		var params = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
		var values = params[0].split('=');
		var value = values[3];
		return value;
	};
	
	var request = new XMLHttpRequest();
	request.open("GET", "php/check.php?id=" + parse() + "&section=" + parse_section() + "&task=" + parse_task());
	request.send();
	request.onreadystatechange = function(){
		if (request.readyState == 4){
			alert(request.responseText);
		}
	};
};