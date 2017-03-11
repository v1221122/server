<?php
    $id = $_GET['id'];
    $index = $_GET['point_index'];
    $x = $_GET['x'];
    $y = $_GET['y'];
    if (!isset($db))
        $db = mysqli_connect("localhost", "nerrevar", "01050062", "graph");
    $query = "create temporary table if not exists ".$id."(id int not null auto_increment,point_index int(2) not null,x int(4) not null,y int(4) not null, primary key(id))";
    mysqli_query($db, $query);
    $insert_query = "insert into ".$id." values(null,".$index.", ".$x.", ".$y.")";
    mysqli_query($db, $insert_query);
?>
