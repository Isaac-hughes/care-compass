$(".email").on("change keyup paste", function (e) {
  let cursorPosition = e.target.selectionStart;

  $(this).val($(this).val().toLowerCase());

  e.target.selectionStart = e.target.selectionEnd = cursorPosition;
});
