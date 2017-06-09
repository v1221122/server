<?php
	$point_num = $_GET['point_num'];
	
	require "connection.php";
	
	mysqli_query($link, "delete from ".$_GET['id']." where point_index=$point_num");
	
	$result = mysqli_query($link, "select * from ".$_GET['id']."_line where p1=$point_num or p2=$point_num");
	while ($r = mysqli_fetch_array($result)){
		echo $r['id']." ";
		
	mysqli_query($link, "delete from ".$_GET['id']."_line where p1=$point_num or p2=$point_num");
	
	}
?>