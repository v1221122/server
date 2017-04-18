<?php
	$task = $_GET['task'];
	if (!isset($db))
		$db = mysqli_connect("localhost", "nerrevar", "01050062", "graph");
	
	$point_num = 0;
	$arr_point = mysqli_query($db, "select * from points where (task_id=".$task.") and (i=0)");
	while ($x = mysqli_fetch_array($arr_point))
		$point_num++;
	
	$s_arr = mysqli_query($db, "select * from points where task_id=".$task." order by i,j");
	$i = 0;
	$str = "";
	while ($arr = mysqli_fetch_array($s_arr)){
		$str = $str.$arr['value']." ";
		$i++;
		if ($i == $point_num){
			$str = $str."<br>";
			$i = 0;
		}
	}
	mysqli_close($db);
	return $str;
?>