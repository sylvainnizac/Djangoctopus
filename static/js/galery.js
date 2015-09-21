var App = angular.module('PhotoGalery', ['filters']);

App.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

App.controller('PhotoCtrl', function($scope, $http) {

    $http.get('json')
        .then(function(res){
            $scope.photos = res.data;
        });

    $scope.total = function(){
        $http.get('json').then(function(res){
            $scope.photos = res.data;
        });
    };

    $scope.filtre = function(faction, sectorielle, figurine){
        
        var added = faction
        
        if (!isNaN(sectorielle)) {
            added += '/' + sectorielle
        }
        
        if (!isNaN(figurine)) {
            added += '/' + figurine
        }
        
        $http.get(added + '/json').then(function(res){
            $scope.photos = res.data;
        });
    };
});

angular.module('filters', []).
    filter('truncate', function () {
        return function (text, start, end) {

            if (isNaN(end))
                String(text).substring(start);

            return String(text).substring(start, end);

        };
    });
