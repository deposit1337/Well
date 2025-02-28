


$(document).on('click','#add-button',function(e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '{% url "basket:basket_add" %}',
        data: {
            itemid : $('#add-button').val(),
            csrfmiddlewaretoken : '{{csrf_token}}',
            action: 'post',
        },
        success: function(json){

        },
        error: function(xhr,errmsg,err){}
     });

})