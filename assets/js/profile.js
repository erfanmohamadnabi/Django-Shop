

//* ____________________ FORM PROFILE START _________________

var forms = document.getElementsByClassName('form_profile');
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

   var status = document.getElementById('status');
   status.style.display = 'flex'
   status.style.opacity = '1'; 

   setTimeout(function() {
    status.style.transition = '1s'
    status.style.opacity = '0'; 
    setTimeout(function() {
        status.style.display = 'none';
    }, 1000);
}, 2000);

}else if(data.error_len){
    var errorlen = document.getElementById('error_len');
    errorlen.style.display = 'flex'
    errorlen.style.opacity = '1'; 
 
    setTimeout(function() {
        errorlen.style.transition = '1s'
     errorlen.style.opacity = '0'; 
     setTimeout(function() {
        errorlen.style.display = 'none';
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

//* ____________________ FORM PROFILE FINISH _________________