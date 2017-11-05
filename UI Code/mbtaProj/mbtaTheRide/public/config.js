//The main purpose of this file is to configure the file
(function () {
    angular
        .module("WamApp")//readOnly
        .config(configuration)
        .controller("homeController", homeController)
        .controller("loginController", loginController);

    function configuration($routeProvider, $httpProvider) {
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/json; charset=utf-8';
        $httpProvider.defaults.headers.post['Accept'] = 'application/json, text/javascript';
        $httpProvider.defaults.headers.post['Access-Control-Max-Age'] = '1728000';

        $routeProvider
            .when("/", {
                templateUrl: "views/home.html",
                controller: "homeController",
                controllerAs: "model"
            })

            .when("/login", {
                templateUrl: "views/login.html",
                controller: "loginController",
                controllerAs: "model"
            })
    }


})();