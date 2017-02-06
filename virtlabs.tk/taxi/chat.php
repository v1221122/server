<?php
echo '
<div style="min-width:40%; max-width:40%; border:2px solid black; 
margin-left:30%; margin-right:30%; max-height:224px">
<iframe style="max-height:200px; min-height:200px; width:100%" 
src="chat_content.php?user='.$_SESSION['login'].'">
</iframe>
</div>
';
?>
    
