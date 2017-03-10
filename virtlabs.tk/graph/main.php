<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="style_main.css">
    <script src="js/jquery.js"></script>
    <script src="js/svg.js"></script>
    <script src="js/paint.js"></script>
    <?php require_once "svg/icons.svg";
        $_SESSION['id'] = $_GET['id'];
    ?>
</head>
<body>
    <div class="wrapper">
        <div id="toolbar">
            <svg class="toolbar_icon" height="64px" width="64px" onClick="paint_point()">
                <use xlink:href="#icon_point_button"></use>
            </svg>
            <svg class="toolbar_icon" height="64px" width="64px" onClick="paint_line()">
                <use xlink:href="#icon_line_button"></use>
            </svg>
            <svg class="toolbar_icon" height="64px" width="64px" onClick="replace()">
                <use xlink:href="#icon_replace_button"></use>
            </svg>
        </div>
        <svg id="svg" xmlns="http://www.w3.org/2000/svg" version="1.1">
        </svg>
        <div id="console">
            <textarea disabled=true id="console_text">hello</textarea>
        </div>
    </div>
    <div class="frames">
        <h1>matrix frames</h1>
    </div>
    <div id="check_div">
        <form method="post" id="check_form">
            <input type="hidden" name="coordinats" id="coordinats">
            <input type="submit" value="Проверить" id="check_button">
        </form>
        <?php
            require_once "php/check.php";
        ?>
    </div>
</body>
</html>
