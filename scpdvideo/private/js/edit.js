function SCPDVideoEdit(runtime, element) {
    'use strict';

    var $ = window.$;
    var $element = $(element);
    var buttonSave = $element.find('.save-button');
    var buttonCancel = $element.find('.cancel-button');
    var url = runtime.handlerUrl(element, 'studio_view_post');

    buttonCancel.on('click', function () {
        runtime.notify('cancel', {});
        return false;
    });

    buttonSave.on('click', function () {
        runtime.notify('save', {
            message: 'Saving...',
            state: 'start'
        });
        $.ajax(url, {
            type: 'POST',
            data: JSON.stringify({
                'xblock_scpdvideo_name':
                    $('#xblock_scpdvideo_name').val(),
                'xblock_scpdvideo_video_url':
                    $('#xblock_scpdvideo_video_url').val()
            }),
            success: function buttonSaveOnSuccess() {
                runtime.notify('save', {
                    state: 'end'
                });
            },
            error: function buttonSaveOnError() {
                runtime.notify('error', {});
            }
        });
        return false;
    });
}
