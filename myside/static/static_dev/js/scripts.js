$(document).ready(function(){        /* Создание консоли в F12*/
    var form = $('#form-buying_product'); /* Название формы */
    console.log(form);

    function basketUpdating(product_id, nmb, is_delete){
        var data = {};                              /* переменные которые мы отпровляем*/
            data.product_id = product_id;
            data.nmb = nmb;
            var csrf_token = $('#form-buying_product [name="csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;

            if (is_delete){
                data["is_delete"] = true;
            }

            var url = form.attr('action');
        console.log(data)
            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                    console.log("OK");
                    console.log(data.products_total_nmb);
                    if (data.products_total_nmb || data.products_total_nmb == 0) {
                        $('#basket_total_nmb').text('('+data.products_total_nmb+')');
                        console.log(data.products);
                        $(".basket-item ul").html('');
                        $.each(data.products, function(k, v) {
                            $('.basket-items ul').append('<li>'+v.name+', ' + v.nmb + ' шт.' + ' по ' + v.price_per_item +' РУБ  ' +
                                '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+
                                '</li>');
                        })
                    }

                },
                error: function(){
                    console.log("error")
                }
            })

    }

    form.on('submit', function(e){   /*Чтобы отпровлять форму */
        e.preventDefault();            /*Чтобы форма остовалась */
        console.log('123');
        var nmb = $('#number').val();            /* Какое количество покупается*/
        console.log(nmb);                        /* Выведение в кансоль количества */
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");     /* Id продукта которая пойдет в карзину*/ 
        var product_name = submit_btn.data("name");        /* имя продукта которая пойдет в карзину*/ 
        var product_price = submit_btn.data("price"); 
        console.log(product_id);                         /* Выведение в кансоль id продукта */
        console.log(product_name);                        /* Выведение в кансоль имя продукта */

        basketUpdating(product_id, nmb, is_delete=false)
        

    });

    function shovingBasket(){                               /* функция что бы не писать несколько раз*/
        $('.basket-items').toggleClass('hidden'); 
    }

    $('.basket-conteiner').on('click', function(e){                     /* при нажатии*/
        e.preventDefault();
        shovingBasket()
    })

    $('.basket-conteiner').mouseover('click', function(){             /* появляется при наведении  */
        shovingBasket()
    })

    $('.basket-conteiner').mouseout('click', function(){               /* Проподает  при отведении*/
        shovingBasket();
    })
    
    $(document).on('click', '.delete-item', function(e){                  /* Удаление */
        e.preventDefault();
        product_id = $(this).data("product_id")
        nmb = 0;
        basketUpdating(product_id, nmb, is_delete=true)
    });

    function calculatingBasketAmount(){
        var total_order_amount = 0;
        $(".total-product-in-basket-amount").each(function(){
            total_order_amount += parseInt($(this).text());
        });
        console.log(total_order_amount);
        $('#total_order_amount').text(total_order_amount);
    };

    $(document).on("change", ".product-in-basket-nmb", function(){
        var current_nmb = $(this).val();
        console.log(current_nmb);
        var current_tr = $(this).closest("tr");
        var current_price = parseInt(current_tr.find('.product-price').text());
        var total_amount = current_nmb*current_price;
        current_tr.find('.total-product-in-basket-amount').text(total_amount);

        calculatingBasketAmount();
    });

    calculatingBasketAmount();
});