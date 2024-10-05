
//* _______________  CONTACT DETAIL COMMENT _____________

var forms = document.getElementsByClassName('contact_form');
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
if (data.success) {


    //! _____ REMOVE INPUTS & TEXTAREA VALUE ____

    var contactForm = document.querySelector('.contact_form');

    var inputs = contactForm.querySelectorAll('input[type="text"], input[type="email"]');
    inputs.forEach(function(input) {
        input.value = '';
    });

    var textareas = contactForm.querySelectorAll('textarea');
    textareas.forEach(function(textarea) {
        textarea.value = '';
    });

    //! _____ REMOVE INPUTS & TEXTAREA VALUE _____

    var success = document.getElementById('success');
    success.style.display = 'flex'
    success.style.opacity = '1'; 
 
    setTimeout(function() {
    success.style.transition = '1s'
    success.style.opacity = '0'; 
     setTimeout(function() {
    success.style.display = 'none';
     }, 1000);
 }, 2000);
 
}else if(data.error){

    var error = document.getElementById('error');
    error.style.display = 'flex'
    error.style.opacity = '1'; 
 
    setTimeout(function() {
        error.style.transition = '1s'
        error.style.opacity = '0'; 
     setTimeout(function() {
        error.style.display = 'none';
     }, 1000);
 }, 2000); 

}

})
.catch(error => {
console.error('خطا:', error);
});
    });
}


//* _______________  CONTACT DETAIL COMMENT _____________








//* _______________  WEBLOG DETAIL COMMENT _____________


var forms = document.getElementsByClassName('comment_weblog');
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
if (data.success) {
    var textinput = document.getElementById('comment_textarea')
    var status = document.getElementById('success')
    status.style.display = 'flex'
    status.style.opacity = '1'; 
    textinput.value = '';
    setTimeout(function() {
        status.style.transition = '1s'
        status.style.opacity = '0'; 
        setTimeout(function() {
            status.style.display = 'none';
        }, 1000);
    }, 2000);
}else if(data.error){
    var textinput = document.getElementById('comment_textarea')
    var error = document.getElementById('error')
    error.style.display = 'block'
    error.style.opacity = '1'; 
    textinput.value = '';
    setTimeout(function() {
        error.style.transition = '1s'
        error.style.opacity = '0'; 
        setTimeout(function() {
            error.style.display = 'none';
        }, 1000);
    }, 2000);
}

})
.catch(error => {
console.error('خطا:', error);
});
    });
}


//* _______________  WEBLOG DETAIL COMMENT _____________


