$(document).ready(function() {
    $('#commentForm').submit(function(event) {
        event.preventDefault();
        let form = $(this);
        let url = form.attr('action');
        let formData = form.serialize();
        
        $.ajax({
            type: 'POST',
            url: url,
            data: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
            success: function(response) {
                $('#comments').append('<p><strong>' + response.user + '</strong>: ' + response.text + ' (' + response.created_at + ')</p>');
                form[0].reset();
            },
            error: function(response) {
                alert('An error occurred. Please try again.');
            }
        });
    });
});
