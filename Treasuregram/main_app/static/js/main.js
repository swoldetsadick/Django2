/**
 * Created by User on 21.04.2017.
 */
$('button').on('click', function(event){
    event.preventDefault();
    var element = $(this);
    $.ajax({
        url: '/like_treasure',
        type: 'GET',
        data: {treasure_id: element.attr("data-id")},
        success: function(response){
            element.html(' ' + response);
        }
    });
});