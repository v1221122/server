<?php
$db = mysqli_connect("localhost", "nerrevar", "01050062", "alex");
$query = mysqli_query($db, "select id,name,car,work from user where work=1");
$row = mysqli_fetch_array($query);
echo '<table style="border: 2px solid black; width:100%">';
while ($row){
    echo '<tr><td style="border: 2px solid black">';
    echo $row["id"];
    echo '</td><td style="border: 2px solid black">';
    echo $row['name'];
    echo '</td><td style="border: 2px solid black">';
    echo $row['car'];
    echo '</td></tr>';
    $row = mysqli_fetch_array($query);
}
echo '</table>';
?>
