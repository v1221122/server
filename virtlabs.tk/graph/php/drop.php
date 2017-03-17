<?php
	if (!isset($db))
		$db = mysqli_connect("localhost", "nerrevar", "01050062", "graph");
	$id = $_GET['id'];
	$query = "drop table if exists ".$id;
	$query_line = "drop table if exists ".$id."_line";
	mysqli_query($db, $query);
	mysqli_query($db, $query_line);
?>