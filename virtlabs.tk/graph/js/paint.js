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
			remove_last_line();
        ended = 1;
		
        get_point_index();
		
        $("#svg").click(function(e){
			
			
            var x = e.pageX - 10;
            var y = e.pageY - 93;
            var request = new XMLHttpRequest();
			
			var g = document.createElementNS(svg_str, "g");
			var attrs = {
				"class": "point",
				"position": "relative",
				"z-index": "10"
			};
			$(g).attr(attrs);
			
            var circle = document.createElementNS(svg_str, "circle");
			attrs = {
				"class": "svg_img_small",
				"cx": x,
				"cy": y,
				"r": "15",
				"fill": "#393"
			};
			$(circle).attr(attrs);

            var text = document.createElementNS(svg_str, "text");
			attrs = {
				"class": "svg_img_small",
				"font-size": "12",
				"fill": "#000",
				"x": x-5,
				"y": y+2
			}
			$(text).attr(attrs);
            text.textContent = '' + point_index;

			g.appendChild(circle);
			g.appendChild(text);
			$(g).attr("cx", $(circle).attr("cx"));
			$(g).attr("cy", $(circle).attr("cy"));
            $("#svg").append(g);
            $("#console_text").val("Вершина №" + point_index + " добавлена\n" + $("#console_text").val());

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
				var attrs = {
					"class": "line svg_img_small",
					"x1": x1,
					"y1": y1,
					"x2": x2,
					"y2": y2,
					"position": "relative",
					"z-index": "2",
					"line_id": line_id
				}
				$(line).attr(attrs);
				
				line_id++;
				
				$("#svg").append(line);
				$("#svg").on("mousemove", function(e2){
    				$(line).attr("x2", e2.pageX);
					$(line).attr("y2", e2.pageY - 80);
				});
				$(".point").each(function(){
					$(this).click(function(e3){
						$(line).attr("x2", $(this).attr("cx"));
						$(line).attr("y2", $(this).attr("cy"));
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
			$(this).on("mouseup", function(e){
				
				var p = $(this);
				
				$("#console_text").val("Выберите новое место\n" + $("#console_text").val());
				$(".point").each(function(){
					$(this).off();
				});
				
				var line_p1;
				var line_p2;
				
				var request = new XMLHttpRequest();
				request.open("GET", "php/replace_p1.php?id=" + parse() + "&point_num=" + $(this).find("text").text());
				request.send();
				request.onreadystatechange = function(){
					if(request.readyState == 4){
						var replaced_lines = request.responseText.trim().split(' ');
						for (i = 0; i < replaced_lines.length; i++){
							var num = replaced_lines[i];
							var lile_p1 = $("line[class*='line'][line_id*='" + num + "']");
						}
					}
				};
				request.close;
				
				var request = new XMLHttpRequest();
				request.open("GET", "php/replace_p2.php?id=" + parse() + "&point_num=" + $(this).find("text").text());
				request.send();
				request.onreadystatechange = function(){
					if(request.readyState == 4){
						var replaced_lines = request.responseText.trim().split(' ');
						for (i = 0; i < replaced_lines.length; i++){
							var num = replaced_lines[i];
							var line_p2 = $("line[class*='line'][line_id*='" + num + "']");
						}
					}
				};
				request.close;
				
				$("#svg").on("mousemove", function(e2){
					p.attr("cx", e2.pageX);
					p.attr("cy", e2.pageY - 80);
					p.find("circle").attr("cx", e2.pageX);
					p.find("circle").attr("cy", e2.pageY - 80);
					p.find("text").attr("x", e2.pageX - 5);
					p.find("text").attr("y", e2.pageY - 78);
					if (line_p1)
						for (i = 0; i < line_p1.length; i++){
							line_p1[i].attr("x1", e2.pageX);
						}
				});
				
				$("#svg").on("mousedown", function(e3){
					p.attr("cx", e3.pageX);
					p.attr("cy", e3.pageY - 80);
					$("#console_text").val("Вершина перемещена\n" + $("#console_text").val());
					p.find("circle").attr("cx", e3.pageX);
					p.find("circle").attr("cy", e3.pageY - 80);
					p.find("text").attr("x", e3.pageX - 5);
					p.find("text").attr("y", e3.pageY - 78);
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
							$("line[class*='line'][line_id*='" + num + "']").remove();
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

function remove_last_line(){
	var line = $(".line:last");
	
	line.remove();
}

function get_point_index(){
	var request = new XMLHttpRequest();
	request.open("GET", "php/get_point_num.php?id=" + parse(), true);
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
