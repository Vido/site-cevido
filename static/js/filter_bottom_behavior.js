/*
    Script that handles the Filter Form.
       ->  It handles input
       ->  Injects Ajax data on content div
*/

$(document).ready( function(){
    $("#filterform").submit( function(e){
        e.preventDefault();
 
        $.ajax({
            type: "GET",
            url: $(this).attr('action'),
            data: $("#filterform").serialize(),
            success: function(data){
                $("#content").html(data);
            }
        });

        alert($(this).attr('action'));
        return false;
    });
});

