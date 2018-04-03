$(document).ready(function() {

    var form = $('#form_buying_product');
    form.on('submit', function(e) {
        e.preventDefault();
        var nmb = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id =  submit_btn.data("product_id");
        var name = submit_btn.data("name");
        var price = submit_btn.data("price");
        //console.log(product_id);
        //console.log(name);
        updateBasket(product_id, nmb, is_delete=false)
    });


    function updateBasket(product_id, nmb, is_delete) {
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete) {
            data["is_delete"] = true;
        }
        else {
            data["is_delete"] = false
        }

        $.ajax({
            url: '/basket_adding/',
            type: 'POST',
            data: data,
            cache: true,
            success: function(response) {
                //console.log(response.products_total_nmb);
                //console.log(response)
                if (response.products_total_nmb || response.products_total_nmb == 0) {
                    //console.log("RRR")
                    $('#basket_total_nmb').text("("+response.products_total_nmb+")");
                    //console.log(response.products);
                    $('.basket-items ul').html("");
                    $.each(response.products, function(k, v) {
                        $('.basket-items ul').append(
                            '<li>'+ v.name+', ' + v.nmb + 'шт. '
                            + 'по ' + v.price_per_item + 'руб.  '
                            + '<a class="delete-item" href="" data-product_id="'+v.id+'">&#10006</a>'
                            + '</li>'
                        );
                    });
                }

            },
            error: function() {
                console.log("error")
            }
        })
    }


    $('.basket-container').on('click', function(e) {
        e.preventDefault();
        showBasket();
    });


    $(document).on('click', '.delete-item', function(e) {
        e.preventDefault();
        product_id = $(this).data("product_id")
        nmb = 0;
        updateBasket(product_id, nmb, is_delete=true)
    })


    function calculateBasketAmount(){
        var total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function() {
            total_order_amount = total_order_amount + parseFloat($(this).text());
        });
        $('#total_order_amount').text(total_order_amount.toFixed(2));
    };


    $(document).on('change', ".product-in-basket-nmb", function() {
        var current_nmb = $(this).val();
        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
        var total_amount = parseFloat(current_nmb*current_price).toFixed(2);

        current_tr.find('.total-product-in-basket-amount').text(total_amount);

        calculateBasketAmount();
    });


    calculateBasketAmount();

});

