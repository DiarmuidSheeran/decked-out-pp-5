/* global $ */

// Get the value of the default country dropdown
let countrySelected = $('#id_default_country').val();

// If no country is selected, set its color to a muted tone
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
}

// Listen for changes on the default country dropdown
$('#id_default_country').change(function() {
    // Update the value of countrySelected when a new option is selected
    countrySelected = $(this).val();
    // If no country is selected, set its color to a muted tone; otherwise, set it to black
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});