$("#btn_card_payment").click(function() {
     let data = {
         "card_number": $("#cp_card_number").val(),
         "card_ttl": $("#cp_card_ttl").val().replace('/', '.'),
         "cvc": $("#cp_cvc").val(),
         "amount": $("#cp_amount").val(),
         "comment": $("#cp_comment").val(),
         "email": $("#cp_email").val()
     };

     $.post("/api/card_payment",
         JSON.stringify(data),
         function (data) {
         if ('error' in data) {
             alert(data['error']);
         }
         else if ('result' in data) {
             alert(data['result']);
         }
         else {
             alert('Неизвестная ошибка');
         }
     });
});