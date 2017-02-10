<?php
echo '
<div style="float:left">
<form method="post" action="index.php">
<input type="hidden" name="work"/>
<input type="submit" value="Работаю" style="min-height:80px; min-width:120px"/>
</form>
<form method="post" action="index.php">
<input type="hidden" name="not_work"/>
<input type="submit" value="Не работаю" style="min-height:80px; min-width:120px"/>
</form>
</div>
';
?>
