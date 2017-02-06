<?php
    $link = mysqli_connect("localhost", "nerrevar", "01050062", "ws");
    if (empty($_SESSION['id']) or empty($_SESSION['login'])){
        echo '<form action="maket.php" method="post">';
        echo '<label for="login">Login</label>';
        echo '<input type="text" name="login"/>';
        echo '<label for="password">Password</label>';
        echo '<input type="password" name="password"/>';
        echo '<input type="submit" value="Log in"/>';
        echo '</form>';
    }//10
    else
        echo "Hello".$_SESSION['login'];
?>
