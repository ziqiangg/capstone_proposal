---
id: "DLV-19"
type: "requirement"
group: "DLV"
verification: "none"
---
# DLV-19

IF the delivery channel revokes BEACON's access, refuses every send of a Delivery after its retries, or, in each of [[CHANNEL_REFUSAL_LIMIT]] consecutive Deliveries, refuses after its retries a send to a recipient who has not blocked the bot, THEN BEACON shall notify every Operator.

**Rationale.** Revoked access or a wholly refused Delivery stops the Delivery for every recipient, so the Operator has to act before the next one. Refusals that recur Delivery after Delivery, such as the channel limiting how fast BEACON sends, point to a problem with BEACON's sending rather than with any one recipient, and can grow; the Operator is told once they persist, not only through each day's digest (OPS-13). A recipient who blocks the bot has opted out (DLV-05), and one recipient's repeated failures pause that recipient (DLV-17).

**Verification.** none yet
