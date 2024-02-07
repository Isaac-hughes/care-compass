let phase = "appointmentTypeSelect";
const appointmentTypes = ["Telephone", "In Person", "Virtual"];

let appointmentDetails = {
  appointmentType: "",
  appointmentDate: "",
  appointmentTime: "",
  contactNumber: "",
  additionalInfo: "",
};

const changePhase = (newPhase) => {
  phase = newPhase;
  $(".appointment-type-select-pane").hide();
  $(".date-select-pane").hide();
  $(".time-select-pane").hide();
  $(".contact-number-pane").hide();
  $(".additional-info-pane").hide();
  $(`.${newPhase}-pane`).show();
};

$(".appointment-type").on("click", function () {
  const selectedAppointmentType = this.textContent;
  appointmentDetails.appointmentType = selectedAppointmentType;
  $(".appointment-type-selected").text(selectedAppointmentType);
  changePhase("date-select");
});

$(".date-input").on("change", function () {
  const selectedDate = this.value;
  appointmentDetails.appointmentDate = selectedDate;
  $(".date-selected").text(selectedDate);
  changePhase("time-select");
});

$(".time-input").on("change", function () {
  const selectedTime = this.value;
  appointmentDetails.appointmentTime = selectedTime;
  $(".time-selected").text(selectedTime);
  changePhase("contact-number");
});

$(".contact-number-input").on("change", function () {
  const contactNumber = this.value;
  appointmentDetails.contactNumber = contactNumber;
  $(".contact-number-selected").text(contactNumber);
  changePhase("additional-info");
});

$(".appointment-submit").on("click", function () {
  const additionalInfo = $(".additional-info-input").val();
  appointmentDetails.additionalInfo = additionalInfo;
  console.log(appointmentDetails);
  // Submit form data to Django
  $.ajax({
    type: "POST",
    url: "/appointments/create/", // Update this URL to match the Django URL
    data: {
      ...appointmentDetails,
      csrfmiddlewaretoken: $('meta[name="csrf-token"]').attr("content"),
    },
    success: function (response) {
      console.log("Appointment created successfully.", response);
      // Redirect or update the UI as needed
    },
    error: function (error) {
      console.log("An error occurred.", error);
    },
  });
  $(".additional-info-selected").text(additionalInfo);
  changePhase("summary");
});

const resetFields = (fields) => {
  for (let field of fields) {
    switch (field) {
      case "appointmentType":
        appointmentDetails.appointmentType = "";
        $(".appointment-type-selected").text("");
        break;
      case "appointmentDate":
        appointmentDetails.appointmentDate = "";
        $(".date-selected").text("");
        $(".date-input").val("");
        break;
      case "appointmentTime":
        appointmentDetails.appointmentTime = "";
        $(".time-selected").text("");
        $(".time-input").val("");
        break;
      case "appointmentContactNumber":
        appointmentDetails.contactNumber = "";
        $(".contact-number-selected").text("");
        $(".contact-number-input").val("");
        break;
      case "appointmentAdditionalInfo":
        appointmentDetails.additionalInfo = "";
        $(".additional-info-selected").text("");
        $(".additional-info-input").val("");
        break;
      default:
        break;
    }
  }
};

$(".change-appointment-type").on("click", function () {
  changePhase("appointment-type-select");
  resetFields([
    "appointmentType",
    "appointmentDate",
    "appointmentTime",
    "appointmentContactNumber",
    "appointmentAdditionalInfo",
  ]);
});

$(".change-date").on("click", function () {
  changePhase("date-select");
  resetFields([
    "appointmentDate",
    "appointmentTime",
    "appointmentContactNumber",
    "appointmentAdditionalInfo",
  ]);
});

$(".change-time").on("click", function () {
  changePhase("time-select");
  resetFields([
    "appointmentTime",
    "appointmentContactNumber",
    "appointmentAdditionalInfo",
  ]);
});

$(".change-contact-number").on("click", function () {
  changePhase("contact-number");
  resetFields(["appointmentContactNumber", "appointmentAdditionalInfo"]);
});

$(".change-preferred-name").on("click", function () {
  changePhase("contact-number");
  resetFields(["appointmentPreferredName", "appointmentAdditionalInfo"]);
});
