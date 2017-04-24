<?php
	function parse(){
		require("get_matrix.php");
		$m_inc = "";
		$str = str_replace('<br>', ' ', $str);
		$str = str_replace(' ', '', $str);

		// echo getcwd();
		
		exec("python3 python/m2.py $str", $m_inc);

		return $m_inc;
	};

	$arr =  parse();
	foreach ($arr as $a){
		echo $a;
	};
?>
