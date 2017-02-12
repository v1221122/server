<?php
    session_start();
?>
<!DOCTYPE html>
<html>
<head>
    <title>VirtLabGraph</title>
    <link rel="stylesheet" href="style.css">
    <script src="js/jquery.js"></script>
    <script src="js/hide.js"></script>
</head>
<body>
    <div class="header">
        <div class="logo">
            <img src="" alt="logo">
        </div>
        <div class="registration">
            <?php
                require_once "php/login.php";
            ?>
            <dialog id="registration_dialog">
                <form method="post">
                    <img src="close.jpg" alt="close" id="dialog_close"/>
                    <label for="reg_login" class="dialog_label">Логин</label>
                    <input type="text" name="reg_login" class="dialog_input"/>
                    <label for="reg_password" class="dialog_label">Пароль</label>
                    <input type="password" name="reg_password" class="dialog_input"/>
                    <input type=submit value="Регистрация" class="dialog_button"/>
                    <?php
                        require_once "php/registration.php";
                    ?>
                </form>
            </dialog>
            <button id="open_dialog" >Зарегистрироваться</button>
        </div>
        <h1>header</h1>
        <script>
            var dialog = document.querySelector('#registration_dialog');
            document.querySelector('#open_dialog').onclick = function(){
                dialog.showModal();
            }
            document.querySelector('#dialog_close').onclick = function(){
                dialog.close();
            }
        </script>
    </div>
    <div class="left_panel">
        <h1>nav</h1>
        <ul class="main_menu">
            <li><a href="#?section=sm" id="s1">sm</a><br>
                <ul id="hide1" class="hidden">
                    <li>1</li>
                </ul>
            </li>
            <li><a href="#?section=inc">inc</a></li>
        </ul>
    </div>
    <div class="main_area">
        <iframe src="main.php" class="frame">
        </iframe>
    </div>
    <div class="footer">
        <h1>footer</h1>
    </div>
</body>
</html>
