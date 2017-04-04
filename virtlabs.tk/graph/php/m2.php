<?php
function parse(){
    require("get_matrix.php");
    $m_inc = "";
    str_replace('<br>', '', $str);
    $arr = str_word_count($str, 1);
    return $arr;
}
    $arr = parse();
    foreach($arr as $a)
        echo $a;
?>
