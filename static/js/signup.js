/**
 * user sign up module
 *
 * @author victor li
 * @date 2015/04/18
 */

define(['jquery'], function($) {
    $('body').on('click', '.js-sign-up', function(e) {
        e.preventDefault();
        location.href = '/user/user_signup';
    });
});

