$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  success: function (result) {
    $('DIV#hello').text(result.hello);
  }
});
