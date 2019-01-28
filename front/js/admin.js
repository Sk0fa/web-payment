$(".not_safe_payment").click(function () {
    let element = $(this);
    let payment_id = $(this).attr('class').split(' ')[0].split('_')[1];
    let data = {
        "payment_id": payment_id,
        "notSafe": true
    };


    $.ajax({
        type: 'PATCH',
        url: '/api/card_payment',
        data: JSON.stringify(data),
        processData: false,
        contentType: 'application/json'
    });

    $(element).parent().parent().css("background-color", "coral");
});