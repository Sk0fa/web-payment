function post(url, data) {
    $.post(url,
        JSON.stringify(data),
        function (data) {
            if ('error' in data) {
                alert(data['error']);
            } else if ('result' in data) {
                alert(data['result']);
            } else {
                alert('Неизвестная ошибка');
            }
        });
}

function validate_card_payment() {
    let result = true;

    let value = $("#cp_card_number").val();
    if (!value.match(/\d{16}/gm)) {
        $("#cp_card_number").addClass("is_invalid");
        result = false;
    }

    value = $("#cp_card_ttl").val();
    if (!value.match(/(0?[1-9]|1[012])\/\d{4}/gm)) {
        $("#cp_card_ttl").addClass("is_invalid");
        result = false;
    }

    value = $("#cp_cvc").val();
    if (!value.match(/\d{3}/gm)) {
        $("#cp_cvc").addClass("is_invalid");
        result = false;
    }

    value = $("#cp_amount").val();
    if (!value.match(/\d+/gm)) {
        $("#cp_amount").addClass("is_invalid");
        result = false;
    }
    else if (parseInt(value) > 75000) {
        $("#cp_amount").addClass("is_invalid");
        result = false;
    }

    value = $("#cp_comment").val();
    if (!value.match(/([a-zA-Z0-9_-]){1,150}/gm)) {
        $("#cp_comment").addClass("is_invalid");
        result = false;
    }

    return result;
}

function validate_internet_payment() {
    let result = true;

    let value = $("#in_bic").val();
    if (!value.match(/\d+/gm)) {
        $("#in_bic").addClass("is_invalid");
        result = false;
    }

    value = $("#in_account_number").val();
    if (!value.match(/\d{20}/gm)) {
        $("#in_account_number").addClass("is_invalid");
        result = false;
    }

    value = $("#in_amount").val();
    if (!value.match(/\d+/gm)) {
        $("#in_amount").addClass("is_invalid");
        result = false;
    }
    else if (parseInt(value) > 75000) {
        $("#in_amount").addClass("is_invalid");
        result = false;
    }

    return result;
}

function validate_requested_payment() {
    let result = true;

    let value = $("#rp_tax").val();
    if (!value.match(/\d+/gm)) {
        $("#rp_tax").addClass("is_invalid");
        result = false;
    }

    value = $("#rp_bic").val();
    if (!value.match(/\d+/gm)) {
        $("#rp_bic").addClass("is_invalid");
        result = false;
    }

    value = $("#rp_account_number").val();
    if (!value.match(/\d{20}/gm)) {
        $("#rp_account_number").addClass("is_invalid");
        result = false;
    }

    value = $("#rp_amount").val();
    if (!value.match(/\d+/gm)) {
        $("#rp_amount").addClass("is_invalid");
        result = false;
    }
    else if (parseInt(value) > 75000) {
        $("#rp_amount").addClass("is_invalid");
        result = false;
    }

    value = $("#rp_phone").val();
    if (!value.match(/^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im)) {
        $("#rp_phone").addClass("is_invalid");
        result = false;
    }

    return result;
}

$("#btn_card_payment").click(function () {
    if (!validate_card_payment()) {
        return;
    }

    let data = {
        "card_number": $("#cp_card_number").val(),
        "card_ttl": $("#cp_card_ttl").val().replace('/', '.'),
        "cvc": $("#cp_cvc").val(),
        "amount": $("#cp_amount").val(),
        "comment": $("#cp_comment").val(),
        "email": $("#cp_email").val()
    };

    post("/api/card_payment", data);
});

$("#btn_internet_payment").click(function () {
    if (!validate_internet_payment()) {
        return;
    }

    let data = {
        "payment_from": $("#in_payment_from").val(),
        "bic": $("#in_bic").val(),
        "account_number": $("#in_account_number").val(),
        "amount": $("#cp_amount").val(),
        "comment": $("#in_comment").val(),
        "amount": $("#in_amount").val()
    };

    $.post("/api/internet_bank_payment",
        JSON.stringify(data),
        function (data) {
            console.log(data);
            let file = new Blob([data], {type: 'text'});
            if (window.navigator.msSaveOrOpenBlob) // IE10+
                window.navigator.msSaveOrOpenBlob(file, 'internet_bank_payment.txt');
            else { // Others
                let a = document.createElement("a"),
                    url = URL.createObjectURL(file);
                a.href = url;
                a.download = 'internet_bank_payment.txt';
                document.body.appendChild(a);
                a.click();
                setTimeout(function () {
                    document.body.removeChild(a);
                    window.URL.revokeObjectURL(url);
                }, 0);
            }
        });
});

$("#btn_requested_payment").click(function () {
    if (!validate_requested_payment()) {
        return;
    }

    let data = {
        "tax": $("#rp_tax").val(),
        "bic": $("#rp_bic").val(),
        "account_number": $("#rp_account_number").val(),
        "comment": $("#rp_comment").val(),
        "amount": $("#rp_amount").val(),
        "phone": $("#rp_phone").val(),
        "email": $("#rp_email").val()
    };

    post("/api/requested_payment", data);
});

function clear_forms() {
    $("#text_put_payment").removeClass("selected");
    $("#text_requested_payment").removeClass("selected");
    $("#text_put_card_payment").removeClass("selected");
    $("#text_put_internet_payment").removeClass("selected");

    $("#put_card_payment").hide();
    $("#put_internet_payment").hide();
    $("#requested_payment").hide();
}

$("#text_put_payment").click(function () {
    clear_forms();

    $(this).addClass("selected");
    $("#text_put_card_payment").addClass("selected");
    $("#put_card_payment").show();
    $("#put_payment").show();
});

$("#text_requested_payment").click(function () {
    clear_forms();

    $(this).addClass("selected");
    $("#requested_payment").show();
    $("#put_payment").hide();
});

$("#text_put_internet_payment").click(function () {
    clear_forms();

    $(this).addClass("selected");
    $("#text_put_payment").addClass("selected");
    $("#put_internet_payment").show();
    $("#put_payment").show();
});

$("#text_put_card_payment").click(function () {
    clear_forms();

    $(this).addClass("selected");
    $("#text_put_payment").addClass("selected");
    $("#put_card_payment").show();
    $("#put_payment").show();
});

$("input").click(function () {
    $(this).removeClass("is_invalid");
});