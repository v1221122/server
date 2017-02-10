<?php
if (isset($_POST['point'])){
    if (!isset($_POST['index']))
        $_POST['index'] = 1;
    else
        $_POST['index'] = $_POST['index'] + 1;
    echo '
    <img src="" alt="point" id="'.$_POST['index'].'">
    ';
}
?>
