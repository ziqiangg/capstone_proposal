---
id: "DLV-21"
type: "requirement"
group: "DLV"
verification: "none"
---
# DLV-21

WHILE delivery is suspended, BEACON shall record each scheduled Delivery as skipped, without sending it then or later.

**Rationale.** A backlog of messages released at resumption would flood recipients. The first Delivery after resumption draws from every Briefing since the last Delivery sent (DLV-09), so the highest-ranked developments of the suspended days can still reach recipients; the rest stay on the web.

**Verification.** none yet
