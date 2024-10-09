

//* PRODUCT LIKE SCRIPT

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
    if (data.success === 'success') {
        $('.success-send').fadeIn().css("display", "flex"); // فقط fadeIn

        setTimeout(function() {
            $('.success-send').fadeOut(); // fadeOut بعد از 4 ثانیه
        }, 4000);

        $(".success-send img").click(function() {
            $(".success-send").fadeOut();
        });
                                
        
    } else if(data.error === "error"){
        $('.error-send').fadeIn().css("display", "flex"); // فقط fadeIn

        setTimeout(function() {
            $('.error-send').fadeOut(); // fadeOut بعد از 4 ثانیه
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

//* PRODUCT LIKE SCRIPT