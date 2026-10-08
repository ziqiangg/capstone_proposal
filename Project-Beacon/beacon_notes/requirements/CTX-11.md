---
id: "CTX-11"
type: "requirement"
group: "CTX"
verification: "none"
---
# CTX-11

WHEN a Curator activates a Baseline, BEACON shall report to the Curator each held mapping whose framework item is absent, revoked, deprecated or changed in that Baseline, relative to the Baseline the mapping was made against.

**Rationale.** ATT&CK marks revocation. ATLAS and the SSP mark nothing, so BEACON must compare the stored Baselines. Re-pointing a mapping is never automatic; any re-derivation goes through FBK-06.

**Verification.** none yet
