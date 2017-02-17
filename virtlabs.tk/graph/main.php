<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="style_main.css">
    <script src="js/jquery.js"></script>
    <script src="js/paint.js"></script>
</head>
<body>
    <div class="wrapper">
        <div id="toolbar">
            <button class="toolbar_button" onClick="paint_point()"><img src="img/point.png" alt="point"/></button>
            <button class="toolbar_button" onClick="paint_line()"><img src="img/line.png" alt="line"/></button>
        </div>
        <div id="main">
            <svg id="svg">
            </svg>
        </div>
        <div id="console">
            <textarea disabled=true id="console_text">hello</textarea>
        </div>
    </div>
    <div class="frames">
        <h1>matrix frames</h1>
    </div>
</body>
</html>
