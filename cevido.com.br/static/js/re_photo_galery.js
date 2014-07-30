/*
    This Script updates the photo galery
*/

$(document).on('click', '.call_photo_ajax', function(event){
    event.preventDefault();
    $.ajax({
        type: "GET",
        url: this.href,
        success: function(data){
            $('#large_photo').attr('src', data.get_display_url);
        },
        fail: function(data){
            alert("AJAX FAIL.");
        }
    });
});

