function check(){
	var request = new XMLHttpRequest();
	request.open("GET", "php/check.php?id=" + parse());
	request.send();
};