var App = angular.module('PhotoGalery', ['filters']);

App.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

App.controller('PhotoAllCtrl', function($scope, $http) {
    $http.get('json')
        .then(function(res){
            $scope.photos = res.data;
        });
});

angular.module('filters', []).
    filter('truncate', function () {
        return function (text, start, end) {

            if (isNaN(end))
                String(text).substring(start);

            return String(text).substring(start, end);

        };
    });