$(document).ready(function(){
    $(".hidden").hide();
});
$(document).ready(
    function(){
        $("#s1").click(
            function(){
                if ($("#hide1").is(":visible"))
                    $("#hide1").hide();
                else
                    $("#hide1").show();
             }
        )
    }
);
