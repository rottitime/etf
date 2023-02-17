$(document).ready(function() {
  $(document).foundation();
});

$(document).ready(function() {
    $('#search_phrase').keypress(function(e) {
      if (e.which == 13) {
        $(this).closest('form').submit();
      }
    });
  });