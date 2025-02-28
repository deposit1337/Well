let formSubmitted = false;

function sendMail(event) {
    if (event) {
        event.preventDefault();
    }

    if (formSubmitted) {
        return;
    }

    let name = document.getElementById('fullname').value;
    let email = document.getElementById('email').value;
    let phone = document.getElementById('phone').value;
    let city = document.getElementById('city').value;

    if (name.trim() === '' || !validateEmail(email) || !validatePhoneNumber(phone)) {
        alert('Пожалуйста, заполните форму корректно.');
        return;
    }

    formSubmitted = true;

    let parms = {
        name: name,
        email: email,
        phone: phone,
        city: city,
        message: name,
    }

    emailjs.send('service_tjape4b', 'template_7yg7f4t', parms)
        .then(() => {
            alert('email sent!');
            formSubmitted = false;
        });
}

function validateEmail(email) {
    const re = /\S+@\S+\.\S+/;
    return re.test(String(email).toLowerCase());
}

function validatePhoneNumber(phone) {
    const re = /^\d{11}$/;
    return re.test(phone);
}

document.querySelector('.sub-btn').addEventListener('click', sendMail);
