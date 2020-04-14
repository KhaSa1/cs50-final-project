/* I don't own this script but i edit it quite a bit */
/* copied from https://www.formget.com/password-strength-checker-in-jquery/ */

$(() => {
    $('#password').keyup(function() {
    $('#result').html(checkStrength($('#password').val()))
    })
    function checkStrength(password) {
        var strength = 0
        const btn = $('#submit')
        if (password.length == 0) {
            $('#result').hide('fast')
        } else {
            $('#result').show('fast')
        }
        if (password.length < 6) {
            $('#result').removeClass()
            $('#result').addClass('short')
            btn.prop('disabled', true)
            return 'Too short'
        }
        if (password.length > 7) strength += 1
        // If password contains both lower and uppercase characters, increase strength value.
        if (password.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/)) strength += 1
        // If it has numbers and characters, increase strength value.
        if (password.match(/([a-zA-Z])/) && password.match(/([0-9])/)) strength += 1
        // If it has one special character, increase strength value.
        if (password.match(/([!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1
        // If it has two special characters, increase strength value.
        if (password.match(/(.*[!,%,&,@,#,$,^,*,?,_,~].*[!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1
        // Calculated strength value, we can return messages
        // If value is less than 2
        if (strength < 2) {
            $('#result').removeClass()
            $('#result').addClass('weak')
            btn.prop('disabled', true)
            return 'Weak'
        } else if (strength == 2) {
            $('#result').removeClass()
            $('#result').addClass('good')
            btn.prop('disabled', false)
            return 'Good'
        } else {
            $('#result').removeClass()
            $('#result').addClass('strong')
            btn.prop('disabled', false)
            return 'Strong'
        }
    }
});