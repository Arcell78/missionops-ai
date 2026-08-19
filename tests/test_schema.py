from missionops.schemas import IncidentTriage

def test_valid_incident_triage():
    result = IncidentTriage(
        category="deployment",
        severity="high",
        escalation_required=True,
        recommended_action="investigate",
        rationale="Errors began after deployment.",
        confidence=0.9,
        missing_information=["application logs"],
    )
    assert result.category == "deployment"
    assert result.severity == "high"
    assert 0 <= result.confidence <= 1
