/*
    Script that handles the Filter Form.
       ->  It handles input
       ->  Injects Ajax data on content div
*/

$(document).ready(redirect_action_via_ajax);

function redirect_action_via_ajax(){
    $("#filterform").submit(function(e){
        e.preventDefault();

        $.ajax({
            type: "GET",
            url: $(this).attr('action'),
            data: $("#filterform").serialize(),
            success: function(data){
                $("#content").html(data);
            }
        });

        return false;
    });
};
