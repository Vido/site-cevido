/*
    TODO: What is this file
*/

/********************** Price *******************************************/

function print_price(pi, pf){
    $("#price").val(
        "R$" + pi + "mil até R$" + pf + "mil"
    );
};

function update_price_slider() {
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
    });
    print_price(
        $( "#slider-price" ).slider("values", 0),
        $( "#slider-price" ).slider("values", 1)
    );
    // init hidden values
    $("#price__gte").val(0);
    $("#price__lte").val(2500);
}

/********************** Rooms *******************************************/

function print_rooms(nri, nrf){
    $("#rooms").val(
        "De " + nri + " a " + nrf + "quartos"
    );
};

function update_rooms_slider() {
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
    });
    print_rooms(
        $( "#slider-rooms" ).slider("values", 0),
        $( "#slider-rooms" ).slider("values", 1)
    );
     // init hidden values
    $("#rooms__gte").val(1);
    $("#rooms__lte").val(8);
};

/********************** Utils *******************************************/

function update_sliders() {
    update_price_slider();
    update_rooms_slider();
};
