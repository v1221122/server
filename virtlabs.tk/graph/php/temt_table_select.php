<?php
    $id = $_GET['id'];
    if (!isset($db))
        $db = mysqli_connect("localhost", "nerrevar", "01050062", "graph");
	$select_query = "select * from ".$id;
	$t_arr = mysqli_query($db, $select_query);
	if ($arr = mysqli_fetch_array($t_arr))
		echo "true";
	else
		echo "false";
?>