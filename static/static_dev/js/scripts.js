$(document).ready(function() {
    var form = $('#form_buying_product');
    //console.log(form);


    function updateBasket(product_id, nmb, is_delete) {
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete) {
            data["is_delete"] = true;
        }
        else {
            data["is_delete"] = false
        }

        //console.log(data)
        var url = form.attr("action");

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                //console.log("OK");
                //console.log(data.products_total_nmb);
                if (data.products_total_nmb || data.products_total_nmb == 0) {
                    $('#basket_total_nmb').text("("+data.products_total_nmb+")");
                    //console.log(data.products);
                    $('.basket-items ul').html("");
                    $.each(data.products, function(k, v) {
                        $('.basket-items ul').append('<li>'+ v.name+', ' + v.nmb + 'шт. '
                            + 'по ' + v.price_per_item + 'руб.  '
                            + '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'
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


    function showBasket() {
        $('.basket-items').removeClass('hidden');
    };


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

    //$('.basket-container').on('click', function(e) {
    //    e.preventDefault();
    //    showingBasket();
    //});

     $('.basket-container').mouseover(function() {
         showBasket();
     });

     //$('.basket-container').mouseout(function() {
     //    showBasket();
     //});

     $(document).on('click', '.delete-item', function(e) {
         e.preventDefault();
         product_id = $(this).data("product_id")
         nmb = 0;
         updateBasket(product_id, nmb, is_delete=true)
     })

});

