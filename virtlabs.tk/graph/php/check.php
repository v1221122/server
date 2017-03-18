<?php
	$id = $_GET['id'];
	$task = 1;
	if (!isset($db))
		$db = mysqli_connect("localhost", "nerrevar", "01050062", "graph");
	
	$select_query_point = "select * from ".$id;
	$user_point_num = 0;
	$arr_point = mysql_query($select_query_point);
	while ($x = mysqli_fetch_array($db, $arr_point)
		$point_num++;
	
	$select_query_line = "select * from ".$id."_line";
	$arr_line_temp = mysqli_query($select_query_line);
	while ($a = mysqli_fetch_array($arr_line_temp))
		$user_arr_line[$a['id']] = array($a['p1'], $a['p2']);
	
	//получение исходной матрицы
	$source_point_num = 0;
	$matrix = array();
	$temp_arr = mysqli_query($db, "select * from points where task_id=".$task." and i=0");
	while ($t = mysqli_fetch_array($temp_arr)
		$source_point_num++;
	if ($user_point_num != $source_point_num){//при неправильном количестве вершин
		echo "point_num_err";
		break;
	}
	for ($i = 0; $i < $source_point_num; $i++){
		$matrix_temp = mysqli_query("select * from points where task_id=".$task." and i=".$i." order by j");
		while ($j = mysqli_fetch_array($matrix_temp)
			$temp_i[] = $j['value'];
		$matrix[] = $temp_i;
	}
	
	
	
	$f = fopen("source_matrix.txt", "w");
	foreach ($matrix as $m){
		foreach ($m as $v)
			fputs($f, $v." ");
		fputs("\n");
	}
	fclose($f);	
?>