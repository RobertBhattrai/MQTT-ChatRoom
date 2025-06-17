const brokerUrl = "wss://86e18b0ac6da4172b58085b6b8aa61e9.s1.eu.hivemq.cloud:8884/mqtt";
const topic = "chatroom/general";
const username = "ChatRoomMQTT";
const password = "ChatRoomMQTT123";

const clientId = "user-" + Math.floor(Math.random() * 1000);
const client = mqtt.connect(brokerUrl, {
  username,
  password,
  clientId,
  clean: true,
  connectTimeout: 4000,
  reconnectPeriod: 4000
});

const statusEl = document.getElementById("status");
const chatBox = document.getElementById("chat");
const msgInput = document.getElementById("msg");
const sendBtn = document.getElementById("send");

// MQTT Events
client.on("connect", () => {
  statusEl.textContent = "🟢 Connected";
  client.subscribe(topic, err => {
    if (err) console.error("Subscribe error:", err);
  });
});

client.on("reconnect", () => {
  statusEl.textContent = "🟠 Reconnecting...";
});

client.on("error", () => {
  statusEl.textContent = "🔴 Error";
});

client.on("close", () => {
  statusEl.textContent = "🔌 Disconnected";
});

client.on("message", (_, message) => {
  const { sender, text } = JSON.parse(message.toString());
  const cls = sender === clientId ? "me" : "other";
  const div = document.createElement("div");
  div.className = cls;
  div.innerText = `${sender}: ${text}`;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
});

// Send Message
sendBtn.onclick = () => sendMessage();
msgInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendMessage();
});

function sendMessage() {
  const text = msgInput.value.trim();
  if (!text) return;

  const payload = JSON.stringify({ sender: clientId, text });
  client.publish(topic, payload);
  msgInput.value = "";
}
