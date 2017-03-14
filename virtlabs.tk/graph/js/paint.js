function parse(){
    var params = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    var values = params[0].split('=');
    var value = values[1];
    return value;
};

function paint_point(){
    $(document).ready(function(){
        $("#console_text").val("Выберите место\n" + $("#console_text").val());
		$(".point").each(function (){
		    $(this).off("click");
	    });
		
        $("#svg").click(function(e){
            var x = e.pageX - 10;
            var y = e.pageY - 93;
            var request = new XMLHttpRequest();

			var g = document.createElementNS(svg_str, "g");
			g.setAttribute("class", "point");
			
            var circle = document.createElementNS(svg_str, "circle");
            circle.setAttribute('cx', x);
            circle.setAttribute('cy', y);
            circle.setAttribute('r', '15');
            circle.setAttribute('class','svg_img_small');
			circle.setAttribute('fill', '#393');

            var text = document.createElementNS(svg_str, "text");
            text.setAttribute('class', 'svg_img_small');
            text.setAttribute('font-size', '12');
            text.setAttribute('fill', '#000');
            text.textContent = '' + point_index;
            text.setAttribute('x', x - 5);
            text.setAttribute('y', y + 2);

			g.append(circle);
			g.append(text);
            $("#svg").append(g);
            $("#console_text").val("Вершина №" + point_index + " добавлена\n" + $("#console_text").val());

            request.open("GET", "http://virtlabs.tk/php/temp_table.php?id=" + parse() + "&point_index=" + point_index +"&x=" + x + "&y=" + y, true);
            request.send();

            point_index++;
        });
    });
};

function paint_line(){
    $(document).ready(function(){
		//disable active click
        $("#svg").off("click");
		$(".point").each(function (){
		    $(this).off("click");
	    });
			
        $("#console_text").val("Выберите начальную вершину\n" + $("#console_text").val());
        var line = document.createElementNS(svg_str, "line");
		var arr = $(".point");
		arr.each(function (){
			$(this).click(function(e){
				var p = $(this);
				arr.each(function(){
					if ($(this) != p)
						$(this).off("click");
				});
	            var request = new XMLHttpRequest();
				request.open("GET", "/php/temp_table_select.php?id=" + parse());
				request.send();
				request.onreadystatechange = function(){
					if (request.readyState == 4){
						if (request.responseText == "true"){
							$("#console_text").val("Выберите конечную вершину\n" + $("#console_text").val());
							var x1 = e.pageX - 10;
							var y1 = e.pageY - 93;
							var x2 = x1;
							var y2 = y1;
							line.setAttribute("x1", x1);
							line.setAttribute("y1", y1);
							line.setAttribute("x2", x2);
							line.setAttribute("y2", y2);
							line.setAttribute("stroke", "#000");
							line.setAttribute("stroke-width", "2");
							$("#svg").append(line);
							$("#svg").on("mousemove", function(e2){
								line.setAttribute("x2", e2.pageX - 10);
								line.setAttribute("y2", e2.pageY - 93);
							});
							arr.each(function(){
								$(this).click(function(e3){
									line.setAttribute("x2", e3.pageX - 10);
									line.setAttribute("y2", e3.pageY - 93);
									arr.each(function(){
										$(this).off("click");
									});
									$("#svg").off("mousemove");
								});
							});
						};
					};
				};
			});
        });
    });
};
