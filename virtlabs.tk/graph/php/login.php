<?php
    $dbname = "virtlabs";
    $url = "index.php";
	
    if (empty($_SESSION["id"]) or empty($_SESSION["login"])){
        echo '<form method="post">';
        echo '<label for="login">Логин</label>';
        echo '<input type="text" name="login"/>';
        echo '<label for="password">Пароль</label>';
        echo '<input type="password" name="password"/>';
        echo '<input type="submit" value="Войти"/>';
        echo '</form>';
    }
    else{
        echo "Hello ".$_SESSION['login']."!";
        echo '<form method="post"/>';
        echo '<input type="hidden" name="logout" value="yes"/>';
        echo '<input type="submit" value="Выйти"/>';
        echo '</form>';
    }
	
	if (isset($SESSION['f']))
		if ($SESSION['f'])
            echo "Введен неверный логин или пароль!";
	$SESSION['f'] = false;

    if (isset($_POST['logout'])){
        session_destroy();
        echo '<meta http-equiv="refresh" content="0,'. $url.'">';
    }

    $link = mysqli_connect("localhost", "nerrevar", "01050062", "$dbname");
    if (isset($_POST['login']))
        if (!empty($_POST['login'])){
			$login = htmlentities(mysqli_escape_string($link, $_POST['login']));
            $query = mysqli_query($link, "select * from user where login='".$login."'");
            $user = mysqli_fetch_array($query);
            if (!empty($user['password'])){
                if ($_POST['password'] == $user['password']){
                    $_SESSION['id'] = session_id();
                    $_SESSION['login'] = $_POST['login'];
                }
            }
            else
				$SESSION['f'] = true;
        }
?>
