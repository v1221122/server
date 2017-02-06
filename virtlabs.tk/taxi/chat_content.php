<?php
echo '
<form method="post" style="max-height=50px; margin-top:0px; min-height:50px">
    <input style="max-width:5em; min-width:5em; height:2em; float:right" 
type="submit" value="send">
    <input type="text" name="text">
</form>
';
$db = mysqli_connect("localhost", "nerrevar", "01050062", "alex");
$read_query = mysqli_query($db, "select user,date,text from user join 
message where message.send_id=user.id order by date desc limit 30"); 
$message = mysqli_fetch_array($read_query);
while ($message){
    echo $message['user']."   ".$message['date'].'<br>';
    echo $message['text'].'<br><br>';
    $message = mysqli_fetch_array($read_query);
}

if (isset($_POST['text']))
    if (!empty($_POST['text'])){
        $text = htmlentities(mysqli_real_escape_string($db, $_POST['text']));
        $write_query = mysqli_query($db, "insert into message (send_id,text) values((select id from user where user='".$_GET['user']."'),'$text' )");
        echo mysqli_error($db);
        unset($_POST['text']);
        echo '<meta http-equiv="refresh" content="0,chat_content.php">';
     }
?>
