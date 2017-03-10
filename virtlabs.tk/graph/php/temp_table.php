<?php
    $f = fopen('t_table', 'a+');
    $id = $_GET['id'];
    $index = $_GET['point_index'];
    $x = $_GET['x'];
    $y = $_GET['y'];
    if (!isset($db))
        $db = mysqli_connect("localhost", "nerrevar", "01050062", "graph");
    if $query = "create temporary table if not exists ".$id."(id int not null auto_increment,point_index int(2) not null,x int(4) not null,y int(4) not null, primary key(id))"
        fputs($f, "created");
    if $insert_query = "insert into ".$id." values(null,".$index.", ".$x.", ".$y.")"
        fputs($f, "inserted");
    if $arr = mysqli_fetch_array(mysqli_query($db, "select * from ".$id))
        fputs($f, "selected");
    while ($arr){
        $arr = mysqli_fetch_array(mysqli_query($db, "select * from ".$id));
        $str = $arr['point_index']." ".$arr['x']." ".$arr['y']."\n";
        fputs($f, $str);
    }
    fclose($f);
?>
