import json
from .triage import triage_incident

SAMPLES = {
    "1": (
        "Deployment / availability",
        "The citizen services portal began returning intermittent HTTP 503 "
        "responses approximately 12 minutes after deployment v3.8.2. Users "
        "can occasionally authenticate, but downstream requests frequently fail.",
    ),
    "2": (
        "Security",
        "Multiple failed administrator login attempts originated from an unfamiliar "
        "IP address, followed by one successful privileged login. No additional "
        "identity or endpoint telemetry is currently available.",
    ),
    "3": (
        "Ambiguous / insufficient evidence",
        "Several users report that the application feels slow today. No latency "
        "metrics, error rates, affected service names, or recent change information "
        "were included in the report.",
    ),
}

def _choose_incident() -> str:
    print("\nChoose an incident:")
    for key, (name, _) in SAMPLES.items():
        print(f"  {key}. {name}")
    print("  4. Enter my own synthetic/public incident")

    choice = input("\nSelection [1-4]: ").strip()
    if choice in SAMPLES:
        return SAMPLES[choice][1]
    if choice == "4":
        incident = input("\nIncident: ").strip()
        if not incident:
            raise ValueError("Incident description cannot be empty.")
        return incident
    print("Invalid selection; using sample 1.")
    return SAMPLES["1"][1]

def main() -> None:
    print("=" * 72)
    print("MISSIONOPS AI v0.1 — API FOUNDATIONS")
    print("Structured incident triage | Human review required")
    print("=" * 72)

    incident = _choose_incident()
    result, elapsed = triage_incident(incident)

    print("\nStructured result:")
    print(json.dumps(result.model_dump(), indent=2))
    print(f"\nLatency: {elapsed:.2f}s")
    print("\nNo production action has been executed.")

if __name__ == "__main__":
    main()
