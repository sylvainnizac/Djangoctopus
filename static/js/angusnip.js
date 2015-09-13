var App = angular.module('Snipdet', []);

App.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});



App.controller('SnipdetCtrl', function($scope, $http, $location) {
  $http.get('json')
       .then(function(res){
          $scope.post = res.data;
        });
});