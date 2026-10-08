# BEACON status

> Generated 2026-10-08 at a3c475d, vault clean, by `python tools/status.py`. Read by an agent only when the owner asks.
> Regenerated after a commit, checkout, merge or rewrite. Current if the commit above is `git rev-parse --short HEAD`; if not, regenerate it.

## Recent events

| when | event | id | what | commit |
|---|---|---|---|---|
| 2026-10-08 | design | C-09 | Source watch, decomposed | a3c475d |
| 2026-10-08 | design | C-08 | Article record, decomposed | 2da9e60 |
| 2026-10-08 | design | C-07 | Field decision, decomposed | 55b6bfd |
| 2026-10-08 | design | C-06 | Collection, decomposed | a12543b |
| 2026-10-08 | design | C-05 | Page reading, decomposed | 1da819f |
| 2026-10-08 | design | C-04 | Source onboarding and the Source Set, decomposed | 1808356 |
| 2026-10-08 | design | C-03 | Digests, named not decomposed | d3a8b12 |
| 2026-10-08 | design | C-02 | Views, the backend read side, named not decomposed | 1c68c5f |
| 2026-10-08 | design | C-01 | the Cycle, composition root, named not decomposed | f3d67ad |
| 2026-10-08 | method | code | no comments or docstrings in src/; src/ in the map | 3588ecb |
| 2026-10-08 | build | tests | src/ carries no comments or docstrings | ae43dbf |
| 2026-10-06 | ask | Q-018 | where names are held, and the retention purpose | ca0ac26 |
| 2026-10-06 | ask | Q-024 | status words restated; first build measures nothing | f00f10a |
| 2026-10-06 | ask | Q-023 | where a metadata value came from, not its status | a5844b2 |
| 2026-10-06 | ask | Q-020 | restated in Entry parts, Refusal grounds, Drift signs | d83ffc8 |
| 2026-10-06 | ask | Q-022 | restated per set of places, with intervals and route | eedada5 |
| 2026-10-06 | ask | Q-026 | restated to the rows and the scoring rulings | 2917b07 |
| 2026-10-06 | apply | CP-010 | breaches, entry versions, correction; OPS-29 to SRC-42 | 93ce167 |
| 2026-10-06 | rule | CP-010 | the owner accepts the proposal | e11d041 |
| 2026-10-06 | assess | CP-010 | coherent, fourth assessment | f796852 |
| 2026-10-06 | propose | CP-010 | breach counts, entry versions, possible gaps | 1fbbe64 |
| 2026-10-06 | apply | CP-009 | drift rows restructured, no content change | ba9b456 |
| 2026-10-06 | rule | CP-009 | the owner accepts the proposal | 64001d7 |
| 2026-10-06 | assess | CP-009 | coherent, second assessment | 6847941 |
| 2026-10-06 | propose | CP-009 | drift rows restructured, no content change | 27340cc |
| 2026-10-06 | apply | CP-008 | completing without error; COLLECTION_TIMEOUT 60 min | 88dd3ef |
| 2026-10-06 | rule | CP-008 | the owner accepts the proposal | e710d58 |
| 2026-10-06 | assess | CP-008 | coherent, fourth assessment | 8aaf0ba |
| 2026-10-06 | propose | CP-008 | COLLECTION_TIMEOUT and completing without error | e5d275a |
| 2026-10-06 | apply | CP-007 | onboarding and the Curator; adds SRC-22 to SRC-35 | 0c05e5d |


## Proposals

_none_


## Open questions

| id | priority | owner | blocks | title |
|---|---|---|---|---|
| Q-013 | P1 | - | ACQ-04, ACQ-05, ACQ-06, SRC-05 | Item identity within a source |
| Q-008 | P1 | - | ASM-01, MIN_SIGNIFICANCE, ASSESSMENT_TOLERANCE | The assessment criteria and the Significance scale |
| Q-003 | P1 | - | SRC-07, SRC-11 | How BEACON finds candidate sources |
| Q-011 | P1 | - | CTX-06, ASM-05 | The confidence scale and its words |
| Q-018 | P1 | - | PERSONAL_DATA_RETENTION, CONSENT_RECORD_RETENTION | Privacy obligations per class of personal data |
| Q-001 | P1 | - | CTX-08 | Whether a mapping's evidence supports it |
| Q-002 | P1 | - | TRD-04 | Whether the evidence supports a trend |
| Q-006 | P1 | - | REL-01 | The initial Scope Criteria |
| Q-009 | P1 | - | CTX-04 | The approved mapping purposes |
| Q-010 | P1 | - | REL-07 | The labelled evaluation set |
| Q-012 | P1 | - | TRD-02 | Trend identity across windows |
| Q-016 | P1 | - | - | Quality attributes BEACON must meet |
| Q-017 | P1 | - | - | Prompt injection from item text |
| Q-020 | P1 | - | - | How a source's link becomes a checked page-structure configuration |
| Q-022 | P1 | - | - | A reproducible, corroborated Source publication time |
| Q-026 | P1 | - | - | How a source becomes Article Records that meet ACQ-02 |
| Q-014 | P2 | - | DEV-08, DEV-05 | The same text from several sources |
| Q-007 | P2 | - | CLS-03 | The initial subject vocabulary |
| Q-004 | P2 | - | - | Internal uses of OSCAL and STIX |
| Q-015 | P2 | - | - | Export of BEACON's output |
| Q-021 | P2 | - | - | Organisations credited jointly inside an item's body |
| Q-023 | P2 | - | - | How later Stages use where a metadata value came from |
| Q-024 | P2 | - | - | Whether a targeted model call may decide a metadata field |
| Q-025 | P2 | - | - | Correcting an Article Record's metadata, and showing Readers what BEACON supplied |


