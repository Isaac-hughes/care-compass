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
  // Hide all panes
  $(".pane").each(function () {
    $(this).removeClass("active");
  });

  // Show the current pane with a slight delay for the transition
  setTimeout(() => {
    $(`.${newPhase}-pane`).addClass("active");
  }, 10); // Small delay to ensure the class addition triggers the transition
};

$(".appointment-type").on("click", function () {
  const selectedAppointmentType = this.textContent;
  appointmentDetails.appointmentType = selectedAppointmentType;
  $(".appointment-type-selected").text(selectedAppointmentType);
  changePhase("date-select");
});

var now = new Date(),
  // minimum date the user can choose, in this case now and in the future
  minDate = now.toISOString().substring(0, 10);

$(".date-input").prop("min", minDate);

$(".date-input").on("change", function () {
  const selectedDate = this.value;
  appointmentDetails.appointmentDate = selectedDate;
  $(".date-selected").text(selectedDate);
  changePhase("time-select");
});

const start = 9;
const end = 16;
const interval = 15;

for (let hour = start; hour <= end; hour++) {
  for (let minute = 0; minute < 60; minute += interval) {
    let timeValue = `${hour.toString().padStart(2, "0")}:${minute
      .toString()
      .padStart(2, "0")}`;
    let amPm = hour >= 12 ? "PM" : "AM";
    let displayTime = `${hour > 12 ? hour - 12 : hour}:${minute
      .toString()
      .padStart(2, "0")} ${amPm}`;
    $("#time-input").append(
      `<option value="${timeValue}">${displayTime}</option>`
    );
  }
}

$(".time-input").on("change", function () {
  const selectedTime = this.value;
  appointmentDetails.appointmentTime = selectedTime;
  $(".initial-option").remove(); // ensures user cannot select placeholder option
  $(".time-selected").text(selectedTime);
  changePhase("contact-number");
});

$(".contact-number-input").on("change", function () {
  let contactNumber = this.value;
  contactNumber = contactNumber.replace(/\s/g, "");
  const ukPhoneNumberRegex = /^(?:(?:\+|00)44|0)7(?:[45789]\d{2}|624)\d{6}$/;
  if (!ukPhoneNumberRegex.test(contactNumber)) {
    $(".contact-number-error").text("Please enter a valid UK phone number.");
    $(".contact-number-input").addClass("error-border");
  } else {
    $(".contact-number-error").text("");
    appointmentDetails.contactNumber = contactNumber;
    if ($(".contact-number-input").hasClass("error-border")) {
      $(".contact-number-input").removeClass("error-border");
    }
    $(".contact-number-selected").text(contactNumber);
    changePhase("additional-info");
  }
});

$(".appointment-submit").on("click", function () {
  const additionalInfo = $(".additional-info-input").val();
  appointmentDetails.additionalInfo = additionalInfo;
  $(".additional-info-selected").text(additionalInfo);
  // Submit form data to Django
  $.ajax({
    type: "POST",
    url: "/appointments/create/",
    data: {
      ...appointmentDetails,
      csrfmiddlewaretoken: $('meta[name="csrf-token"]').attr("content"),
    },
    success: function (response) {
      changePhase("summary");
    },
    error: function (error) {
      console.log("An error occurred.", error);
    },
  });
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
