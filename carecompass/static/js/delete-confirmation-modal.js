$(".delete-btn").on("click", function () {
  console.log("click reg");
  const appointmentId = $(this).data("appointment-id");
  $("#deleteModal" + appointmentId).show();
});

$(".close, .close-btn").on("click", function () {
  $(this).closest(".modal-backdrop").hide();
});

// closes modal when user clicks outside of modal
$(window).on("click", function (event) {
  if ($(event.target).hasClass("modal-backdrop")) {
    $(event.target).hide();
  }
});
