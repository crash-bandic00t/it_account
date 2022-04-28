$('#id_vlan').multiSelect();
// Чтобы после POST не подставлялись предыдущие значения
$('#id_rack option:first').prop('selected', true);
$('#id_equip').html('<option value="">Выберите оборудование...</option>');
$('#id_port').html('<option value="">Выберите порт...</option>');

// Функция возвращает список оборудования в конкретном шкафу
$('#id_rack').change(function () {
    const rackId = $(this).val();  // get the selected rack ID from the HTML input
    $.ajax({                       // initialize an AJAX request
        url: '/ajax/port-dest/equip',                    // set the url of the request (= /ajax/port-dest-update/ )
        data: {
            'rack_id': rackId       // add the rack_id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `get_equip_dropdown` view function
            $('#id_equip').html(data);  // replace the contents of the equip input with the data that came from the server
            $('#id_port').html('<option value="">Выберите порт...</option>');
        }
    });

});

// Функция возвращает список портов в конкретном оборудовании
$('#id_equip').change(function () {
    const equipId = $(this).val();
    $.ajax({
        url: '/ajax/port-dest/ports',
        data: {
            'equip_id': equipId
        },
        success: function (data) {
            $('#id_port').html(data);
        }
    });

});
