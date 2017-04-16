<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="style_main.css">
    <script src="js/jquery.js"></script>
    <script src="js/svg.js"></script>
    <script src="js/paint.js"></script>
	<script src="js/check.js"></script>
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
        <div id="m1" class="matrix">
			<div class="matrix_head">
				Матрица смежности
			</div>
			<div class="matrix_main">
				<?php require_once "php/m1.php" ?>
			</div>
		</div>
		<div id="m2" class="matrix">
			<div class="matrix_head">
				Матрица инцидентности
			</div>
			<div class="matrix_main">
				<?php require_once "php/m2.php" ?>
			</div>
		</div>
    </div>
    <div id="check_div">
		<button id="check_button" onClick="check()">Проверить</button>
    </div>
</body>
</html>
