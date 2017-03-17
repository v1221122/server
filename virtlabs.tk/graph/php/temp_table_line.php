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
	
	$f = fopen("t_table", "w");
	$arr = mysqli_query($db, "select * from ".$id."_line");
	fputs($f, $p1." ".$p2."\n");
	while ($a1 = mysqli_fetch_array($arr))
		foreach ($a1 as $a)
			fputs($f, $a."\n");
	fclose($f);
?>