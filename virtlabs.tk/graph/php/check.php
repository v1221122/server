<?php
	$id = $_GET['id'];
	echo $id;
	$task = 1;
	if (!isset($db))
		$db = mysqli_connect("localhost", "nerrevar", "01050062", "graph");
	
	$select_query_point = "select * from ".$id;
	$user_point_num = 0;
	$arr_point = mysqli_query($db, $select_query_point);
	while ($x = mysqli_fetch_array($arr_point))
		$point_num++;
	
	$select_query_line = "select * from ".$id."_line";
	$arr_line_temp = mysqli_query($select_query_line);
	while ($a = mysqli_fetch_array($arr_line_temp))
		$user_arr_line[$a['id']] = array($a['p1'], $a['p2']);
	
	require_once "get_matrix.php";
	
?>