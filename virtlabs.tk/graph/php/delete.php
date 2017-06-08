<?php
	$point_num = $_GET['point_num'];
	echo $point_num;
	
	require "connection.php";
	
	$r = mysqli_query($link, "select * from ".$_GET['id']);
	
	while ($result = mysqli_fetch_array($r))
		echo $result['point_index']."\n";
	
	echo "\n\n\n";
	
	mysqli_query($link, "delete from ".$_GET['id']." where point_index=$point_num");
	
	$r = mysqli_query($link, "select * from ".$_GET['id']);
	
	while ($result = mysqli_fetch_array($r))
		echo $result['point_index']."\n";
?>