<?php
    if (session_start())
        echo "session started";
?>
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width">
    <link rel="stylesheet" href="m_style.css">
    <title>Title</title>
</head>
<body>
    <div class="header">
        <div class="logo">
            <img src="logo.jpg" alt="logo">
        </div>
        <div class="div-h1">
            <h1>Title<br>of site</h1>
        </div>
        <div class="reg">
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
    }
    else
        echo "Hello".$_SESSION['login'];
    echo "Hello".$_SESSION['login'];
    echo "Hello".$_SESSION['id'];

?>
        </div>
    </div>
    <div class="main">
        <div class="sidebar">
            <ul>
                <li><a href="#">link1</a></li>
                <li><a href="#">link2</a></li>
            </ul>
        </div>
        <div class="banner">
            <img src="banner.jpg" alt="banner">
        </div>
        <div class="main_area">
            <div class="main_img">
                <img src="main_img1.jpg" alt="main_img1">
            </div>
            <p>main</p>
        </div>
    </div>
    <div class="footer">
        <a hfer="#">Copyrite</a>
    </div>
</body>
</html>
