/*
    TODO: What is this file
*/

/********************** Price *******************************************/

function print_price(pi, pf){
    $("#price").val(
        "R$" + pi + "mil até R$" + pf + "mil"
    );    
};


$(function() {
    $( "#slider-price" ).slider({
        range: true,
        min: 0,
        max: 2500,
        step: 10,
        values: [ 500, 1000 ],
        slide: function( event, ui ) {
            // Show values
            print_price(ui.values[0], ui.values[1]);
            // GET Request
            $("#price__gte").val(ui.values[0]);
            $("#price__lte").val(ui.values[1]);
        }
    })
});

/********************** ROOMS *******************************************/

function print_rooms(nri, nrf){
    $("#rooms").val(
        "De " + nri + " a " + nrf + "quartos"
    );    
};

$(function() {
    $( "#slider-rooms" ).slider({
        range: true,
        min: 1,
        max: 8,
        step: 1,
        values: [ 2, 6 ],
        slide: function( event, ui ) {
            // Show values
            print_rooms(ui.values[0], ui.values[1]);
             // GET Request
            $("#rooms__gte").val(ui.values[0]);
            $("#rooms__lte").val(ui.values[1]);
        }
    })
});

