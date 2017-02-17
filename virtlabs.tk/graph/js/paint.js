function paint_point(){
    $(document).ready(function(){
        $("#console_text").val("Выберите место\n" + $("#console_text").val());
        $("#main").off("click");
        $("#main").click(function(e){
            var x = e.pageX - 15;
            var y = e.pageY - 15;
            var str = '<img class="point_img" src="img/point.png" alt="point" style="display:block; position:absolute; left:' + x +'px; top:' + y +'px" >';
            $("#main").append(str);
            $("#console_text").val("Вершина добавлена\n" + $("#console_text").val());
        });
    });
};

function paint_line(){
    $(document).ready(function(){
        $("#svg").off("click");
        $("#console_text").val("Выберите начальную вершину\n" + $("#console_text").val());
        var str = '<line stroke="#000" stroke-width="3" ';
        $("#svg").click(function(e){
            $("#console_text").val("Выберите конечную вершину\n" + $("#console_text").val());
            var x1 = e.pageX;
            var y1 = e.pageY;
            str += 'x1="' + x1 + '" y1="' + y1 + '" ';
            $("#svg").off("click");
            $("#svg").click(function(e2){
                var x2 = e2.pageX;
                var y2 = e2.pageY;
                str += 'x2="' + x2 + '" y2="' + y2 + '"/>';
        $("#console_text").val(str + "\n" + $("#console_text").val());
                $("#svg").append(str);
                $("#svg").off("click");
            });
        });
    });
};
