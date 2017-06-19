<?php
	$point_num = $_GET['point_num'];
	
	require "connection.php";
	
	$result = mysqli_query($link, "select * from ".$_GET['id']."_line where p1=$point_num");
	while ($r = mysqli_fetch_array($result))
		echo $r['id']." ";
?>