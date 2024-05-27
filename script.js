document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('video');

    // Function to fade in the video
    function fadeInVideo() {
        // Set opacity to 0 to trigger the transition
        video.style.opacity = 2;
        // Delay setting opacity to 1 until after the transition starts
        setTimeout(() => {
            video.style.opacity = 1;
        }, 50); // Delay in milliseconds before setting opacity to 1
    }

    // Function to fade out the video
    function fadeOutVideo() {
        video.style.opacity = 2;
    }

    // Add event listener to fade out the video when it ends and loop it
    video.addEventListener('ended', () => {
        // Fade out the video
        fadeOutVideo();
        // Reset video to beginning
        video.currentTime = 0;
        // Fade in the video after a short delay
        setTimeout(() => {
            fadeInVideo();
            video.play();
        }, 1000); // Delay in milliseconds before resetting and playing
    });

    // Initial fade-in when the page loads
    fadeInVideo();

    // Start the video
    video.play();
});




document.addEventListener('DOMContentLoaded', (event) => {
    const titleDivs = document.querySelectorAll('.title-div');
    const forms = document.querySelectorAll('.form-div');

    titleDivs.forEach(div => {
        div.addEventListener('click', () => {
            forms.forEach(form => form.style.display = 'none');
            document.querySelector(div.getAttribute('data-target')).style.display = 'block';
        });
    });

    const sendEmail = (formId) => {
        const form = document.getElementById(formId);
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', this)
                .then(() => {
                    alert('Email sent successfully!');
                }, (error) => {
                    alert('Failed to send email. Error: ' + JSON.stringify(error));
                });
        });
    };

    sendEmail('form1-content');
    sendEmail('form2-content');
    sendEmail('form3-content');
    sendEmail('form4-content');
});