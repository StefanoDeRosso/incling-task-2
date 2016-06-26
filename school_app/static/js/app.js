var schoolApp = angular.module('schoolApp', ['ngResource']);

schoolApp.factory('Classroom', ['$resource', function($resource) {
    return $resource('/classrooms/?format=json', {}, {
        query: {
            method: 'GET',
            isArray: true,
        }
    });
}]);

schoolApp.controller('schoolCtrl', ['$scope', 'Classroom', 
	function($scope, Classroom) {
		$scope.classrooms = Classroom.query();
		Classroom.query().$promise.then(function(data) {
		        $scope.classrooms = data;
		        console.log(Classroom.query({}));
			});
		}]);

