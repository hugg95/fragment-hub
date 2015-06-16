define(['jquery'], function($) {

    $('body')
    .off('click', '.js-select-library')
    .on('click', '.js-select-library', function(e) {
        $(this).next().toggle();
    })

    function getWindowHeight() {
        return $(document).height();
    }

    $('#editor-area').css('height', getWindowHeight());

});
