function sendmail() {
  var params = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    message: document.getElementById("message").value,
  };
  const serviceId = "service_4fiu4kl";
  const templateId = "template_ll9dqth";
  const publicKey = "MTQgE0u8nxJFmCDgZ";

  emailjs.send(serviceId, templateId, params, publicKey).then(res => {
      document.getElementById("name").value = "";
      document.getElementById("email").value = "";
      document.getElementById("message").value = "";
      console.log(res);
      alert("Thanks! I got your message.");
    })
    .catch(err => console.log(err));
}


