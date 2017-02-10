<?php
    $dbname = "alex";
    $url = "index.php";
//login check
    $link = mysqli_connect("localhost", "nerrevar", "01050062", "$dbname");
    if (isset($_POST['login']))
        if (!empty($_POST['login'])){
            $query = mysqli_query($link, "select * from user where user='".$_POST['login']."'");
            $user = mysqli_fetch_array($query);
            if (!empty($user['password'])){
                if ($_POST['password'] == $user['password']){
                    $_SESSION['id'] = session_id();
                    $_SESSION['login'] = $_POST['login'];
                }
            }
            else
                echo "wrong login or password!";
        }
?>

<?php   //adding login form
    if (empty($_SESSION["id"]) or empty($_SESSION["login"])){
        echo '<form method="post">';
        require_once "login_form.php";
        echo '</form>';
    }
    else{   //login succesful
        echo '<form method="post" style="float:right">';
        $name_query = mysqli_query($link, "select name from user where user = '".$_SESSION['login']."'");
        $name = mysqli_fetch_array($name_query);
        echo "Hello, ".$name['name']."!<br>";
        //logout form
        echo '<input type="hidden" name="logout" value="yes"/>';
        echo '<input type="submit" value="Log out"/><br>';
        //reg link
        if (mysqli_fetch_array(mysqli_query($link, "select * from user where user='".$_SESSION["login"]."'"))['admin'])
            echo '<a href="registration.php">Registration</a>';
        echo '</form>';
        require_once "change_status.php";//buttons
        require_once "table.php" ;//workers
        //status listeners
        if (isset($_POST['work'])){
            $query=mysqli_query($link, "update user set work=true where user='".$_SESSION['login']."'");
            require "refresh.php";
            unset($_POST['work']);
        }
        if (isset($_POST['not_work'])){
            $query=mysqli_query($link, "update user set work=false where user='".$_SESSION['login']."'");
            require "refresh.php";
            unset($_POST['not work']);
        }
    }
    //logout listener
    if (isset($_POST['logout'])){
        session_destroy();
        echo '<meta http-equiv="refresh" content="0,'.$url.'">';
    }
?>
