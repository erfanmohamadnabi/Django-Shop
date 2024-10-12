

//* PRODUCT LIKE AND ADD TO ORDER SCRIPT

var forms = document.getElementsByClassName('like-form');
for (var i = 0; i < forms.length; i++) {
    forms[i].addEventListener('submit', function(event) {
        event.preventDefault();
            
        var form = event.target;
        var url = form.getAttribute('action');
        var method = form.getAttribute('method');
        var formData = new FormData(form);
            
    fetch(url, {
method: method,
body: formData
})
.then(response => response.json())
.then(data => {
    if (data.add_like === 'success') {

        $('.success-send').fadeIn().css("display", "flex"); 
        $('.success-send span').text("با موفقیت به علاقه مندی ها اضافه شد.")

        setTimeout(function() {
            $('.success-send').fadeOut();
        }, 4000);

        $(".success-send img").click(function() {
            $(".success-send").fadeOut();
        });
                                
        
    }else if(data.add_cart === 'success'){

        $('.success-send').fadeIn().css("display", "flex"); 
        $('.success-send span').text("با موفقیت به سبد خرید اضافه شد.")

        setTimeout(function() {
            $('.success-send').fadeOut(); 
        }, 4000);

        $(".success-send img").click(function() {
            $(".success-send").fadeOut();
        });

        
    } else if(data.error === "error"){
        $('.error-send').fadeIn().css("display", "flex"); 
        $('.error-send span').text("خطا : برای  انجام درخواست وارد شوید !!!")

        setTimeout(function() {
            $('.error-send').fadeOut(); 
        }, 4000);

        $(".error-send img").click(function() {
            $(".error-send").fadeOut();
        });
    }
})
.catch(error => {
    console.error('خطا:', error);
});
    });
}

//* PRODUCT LIKE AND ADD TO ORDER SCRIPT


