let recognition;
let isListening = false;
let fullText = "";
let lastText = "";

//START
function startMic() {

  if (!('webkitSpeechRecognition' in window)) {
    alert("Use Chrome!");
    return;
  }

  if (isListening) return;

  fullText = "";
  lastText = "";

  recognition = new webkitSpeechRecognition();
  recognition.continuous = true;
  recognition.interimResults = false;
  recognition.lang = "en-IN";

  recognition.onstart = () => {
    isListening = true;
  };

  recognition.onresult = (event) => {
    let result = event.results[event.results.length - 1];

    if (!result.isFinal) return;

    let text = result[0].transcript.toLowerCase().trim();

    if (text === lastText) return;
    lastText = text;

    fullText += text + " ";

    document.getElementById("liveText").innerText = fullText;
  };

  //AUTO RESTART (fix no speech issue)
  recognition.onend = () => {
    if (isListening) {
      recognition.start(); // restart automatically
    }
  };

  recognition.onerror = (event) => {
    console.log("Error:", event.error);
  };

  recognition.start();
}


// STOP (ONLY HERE RESULT SHOW)
function stopMic() {

  if (recognition) {
    isListening = false;
    recognition.stop();
  }

  fetch("/analyze_text", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text: fullText.trim() })
  })
  .then(res => res.json())
  .then(data => {

    let statusEl = document.getElementById("liveResult");
    statusEl.innerText = data.status;

    statusEl.className =
      data.status.includes("Scam") ? "scam" :
      data.status.includes("Suspicious") ? "suspicious" : "safe";

    document.getElementById("riskScore").innerText = data.risk + "%";

    let list = document.getElementById("reasonList");
    list.innerHTML = "";

    data.reasons.forEach(r => {
      let li = document.createElement("li");
      li.innerText = r;
      list.appendChild(li);
    });
  })
  .catch(err => console.error(err));
}


//RESET
function resetAll() {
  fullText = "";
  lastText = "";

  document.getElementById("liveText").innerText = "";
  document.getElementById("liveResult").innerText = "";
  document.getElementById("riskScore").innerText = "";
  document.getElementById("reasonList").innerHTML = "";

  if (recognition) {
    isListening = false;
    recognition.stop();
  }
}