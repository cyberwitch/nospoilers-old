$(function() {
    $('#seasons').accordion({
        active: false,
        collapsible: true,
        heightStyle: 'content',
        beforeActivate: function(event, ui) {
            if (ui.newPanel.hasClass('empty')) {
                ui.newPanel.removeClass('empty').addClass('loading');
                $.getJSON($SCRIPT_ROOT + '/show/' + $('#seasons').attr('data-show-id') + '/season/' + ui.newHeader.attr('id').substring(1), function (data) {
                    var $episodeList = $('<ol></ol>');
                    _.each(data['episodes'], function (episode) {
                        var $episode = $('<li>'),
                            text = episode['name'];

                        text += episode['air_date'] ? ' (' + episode['air_date'] + ')' : '';
                        $episode.append(text);
                        $episodeList.append($episode);
                    });
                    ui.newPanel.removeClass('loading').append($episodeList);
                });
            }
        }
    });
});