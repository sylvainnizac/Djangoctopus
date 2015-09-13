var App = angular.module('SnipDet', ['ngSanitize']);

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

App.controller('SnipDetCtrl', function($scope, $http, $location) {
  $http.get('json')
       .then(function(res){
          $scope.snip = res.data;
        });
});