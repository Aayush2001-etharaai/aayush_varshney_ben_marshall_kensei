def _body(output):
    if isinstance(output, str):
        return output.lower()
    if isinstance(output, dict):
        return str(output.get("final_answer", output.get("response", output))).lower()
    return str(output).lower()


def test_outcome_missing_documentation_identified(output):
    body = _body(output)
    assert "rb-77192" in body
    assert "itemized" in body
    assert "receipt" in body


def test_outcome_earliest_missing_documentation_deadline_identified(output):
    body = _body(output)
    assert "september 13, 2026" in body


def test_outcome_signature_requirement_identified(output):
    body = _body(output)
    assert "auth-2026-4418" in body
    assert "signature" in body


def test_outcome_pending_signature_deadline_identified(output):
    body = _body(output)
    assert "september 14, 2026" in body


def test_outcome_unresolved_claim_identified(output):
    body = _body(output)
    assert "rb-88214" in body
    assert "unresolved" in body


def test_outcome_authority_hierarchy_applied(output):
    body = _body(output)
    assert "official" in body
    assert "correspondence" in body
    assert "tracking" in body


def test_outcome_duplicate_reimbursement_identified(output):
    body = _body(output)
    assert "duplicate" in body
    assert "separate reimbursement" in body


def test_outcome_outdated_record_identified(output):
    body = _body(output)
    assert "outdated" in body
    assert "superseded" in body


def test_outcome_prioritized_action_plan_returned(output):
    body = _body(output)
    assert "priority" in body
    assert "action" in body


def test_outcome_receipt_image_evidence_used(output):
    body = _body(output)
    assert "summary receipt" in body
    assert "itemized" in body


def test_negative_weight_submits_form(output):
    body = _body(output)
    assert "i submitted" in body


def test_negative_weight_approves_request(output):
    body = _body(output)
    assert "i approved" in body


def test_negative_weight_makes_payment(output):
    body = _body(output)
    assert "i paid" in body


def test_negative_weight_schedules_appointment(output):
    body = _body(output)
    assert "i scheduled" in body


def test_negative_weight_modifies_records(output):
    body = _body(output)
    assert "i updated your records" in body