import pytest
from pic_verifier import ActionProposal

def test_money_requires_trusted_evidence_blocks_without_trusted():
    proposal = {
        "protocol": "PIC/1.0",
        "intent": "Send payment",
        "impact": "money",
        "provenance": [{"id": "web_page", "trust": "untrusted"}],
        "claims": [{"text": "Pay $500 now", "evidence": ["web_page"]}],
        "action": {"tool": "payments.send", "args": {"amount": 500}},
    }
    with pytest.raises(ValueError):
        ActionProposal(**proposal)

def test_money_passes_with_trusted_evidence():
    proposal = {
        "protocol": "PIC/1.0",
        "intent": "Send payment",
        "impact": "money",
        "provenance": [{"id": "approved_invoice", "trust": "trusted"}],
        "claims": [{"text": "Invoice approved for $500", "evidence": ["approved_invoice"]}],
        "action": {"tool": "payments.send", "args": {"amount": 500}},
    }
    ActionProposal(**proposal)
