<?php
    session_start();
?>
<!DOCTYPE html>
<html>
<head>
    <title>VirtLabGraph</title>
    <meta name="yandex-verification" content="3de45f2600675f37" />
    <link rel="stylesheet" href="style.css"/>
	<link rel="shortcut icon" href="img/icon.png" type="image/x-icon"/>
    <script src="js/jquery.js"></script>
    <script src="js/hide.js"></script>
	<?php 
		require_once "svg/icons.svg";
    ?>
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
					<svg id="dialog_close">
						<use xlink:href="#icon_close"></use>
					</svg>
                    <label for="reg_login" class="dialog_label">Логин</label><br>
                    <input type="text" name="reg_login" class="dialog_input"/><br>
                    <label for="reg_password" class="dialog_label">Пароль</label><br>
                    <input type="password" name="reg_password" class="dialog_input"/><br>
                    <input type=submit value="Регистрация" class="dialog_button"/><br>
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
        <iframe src=<?php echo "main.php?id=".session_id() ?> class="frame">
        </iframe>
    </div>
    <div class="footer">
        <h1>footer</h1>

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
