<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="style_main.css">
    <script src="jquery.js></script>
    <script src="paint.js"></script>
</head>
<body>
    <div class="toolbar">
        <h1>Toolbar</h1>
    </div>
    <div class="main" id="main">
        <form method="post">
            <input type="hidden" name="point"/>
            <input type="submit" value=""><img src='' alt='point'/></input>
        </form>
        <?php
            require "point.php";
        ?>
        <h1>Main</h1>
    </div>
    <div class="console">
        <h1>console</h1>
    </div>
</body>
</html>
