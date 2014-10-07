function SCPDVideoView(runtime, element) {
    'use strict';

    var $ = window.jQuery;
    var $element = $(element);

    // TODO: Put your logic here
    
    document.domain='class.stanford.edu';
    
    function fnVideoSupport() {
        var name = $('.user .user-link').text().replace(/\s+/g,'');
        message='username=' + name;
        var elem=document.getElementById('helper');
        elem.contentWindow.location = 'https://mvideos.stanford.edu/Viewer/index_helper.html#' + message;
    }
    window.onload = function() {
        fnVideoSupport();
    };
}
