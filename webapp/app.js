
const API_URL =
  "https://hmbtwop1gh.execute-api.eu-west-1.amazonaws.com/production/submit";

const form = document.getElementById("submission-form");
const statusMessage = document.getElementById("status");
const submitButton = document.getElementById("submit-button");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const name = document.getElementById("name").value.trim();
  const message = document.getElementById("message").value.trim();

  if (!name || !message) {
    statusMessage.textContent = "Please enter your name and message.";
    return;
  }

  submitButton.disabled = true;
  statusMessage.textContent = "Sending your message...";

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name, message })
    });

    const result = await response.json();

    if (!response.ok) {
      throw new Error(result.message || `Request failed (${response.status})`);
    }

    statusMessage.textContent =
      `Success! Your message was received. Reference: ${result.id || "received"}`;

    form.reset();
  } catch (error) {
    console.error("Submission error:", error);
    statusMessage.textContent =
      "Could not submit your message. Please try again.";
  } finally {
    submitButton.disabled = false;
  }
});
