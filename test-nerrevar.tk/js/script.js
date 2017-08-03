var test_app = angular.module("test_app",[]);
test_app.controller("sidebar_ctrl", function($scope){
    $scope.menu = {
        item0: {
            name: "Графы",
            sub:[{
                name: "Графы",
                href: "theory/graph.html",
            },{
                name: "Матрица смежности",
                href: "theory/graph.html",
            },{
                name: "Матрица инцидентности",
                href: "theory/graph.html",
            }],
        },
    };
});

test_app.controller("main_ctrl", function($scope){
    
});