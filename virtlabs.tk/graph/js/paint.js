function paint_point(){
    $(document).ready(
        $("#main").click(function(){
            var point = $("#main").createElement("img");
            point.setAttribute("class", "point");
            point.setAttribute("src", "point.png");
            $(document).$(".main").innerHTML.appendChild(point);
        });
    );
};
