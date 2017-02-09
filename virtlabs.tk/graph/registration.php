<?php
    $db = mysqli_connect("localhost", "nerrevar", "01050062", "virtlabs");
    if (isset($_POST['reg_login']) and isset($_POST['reg_password'])){
        if (empty($_POST['reg_login']))
            echo "Не введен логин";
        elseif (empty($_POST['reg_password']))
            echo "Не введен пароль";
        else{
            $login = $_POST['reg_login'];
            $password = $_POST['reg_password'];
            $check_query = mysqli_query($link, "select * from user where login='$login'");
            if (mysqli_fetch_array($check_query)){
                echo "Пользователь с таким логином уже существует. Пожалуйста попробуйте еще раз";
                $_POST=array();
            }
            else{
                $query = mysqli_query($link, "insert into user values (null,'$login', '$password')");
                echo "Регистрация успешна!";
            }
        }
    }
    else
        echo "Заполнены не все поля";

    mysqli_close($db);
?>
