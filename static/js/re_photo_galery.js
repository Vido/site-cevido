/*
    This Script updates the photo galery
*/

$(document).on('click', '.call_photo_ajax', function(event){
    event.preventDefault();

    $.ajax({
        type: "GET",
        url: this.href,
        sucess: function(data){
            alert("foobar");
            $("#details_struct1").html(data);
        },
        fail: function(data){
            alert("AJAX FAIL.");
            $("#details_struct1").html(data);
        },
        always: function(){
            alert("FOO");
        }
    });
});

