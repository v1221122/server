<?php
    session_start();
?>
<!DOCTYPE html>
<html>
<head>
    <title>VirtLabGraph</title>
    <meta name="yandex-verification" content="3de45f2600675f37" />
	<meta charset="UTF-8">
    <link rel="stylesheet" href="style.css"/>
	<link rel="shortcut icon" href="img/icon.png" type="image/x-icon"/>
	<link href="https://fonts.googleapis.com/css?family=PT+Sans" rel="stylesheet">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="js/hide.js"></script>
	<?php
		require_once "svg/icons.svg";
		if (isset($_GET['task']) && isset($_GET['section'])){
			$section = $_GET['section'];
			$task = $_GET['task'];
		}
    ?>
</head>
<body>
    <div class="header">
        <div id="logo">
            <img src="img/logo.png" alt="logo">
        </div>
        <div class="registration">
            <?php
                require "php/login.php";
            ?>
            <dialog id="registration_dialog">
                <form method="post">
					<svg id="dialog_close">
						<use xlink:href="#icon_close"></use>
					</svg>
                    <label for="reg_login" class="dialog_label">Логин</label><br>
                    <input type="text" name="reg_login" class="dialog_input"/><br>
                    <label for="reg_password" class="dialog_label">Пароль</label><br>
                    <input type="password" name="reg_password" class="dialog_input"/><br>
                    <input type=submit value="Регистрация" class="dialog_button"/><br>
                    <?php
                        require "php/registration.php";
                    ?>
                </form>
            </dialog>
            <button id="open_dialog">Зарегистрироваться</button>
        </div>
        <h1>Виртуальная лаборатория<br>Граф</h1>
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
    <div id="left_panel">
        <h1>Навигация
			<!--<button id="hide_button" style="width:30px;background-color:#093">&#9668</button>-->
		</h1>
        <ul class="main_menu">
			<li class="section"><a href="#">Теория</a></br>
				<ul class="hidden">
					<li><a href="theory/graph.html" target="_blank">Графы</a></li>
					<li><a href="theory/m_sm.html" target="_blank">Матрица смежности</a></li>
					<li><a href="theory/m_inc.html" target="_blank">Матрица инцидентности</a></li>
				</ul>
			</li>
            <li class="section"><a href="#" id="s1">Матрица смежности</a><br>
                <ul class="hidden">
                    <li><a href="?section=sm&task=1">1</a></li>
					<li><a href="?section=sm&task=2">2</a></li>
					<li><a href="?section=sm&task=3">3</a></li>
                </ul>
            </li>
            <li class="section"><a href="#">Матрица инцидентности</a>
                <ul class="hidden">
                    <li><a href="?section=inc&task=1">1</a></li>
					<li><a href="?section=inc&task=2">2</a></li>
					<li><a href="?section=inc&task=3">3</a></li>
                </ul>
			</li>
        </ul>
    </div>
    <div class="main_area">
        <iframe src=<?php
			if (!(empty($section) || empty($task))){
				echo "main.php?id=".session_id()."&section=".$section."&task=".$task;
			}
			else
				echo "main.php?id=".session_id()."&section=sm&task=1";
			?> 
			class="frame">
        </iframe>
    </div>
    <div class="footer">
        <p>(c) nerrevar 2017</p>

        <div id="ya"><!-- Yandex.Metrika informer -->
        <a href="https://metrika.yandex.ru/stat/?id=43325794&amp;from=informer" target="_blank" rel="nofollow"><img src="https://informer.yandex.ru/informer/43325794/3_1_B9FF53FF_99FF33FF_0_pageviews" style="display:inline-block; width:88px; height:31px; border:0;" alt="Яндекс.Метрика" title="Яндекс.Метрика: данные за сегодня (просмотры, визиты и уникальные посетители)" class="ym-advanced-informer" data-cid="43325794" data-lang="ru" /></a>
        <!-- /Yandex.Metrika informer -->

        <!-- Yandex.Metrika counter -->
        <script type="text/javascript">
            (function (d, w, c) {
                (w[c] = w[c] || []).push(function() {
                    try {
                        w.yaCounter43325794 = new Ya.Metrika({
                            id:43325794,
                            clickmap:true,
                            trackLinks:true,
                            accurateTrackBounce:true
                        });
                    } catch(e) { }
                });

                var n = d.getElementsByTagName("script")[0],
                    s = d.createElement("script"),
                    f = function () { n.parentNode.insertBefore(s, n); };
                s.type = "text/javascript";
                s.async = true;
                s.src = "https://mc.yandex.ru/metrika/watch.js";

                if (w.opera == "[object Opera]") {
                    d.addEventListener("DOMContentLoaded", f, false);
                } else { f(); }
            })(document, window, "yandex_metrika_callbacks");
        </script>
        <noscript>
            <div>
                <img src="https://mc.yandex.ru/watch/43325794" style="position:absolute; right:3px; bottom:3px" alt="" />
            </div>
        </noscript>
        </div><!-- /Yandex.Metrika counter -->

    </div>
</body>
</html>
