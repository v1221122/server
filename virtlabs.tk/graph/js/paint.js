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
		    $(this).off();
	    });

        if (ended == 0)
			$(".line:last").remove();
        ended = 1;
		
        $("#svg").click(function(e){
			
            get_point_index();
			
            var x = e.pageX - 10;
            var y = e.pageY - 93;
            var request = new XMLHttpRequest();

			// var g = $("g", {
				// class:"point",
				// position:"relative",
				// Zindex:"10"
			// });
			
            // var circle = $("circle", {
				// cx:x,
				// cy:y,
				// r:"15",
				// class:"svg_ing_small",
				// fill:"#393"
			// });
			
			var g = document.createElementNS(svg_str, "g");
			$(g).attr("class", "point");
			g.setAttribute("position", "relative");
			g.setAttribute("z-index", "10");
			
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

			g.appendChild(circle);
			g.appendChild(text);
			g.setAttribute("cx", circle.getAttribute("cx"));
			g.setAttribute("cy", circle.getAttribute("cy"));
            $("#svg").append(g);
            $("#console_text").val("Вершина №" + point_index + " добавлена\n" + $("#console_text").val());


            ended = 1;
            request.open("GET", "http://virtlabs.tk/php/temp_table.php?id=" + parse() + "&point_index=" + point_index +"&x=" + x + "&y=" + y, true);
            request.send();
			
			$("#svg").off();
        });
    });
};


function paint_line(){
    $(document).ready(function(){
		//disable active click
        $("#svg").off();
		$(".point").each(function (){
		    $(this).off();
	    });
		if(ended == 0)
			$(".line:last").remove();
				
        $("#console_text").val("Выберите начальную вершину\n" + $("#console_text").val());
		$(".point").each(function (){
			$(this).click(function(e){
				var p = $(this);
				$(".point").each(function(){
					$(this).off();
				});
				

				ended = 0;
				
				$("#console_text").val("Выберите конечную вершину\n" + $("#console_text").val());
				var x1 = $(this).attr("cx");
				var y1 = $(this).attr("cy");
				var x2 = x1;
				var y2 = y1;
				
				var line = document.createElementNS(svg_str, "line");
				line.setAttribute("class", "line svg_img_small");
				line.setAttribute("x1", x1);
				line.setAttribute("y1", y1);
				line.setAttribute("x2", x2);
				line.setAttribute("y2", y2);
				line.setAttribute("position", "relative");
				line.setAttribute("z-index", "2");
				line.setAttribute("line_id", line_id);
				
				// var line = $("line", {
					// "class":"line, svg_img_small",
					// "x1":x1,
					// "y1":y1,
					// "x2":x2,
					// "y2":y2,
					// "position":"relative",
					// "z-index":"2",
					// "id":line_id
				// });
				line_id++;
				
				$("#svg").append(line);
				$("#svg").on("mousemove", function(e2){
    				line.setAttribute("x2", e2.pageX);
					line.setAttribute("y2", e2.pageY - 80);
				});
				$(".point").each(function(){
					$(this).click(function(e3){
						line.setAttribute("x2", $(this).attr("cx"));
						line.setAttribute("y2", $(this).attr("cy"));
						$("#svg").off();
						
						ended = 1;

                        var request = new XMLHttpRequest();
						request.open("GET", "php/temp_table_line.php?id=" + parse() + "&p1=" + p.find('text').text() + "&p2=" + $(this).find('text').text());
						request.send(null);
						$(".point").each(function(){
							$(this).off();
						});
					});
				});
			});
        });
    });
};

function replace(){
	$(document).ready(function(){
		$("#console_text").val("Выберите вершину\n" + $("#console_text").val());
		$(".point").each(function(){
			$(this).click(function(e){
				
				var p = $(this);
				
				$("#console_text").val("Выберите новое место\n" + $("#console_text").val());
				$(".point").each(function(){
					$(this).off();
				});
				$("#svg").on("mousemove", function(e2){
					p.attr("cx", e2.pageX);
					p.attr("cy", e2.pageY - 80);
				});
				$("#svg").on("click", function(e3){
						$("#console_text").val("Вершина перемещена\n" + $("#console_text").val());
						p.attr("cx", e3.pageX);
						p.attr("cy", e3.pageY - 80);
						$("#svg").off();
				});
			});
		});
	});
};

function delete_any(){
    $(document).ready(function(){
        $(".point").each(function(){
            $(this).click(function(e){
                $(this).remove();
				
				var request = new XMLHttpRequest();
				request.open("GET", "php/delete.php?id=" + parse() + "&point_num=" + $(this).find("text").text());
				request.send();
				request.onreadystatechange = function(){
					if(request.readyState == 4){
						var deleted_lines = request.responseText.trim().split(' ');
						for (i = 0; i < deleted_lines.length; i++){
							var num = deleted_lines[i];
							var lines = $("line[class*='line']");
							$("line[class*='line'][line_id*=" + num + "]").remove();
							get_point_index();
						}
					}
				};
				$(".point").each(function(){
					$(this).off();
				});
            });
        });
    });
};

function get_point_index(){
	var request = new XMLHttpRequest();
	request.open("GET", "php/get_point_num.php?id=" + parse());
	request.send();
	request.onreadystatechange = function(){
		if (request.readyState == 4){
			point_index = request.responseText;
		}
	}
}

window.onbeforeunload = function(){
	var request = new XMLHttpRequest();
	request.open("GET", "php/drop.php?id=" + parse(), false);
	request.send(null);
	while (request.readyState != 4);
	return;
};
