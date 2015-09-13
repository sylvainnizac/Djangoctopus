var App = angular.module('SnipAccueil', ['ngSanitize']);

App.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

App.filter('newlines', function($sce){
    return function(msg,is_xhtml) {
        var is_xhtml = is_xhtml || true;
        var breakTag = (is_xhtml) ? '<br />' : '<br>';
        var msg = (msg + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1'+ breakTag +'$2');
        return $sce.trustAsHtml(msg);
    }
});

App.controller('SnipAllCtrl', function($scope, $http, $location) {
    $scope.desclimit = 100;
    $http.get('json')
        .then(function(res){
            $scope.snips = res.data;
        });

    $scope.shall = function () {
        $scope.desclimit = undefined;
    };

    $scope.hiall = function () {
        $scope.desclimit = 100;
    };
});