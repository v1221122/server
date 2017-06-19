<?php
	require "connection.php";
	
	$result = mysqli_query($link, "select * from ".$_GET['id']." order by point_index");
	
	$point_num = 1;
	if ($result)
		while ($r = mysqli_fetch_array($result)){
			if ($r['point_index'] == $point_num)
				$point_num++.'';
			else
				break;
		}
	echo $point_num;
?>