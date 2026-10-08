---
id: "ACQ-28"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-28

WHEN a release of BEACON changes the version of the procedure that extracts items' text or of a procedure that supplies values under ACQ-10 or ACQ-13, BEACON shall make, before the first Collection of each source under that release, a Re-extraction of every item of that source that is not an Erased item and whose latest raw page was collected within [[REDERIVE_HORIZON]] before the release takes effect, other than an item whose Re-extraction under this row fails (ACQ-40).

**Rationale.** A better extraction procedure, or a better procedure for the fields, reaches the items held, not only those collected after it. A change of the renderer is not named: a Re-extraction reads the rendered copy kept at Collection and renders nothing, so a new renderer applies to new Collections only, and a run for it could only confirm what is held. Re-extracting a source's recent items before its first Collection under the release means that the held text a return is compared with was made by the procedures now running, so a difference is a change at the source (ACQ-06). The bound keeps a release's run in proportion as the archive grows; an older item is re-extracted when it returns (ACQ-30), when its source's entry is corrected (ACQ-29) or on the Operator's command (ACQ-31). A release that changes none of these versions makes no Re-extraction under this row.

**Verification.** none yet
