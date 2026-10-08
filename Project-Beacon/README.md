1. Project-Beacon\beacon_notes is an obsidian vault of up-to-date beacon information covering:

Project-Beacon\beacon_notes\architecture
Project-Beacon\beacon_notes\architecture\components
Project-Beacon\beacon_notes\architecture\contracts
Project-Beacon\beacon_notes\architecture\steps

Project-Beacon\beacon_notes\decisions

Project-Beacon\beacon_notes\experiments

Project-Beacon\beacon_notes\proposals

Project-Beacon\beacon_notes\questions

Project-Beacon\beacon_notes\requirements
Project-Beacon\beacon_notes\requirements\parameters
Project-Beacon\beacon_notes\requirements\A-terms.md

NOTE: Project-Beacon\Beacon_Report.docx was a separate initial draft made awhile ago, it is outdated. Refer to it for contextual information and understanding of project beacon only. 

To note:
| Band | Means |
|---|---|
| **P0** | The work that is next cannot be settled correctly until this is answered, and `blocks` names the node it would settle |
| **P1** | It shapes work about to start, and that work can proceed under a recorded assumption |
| **P2** | Real, and the fallback in *If it stays unknown* is costing nothing yet |

| Written as a note | Derived, never written | Not in the vault |
|---|---|---|
| component, step, contract | data flow (producer to consumers: `architecture.base`) | prompts, schemas as code, runtime logs -- implementation artefacts; the vault holds the *decisions* about them |
| a contract's `## Shape`, `## Invariants` and `## Failure` | whether a contract crosses components (its producer's and consumers' components) | |


2. Project-Beacon\security_frameworks refer to Project-Beacon\security_frameworks\README.md for context