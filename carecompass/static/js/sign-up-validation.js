const validateEmailAddress = (email) => {
  if (email.length > 0) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
  }
  return true;
};

const nameValidation = (name) => {
  if (name.length > 0) {
    const namePattern = /^[a-zA-Z\s]*$/;
    return namePattern.test(name);
  }
  return true;
};

$("#id_email").blur(function () {
  const email = $(this).val();
  if (!validateEmailAddress(email)) {
    $("#email-error").text("Please enter a valid email address.");
  } else {
    $("#email-error").text(""); // Clear the error message
  }
});

$("#id_first_name").blur(function () {
  const name = $(this).val();
  if (!nameValidation(name)) {
    $("#first-name-error").text("Please enter a valid name.");
  } else {
    $("#first-name-error").text(""); // Clear the error message
  }
});

$("#id_last_name").blur(function () {
  const name = $(this).val();
  if (!nameValidation(name)) {
    $("#last-name-error").text("Please enter a valid name.");
  } else {
    $("#last-name-error").text(""); // Clear the error message
  }
});

// on submit, validate all fields
$("#sign-up-form").submit(function (event) {
  const email = $("#id_email").val();
  if (!validateEmailAddress(email) || email.length === 0) {
    event.preventDefault();
    $("#email-error").text("Please enter a valid email address.");
  }
  const firstName = $("#id_first_name").val();
  if (!nameValidation(firstName) || firstName.length === 0) {
    event.preventDefault();
    $("#first-name-error").text("Please enter a valid name.");
  }
  const lastName = $("#id_last_name").val();
  if (!nameValidation(lastName) || lastName.length === 0) {
    event.preventDefault();
    $("#last-name-error").text("Please enter a valid name.");
  }
});
