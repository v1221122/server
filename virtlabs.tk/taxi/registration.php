<?php
    $title = "Такси форсаж";
    $dbname = "alex";
    $url = "index.php";
?>

<!DOCTYPE html>
<html>
<head>
<?php
    echo "<title>Registration in $title</title>"
?>
</head>
<body>
    <form method="post">
        <label for="login">Login</label>
        <input type="text" name="login" placeholder="login"/><br>
        <label for="password">Password</label>
        <input type="password" name="password" placeholder="password"/><br>
        <input type="submit" value="Register">
    </form>

<?php
    $link = mysqli_connect("localhost", "nerrevar", "01050062", "$dbname");
    if (isset($_POST['login']) and isset($_POST['password'])){
        if (empty($_POST['login']))
            echo "You don't input login";
        elseif (empty($_POST['password']))
            echo "You don't input password";
        else{
            $login = $_POST['login'];
            $password = $_POST['password'];
            $check_query = mysqli_query($link, "select * from user where user='$login'");
            if (mysqli_fetch_array($check_query)){
                echo "User with this login is already exist. Please try again";
                $_POST=array();
            }
            else{
                $query = mysqli_query($link, "insert into user (user, password) values 
                        ('$login', '$password')");
                echo "Registration seccesful!";
                echo '<meta http-equiv="refresh" content="5,'.$url.'">';
            }
        }
    }
    else
        echo "Not all fields inputed";

    mysqli_close($link);
?>

</body>
</html>
