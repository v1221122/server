<?php
	$id = $_GET['id'];
	$task = $_GET['task'];
	if (!isset($db))
		$db = mysqli_connect("localhost", "nerrevar", "01050062", "graph");

	$select_query_user_point = "select * from ".$id;
	$user_point_num = 0;
	$arr_user_point = mysqli_query($db, $select_query_user_point);
	while ($x = mysqli_fetch_array($arr_user_point))
		$user_point_num++;

	$select_query_user_line = "select * from ".$id."_line";
	$arr_user_line_temp = mysqli_query($db, $select_query_user_line);
    $str_user_line = '';
	while ($a = mysqli_fetch_array($arr_user_line_temp))
		$str_user_line = $str_user_line.$a['p1'].$a['p2'];

	$exec_str = "python ../convert_sm.py $user_point_num $str_user_line";
    exec($exec_str, $user_sm_arr, $err);

    $user_sm_str = '';
    foreach($user_sm_arr as $ar)
        $user_sm_str = $user_sm_str.$ar;

    echo $user_sm_str;

	require "get_matrix.php";

    if ($str == $user_sm_str)
        echo "\nsuccessful";
    else
        echo "\nepic fail";
?>
