function paint_point(){
    $(document).ready(function(){
        $("#console_text").val("Выберите место\n" + $("#console_text").val());
        $("#svg").off("click");
        $("#svg").click(function(e){
            var x = e.pageX - 15;
            var y = e.pageY - 15;
            var circle = document.createElementNS(svg_str, "circle");
            circle.setAttribute('cx', x);
            circle.setAttribute('cy', y);
            circle.setAttribute('r', '30');
            circle.setAttribute('class','svg_img');
            var text = document.createElementNS(svg_str, "text");
            text.setAttribute('class', 'svg_img');
            text.setAttribute('font-size', '26');
            text.setAttribute('fill', '#000');
            text.textContent = '' + point_index;
            text.setAttribute('x', x);
            text.setAttribute('y', y);
            point_index++;
            $("#svg").append(circle);
            $("#svg").append(text);
            $("#console_text").val("Вершина добавлена\n" + $("#console_text").val());
        });
    });
};

function paint_line(){
    $(document).ready(function(){
        $("#svg").off("click");
        $("#console_text").val("Выберите начальную вершину\n" + $("#console_text").val());
        var line = document.createElementNS(svg_str, "line");
        $("#svg").click(function(e){
            $("#console_text").val("Выберите конечную вершину\n" + $("#console_text").val());
            var x1 = e.pageX;
            var y1 = e.pageY;
            var x2 = e.pageX;
            var y2 = e.pageY;
            line.setAttribute('x1', x1);
            line.setAttribute('y1', y1);
            line.setAttribute('x2', x2);
            line.setAttribute('y2', y2);
            $("#svg").append(line);
            $("#svg").on("mousemove", function(e2){
                line.setAttribute('x2', e2.pageX);
                line.setAttribute('y2', e2.pageY);
            });
            $("#svg").off("click");
            $("#svg").click(function(e3){
                line.setAttribute('x2', e3.pageX);
                line.setAttribute('y2', e3.pageY);
                $("#svg").off("click");
                $("#svg").off("mousemove");
            });
        });
    });
};
