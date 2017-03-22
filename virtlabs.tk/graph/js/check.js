function check(){
	var request = new XMLHttpRequest();
	request.open("GET", "php/check.php?id=" + parse());
	request.send();
	request.onreadystatechange = function(){
		if (request.readyState == 4){
			alert(request.responseText);
		}
	};
};