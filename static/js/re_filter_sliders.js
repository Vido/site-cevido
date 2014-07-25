/*
    Defines dynamic JQueryUI HTML components behavior.
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

/********************** Area *******************************************/

function print_area(nri, nrf){
    $("#area").val(
        "De " + nri + "m² a " + nrf + "m²"
    );
};

function update_area_slider() {
    $( "#slider-area" ).slider({
        range: true,
        min: 10,
        max: 1000,
        step: 1,
        values: [ 45, 250 ],
        slide: function( event, ui ) {
            // Show values
            print_area(ui.values[0], ui.values[1]);
             // GET Request
            $("#area__gte").val(ui.values[0]);
            $("#area__lte").val(ui.values[1]);
        }
    });
    print_area(
        $( "#slider-area" ).slider("values", 0),
        $( "#slider-area" ).slider("values", 1)
    );
     // init hidden values
    $("#area__gte").val(45);
    $("#area__lte").val(250);
};

/********************** Utils *******************************************/

function update_sliders() {
    update_price_slider();
    update_rooms_slider();
    update_area_slider();
};
