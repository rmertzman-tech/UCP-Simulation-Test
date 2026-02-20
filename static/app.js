document.getElementById("loadPresetBtn").onclick = async () => {
  const role = document.getElementById("roleSelect").value;
  const res = await fetch("/presets");
  const presets = await res.json();
  alert("Loaded preset for: " + role + "\n" + JSON.stringify(presets[role], null, 2));
};

document.getElementById("moduleSelect").onchange = async (e) => {
  const moduleName = e.target.value;
  const res = await fetch("/load_module", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name: moduleName })
  });
  const data = await res.json();
  document.getElementById("moduleDescription").textContent = data.description;
};

document.getElementById("simulateBtn").onclick = async () => {
  const scenario = document.getElementById("moduleSelect").value;
  const agentInput = document.getElementById("agentInput").value;
  let agents;
  try {
    agents = JSON.parse(agentInput);
  } catch (err) {
    alert("Invalid JSON for agents");
    return;
  }
  const res = await fetch("/simulate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ scenario, agents })
  });
  const result = await res.json();
  document.getElementById("output").textContent = JSON.stringify(result, null, 2);
};
