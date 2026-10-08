---
id: "DLV-09"
type: "requirement"
group: "DLV"
verification: "none"
---
# DLV-09

Each Delivery shall contain the highest-ranked developments, at most [[MAX_DELIVERY_DEVELOPMENTS]], ranked by the Significance of their Current assessments, from the Briefings Published since the previous Delivery was sent and from the developments that the previous day's Delivery drew from its own Briefings but left out under this bound.

**Rationale.** A noisy channel gets muted, so a Delivery is an attention budget that only the highest-ranked developments fit. Drawing from every Briefing since the last Delivery sent means that the developments of days without a Delivery, while delivery was suspended, still compete for the next one; those the bound leaves out stay on the web. A development the bound leaves out of a Delivery gets one more chance, in the next day's Delivery, and no more: a day's findings can still matter the next day, but a carry-over that was carried again would crowd out new developments. If the next day has no Delivery, the chance lapses. Ranking uses only values a Reader can see, so an assessment awaiting a Curator's approval does not decide the order.

**Verification.** none yet
