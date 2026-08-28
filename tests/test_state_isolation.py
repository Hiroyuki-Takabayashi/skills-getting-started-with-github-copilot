def test_participant_registration_does_not_leak_between_tests(client):
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "temporary@mergington.edu"},
    )

    assert response.status_code == 200
    assert "temporary@mergington.edu" in client.get("/activities").json()["Chess Club"]["participants"]


def test_each_test_starts_with_initial_participants(client):
    participants = client.get("/activities").json()["Chess Club"]["participants"]

    assert participants == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]
