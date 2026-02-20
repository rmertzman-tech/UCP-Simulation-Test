from datetime import datetime

class Agent:
    def __init__(self, name, identity_kernel, ita_role, prf):
        self.name = name
        self.identity_kernel = identity_kernel
        self.ita_role = ita_role
        self.prf = prf
        self.actions = []
        self.coherence_log = []
        self.narrative_log = []

    def act(self, scenario_input):
        response = f"{self.name} responds to scenario '{scenario_input}' using PRF lens: {self.prf}"
        coherence = self.evaluate_coherence(scenario_input)
        self.actions.append(response)
        self.coherence_log.append((datetime.now(), coherence))
        self.narrative_log.append((datetime.now(), f"{response} with coherence: {coherence}"))
        return {"response": response, "coherence": coherence}

    def evaluate_coherence(self, scenario):
        return round(hash(scenario + self.name) % 100 / 100, 2)

def run_simulation(input_data):
    agents_data = input_data.get("agents", [])
    scenario = input_data.get("scenario", "Unspecified")
    results = []
    for agent_info in agents_data:
        agent = Agent(
            agent_info["name"],
            agent_info["identity_kernel"],
            agent_info["ita_role"],
            agent_info["prf"]
        )
        output = agent.act(scenario)
        results.append({"agent": agent.name, **output})
    return {"scenario": scenario, "results": results}

MODULES = {
    "Ethical Dilemma: Trolley Problem": "A classic PRF-based ethical simulation.",
    "Whistleblower Simulation": "PRF vs ITA tensions explored in institutional settings.",
    "Paradigm Shift and PRF Drift": "Shock-triggered restructuring of belief systems."
}

def load_module(name):
    description = MODULES.get(name, "No description available.")
    return {"module": name, "description": description}

def load_presets():
    return {
        "Instructor": {"hide_advanced_metrics": True, "show_walkthrough": True},
        "Researcher": {"show_energy_cost": True, "log_every_action": True},
        "Practitioner": {"show_impact": True, "focus_mode": True}
    }