## Architecture gaps

### Components with no step

| id | title |
|---|---|
| C-01 | Cycle |
| C-02 | Views |
| C-03 | Digests |


### Contracts still undesigned

| id | title | producer | consumers |
|---|---|---|---|
| K-001 | Candidate | S-001 | S-002, S-006 |
| K-002 | Acceptance | S-002 | S-003, S-006 |
| K-003 | Sample | S-003 | S-004, S-005 |
| K-004 | Proposed part | S-004 | S-005 |
| K-005 | Checked part | S-005 | S-006 |
| K-006 | Onboarding outcome or failure report | S-006 | S-007, C-02 |
| K-007 | Source Set entry version | S-007 | S-008, S-009, S-010, S-011, S-012, S-013, S-014, S-015, S-016, S-017, S-019, S-020, S-022, S-024, S-025, S-027, S-030, S-033, S-034, S-035, S-037 |
| K-008 | Evidence log | S-007 | S-033 |
| K-009 | Source state | S-009 | S-008, S-012, S-019, S-033, S-034, S-035, S-037, C-01, C-02 |
| K-010 | Preparing result | S-008 | S-007, C-02, C-03 |
| K-011 | Part result | S-010 | S-004, S-005, S-008, S-011, S-013, S-018, S-020 |
| K-012 | Extraction | S-011 | S-005, S-008, S-017, S-018, S-019 |
| K-013 | Fetched item | S-016 | S-002, S-003, S-008, S-010, S-011, S-017, S-018 |
| K-014 | Field set | S-025 | S-005, S-008, S-017, S-019, S-027 |
| K-015 | Held view | S-029 | S-002, S-013, S-014, S-017, S-019 |
| K-016 | Drift flag | S-033 | S-008, S-038, C-02, C-03 |
| K-017 | Page bundle | S-017 | S-020, S-024, S-025 |
| K-018 | Item return | S-017 | S-018, S-026, S-027, S-028 |
| K-019 | Re-extraction result | S-019 | S-017, S-027 |
| K-020 | Collection log and health counts | S-018 | S-014, S-033, S-034, S-035, S-037, C-02 |
| K-021 | Re-extraction run report | S-019 | S-012, C-02, C-03 |
| K-022 | Kept raw set | S-026 | S-019, S-027, S-029, S-030, S-031 |
| K-023 | Collection plan | S-012 | S-013, S-015, S-018 |
| K-024 | Listing entry | S-013 | S-014, S-018 |
| K-025 | Item reference | S-014 | S-015, S-017, S-018 |
| K-026 | Fetched pages | S-015 | S-016 |
| K-027 | Candidates | S-020 | S-021 |
| K-028 | Normalised values | S-021 | S-022, S-023 |
| K-029 | Publisher credit | S-022 | S-023, S-025 |
| K-030 | Kept values | S-023 | S-024, S-025 |
| K-031 | Supplied values | S-024 | S-025 |
| K-032 | Article Record version | S-027 | S-029, S-030, S-031, S-032, S-033, S-034, S-036, C-02, C-03 |
| K-033 | Record write entry | S-027 | S-033, S-034, S-036, C-02 |
| K-034 | Version reach | S-030 | C-03 |
| K-035 | Erasure entry and log | S-031 | S-026, S-027, S-029, S-030, S-033, C-02, C-03 |
| K-036 | Pending return | S-028 | S-027, S-031 |
| K-037 | Procedure description | S-032 | S-027, S-030 |
| K-038 | Health entry | S-034 | C-02, C-03 |
| K-039 | Source failure state | S-035 | S-038, C-02, C-03 |
| K-040 | Cycle breach counts | S-036 | C-02, C-03 |
| K-041 | Silence notice | S-037 | C-03 |
| K-042 | Keep | S-038 | S-033, S-035 |
| K-043 | Cycle record |  | S-033, S-034, S-036, S-037 |


## Experiments designed, not run

_none_


## Counts

| kind | status | n |
|---|---|---|
| component | proposed | 9 |
| contract | proposed | 43 |
| decision | accepted | 4 |
| experiment | recorded | 5 |
| experiment | superseded | 1 |
| glossary | - | 1 |
| parameter | - | 32 |
| proposal | applied | 10 |
| question | answered | 1 |
| question | open | 24 |
| question | superseded | 1 |
| requirement | - | 288 |
| step | proposed | 38 |
