<?php
	$id = $_GET['id'];
	$p1 = $_GET['p1'];
	$p2 = $_GET['p2'];
	if (!isset($db))
		$db = mysqli_connect("localhost", "nerrevar", "01050062", "graph");
	$create_query = "create table if not exists ".$id."_line(id int not null auto_increment, p1 int not null, p2 int not null, primary key(id))";
	mysqli_query($db, $create_query);
	$insert_query = "insert into ".$id."_line values(null, ".$p1.", ".$p2.")";
	mysqli_query($db, $insert_query);
?>