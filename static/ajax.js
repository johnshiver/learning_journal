$(document).ready(function() {
  $('.add_entry').on('submit', function(event) {
    event.preventDefault();
    $.ajax('/add', {
      type: 'POST',
      data: $('form').serialize(),
      success: function(data) {
        $('.new').html(data);
        $('.add_entry').remove();

      }
    });
  });
});

$(document).ready(function() {
  $('.edit_entry').on('submit', function(event) {
    event.preventDefault();
    $.ajax('/update/{{ entry[0] }}', {
      type: 'POST',
      data: $('form').serialize(),
      success: function(data) {
        $('.new').html(data);
        $('.add_entry').remove();

      }
    });
  });
});