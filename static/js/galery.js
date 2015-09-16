var App = angular.module('PhotoGalery', []);

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
