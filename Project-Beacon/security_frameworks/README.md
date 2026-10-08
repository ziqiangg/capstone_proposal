# security_frameworks

Exploration material for acquiring framework data. Not part of any pipeline.

## How to run

Create a Python virtual environment outside this repository, then:

```
<venv python> -m pip install -r security_frameworks/.env-framework
```

Run each notebook with `security_frameworks/` as the working directory — every
notebook checks its own working directory and raises if launched from
elsewhere. Google Colab support remains in the code (each notebook detects
Colab and, on Colab, writes into `/content/security_frameworks` instead).
Network access is required: every notebook fetches from a live site, clones a
GitHub repository, or calls the GitHub API.

## Per notebook

### SSP_exploration

- **Corpus.** The Singapore Government's "System Security Plan (SSP)" control
  set, published on `info.standards.tech.gov.sg` (Singapore Government
  ICT&SS Policy Reform site). The site presents a **control catalog** plus, per
  system type, a selection of those controls at a level — in OSCAL terms a
  catalog and a set of profiles. Level 0 is "cardinal and mandatory", Level 1
  is "basic hygiene", Level 2 is optional "best practices" (site text).
- **Source.** `https://info.standards.tech.gov.sg/ssp/` (system types and
  level definitions) and `https://info.standards.tech.gov.sg/control-catalog/`
  (catalogs, domains, controls).
- **Method.** Discovery + parsing: the notebook discovers catalog slugs and
  domain codes from the site's own index pages (rather than assuming which
  exist), then scrapes each domain page and each system-type page with
  BeautifulSoup, using the page's heading structure (`h1`/`h2`/`h3`) as text
  landmarks. Control-catalog pages: `h2` = control id, `h3` = section label.
  System-type profile pages: `h2` = domain group, `h3` = control id, `h4`
  (via full paragraph text) = section label.
- **Writes.** To `SSP_output/`: `controls.json`, `domains.json`,
  `system-types.json`, `level-definitions.json`, `baselines.json` (the
  system-type profiles, under the site's own name), each both
  in a dated snapshot folder and as a flat `SSP-<name>-latest.json`, plus
  `manifest.json` (source URLs, retrieval time, snapshot folder, per-domain
  and per-catalog counts, per-system-type counts, sha256 per file).
- **Version tracking / pin.** The notebook reads no version number from the
  site; it uses the UTC retrieval date (`YYYY-MM-DD`) as the snapshot key. There is no PIN parameter for this
  notebook — each run fetches whatever the live site currently shows.
- **Failure behaviour.** Raises if: zero controls are scraped in total; a
  discovered domain yields zero controls; the `/control-catalog/` index
  yields no catalogs; the "Control Levels" section cannot be found on the
  `/ssp/` page; a system-type page yields zero profile entries, or a
  control heading has no following "Profile Level:" paragraph, or that value
  is non-numeric; a profile entry references a control id not found in any
  discovered domain; or the final manifest's total-control count is 0.
- **Measured results, 2026-09-23.** 248 controls across 26 domains in 2
  catalogs (cybersecurity 156, dss 92); 8 system types; 3 level definitions;
  784 profile memberships validated against the 248 catalog controls; 39
  HTTP requests, 0 404s. Per-domain counts: AC 16, AS 15, BR 6, CK 4, CS 11,
  DC 2, DP 8, GA 8, HR 3, IS 14, LM 21, NS 11, PM 10, RS 3, SC 9, SD 10, ST 5,
  BD 9, PR 7, TL 6, TX 15, UU 2, WO 18, WP 19, WR 2, WU 14. Field coverage:
  `levels` 242/248, `parameters` 42/248, `rationale` 92/248, `risk` 156/248;
  all other fields 248/248. Profile membership per system type (total,
  by level):
  | System type | Total | L0 | L1 | L2 |
  |---|---|---|---|---|
  | dss-high | 92 | 3 | 82 | 7 |
  | dss-others | 92 | 3 | 73 | 16 |
  | gen-ai | 9 | 4 | 5 | 0 |
  | high-risk-cloud | 137 | 61 | 60 | 16 |
  | low-risk-cloud | 117 | 7 | 78 | 32 |
  | low-risk-on-premises | 103 | 7 | 68 | 28 |
  | medium-risk-cloud | 117 | 26 | 68 | 23 |
  | sandbox | 117 | 3 | 0 | 114 |
- **Known characteristics.** 6 controls belong to no profile. Levels are
  per system type: the same control can carry a different profile level
  under different system types.

### MITRE_ATTACK_git_exploration

- **Corpus.** MITRE ATT&CK, published by the MITRE Corporation: Enterprise,
  ICS and Mobile domains, as STIX 2.1 bundles.
- **Source.** `https://github.com/mitre-attack/attack-stix-data.git`.
- **Method.** Download via `git clone --depth 1` (or fetch + hard reset to
  the remote default branch on a re-run); the bundles themselves are read
  directly from the clone, not regenerated.
- **Writes.** To `MITRE_ATTACK_output/`: a flat copy per domain
  (`enterprise-attack.json`, `ics-attack.json`, `mobile-attack.json`) plus
  versioned copies under `<version>/` (a single shared folder if all three
  domains report the same `x_mitre_version`, otherwise
  `<version>/<domain-folder>/` per domain), and `manifest.json` (repo URL,
  git commit, pin, retrieval time, and per-domain file path, version,
  sha256 and object counts).
- **Version tracking / pin.** `PIN` (a release string, e.g. `"17.1"`) selects
  the versioned per-release file `<domain>-attack-<PIN>.json` instead of the
  unversioned `<domain>-attack.json`; when `PIN` is `None`, the unversioned
  file (the repo's moving pointer to its current release) is used. Each
  domain's actual version is read from its bundle's `x-mitre-collection`
  object, not assumed from the PIN.
- **Failure behaviour.** Raises if: Git is not on PATH; a PIN is requested
  but the clone has no versioned per-release files, or the pinned file does
  not exist for a domain; a bundle has no `x-mitre-collection` object or that
  object has no `x_mitre_version`; or a domain's bundle counts zero
  techniques.
- **Measured results, 2026-09-23.** Git commit `6cda5ad8462c79e14fbb872f4e09059b18e0cfc4`.
  All three domains share version 19.2 (shared version layout). Per-domain
  counts:
  | Domain | Technique | Sub-technique | Tactic | CoA | Intrusion set | Malware/tool | Campaign | Data source | Revoked | Deprecated |
  |---|---|---|---|---|---|---|---|---|---|---|
  | enterprise | 365 | 493 | 15 | 268 | 191 | 828 | 56 | 38 | 157 | 289 |
  | ics | 100 | 18 | 12 | 52 | 16 | 30 | 9 | 17 | 11 | 37 |
  | mobile | 143 | 47 | 14 | 15 | 22 | 127 | 3 | 6 | 55 | 25 |
- **Known characteristics.** Each domain's bundle carries its own
  `x_mitre_version`; in this run all three reported 19.2, so one shared
  `<version>/` folder was used.

### MITRE_ATLAS_git_exploration

- **Corpus.** MITRE ATLAS ("Adversarial Threat Landscape for AI Systems"),
  published by the MITRE Corporation: adversary tactics, techniques,
  mitigations and case studies targeting AI systems.
- **Source.** `https://github.com/mitre-atlas/atlas-data.git`; the notebook
  reads the `dist/` release YAML and regenerates STIX with the repo's own
  `tools/atlas_to_stix.py` (run via `uv run`, after `uv sync`).
- **Method.** Clone/update via `git`, then generation: the release YAML is
  converted to STIX 2.1 with `atlas_to_stix.py`, once for ATLAS alone and
  once with `--include-attack` for a combined ATLAS + ATT&CK Enterprise
  bundle.
- **Writes.** To `MITRE_ATLAS_output/<content-version>/`: the source YAML,
  `ATLAS-STIX-<version>.json`, `ATLAS-ATTACK-Enterprise-STIX-<version>.json`,
  each also copied flat as `*-latest.json` in `MITRE_ATLAS_output/`, plus
  `manifest.json` (repo, git commit, pin, content/format version, retrieval
  time, per-file sha256, counts, and full id lists per object type).
- **Version tracking / pin.** `dist/manifest.yaml` in the clone is the
  release index: each entry lists a release string and its dist file(s),
  newest first. `PIN` (a release string, e.g. `"2026.08"`) selects that
  entry and raises if not listed; `None` selects the newest entry. Within a
  release, the dist file with the highest `format-version` is used. The
  manifest also records full id lists (not just counts) per object type,
  because ATLAS has no deprecation marker, so a vanished id between releases
  can only be found by diffing id lists across manifest versions.
- **Failure behaviour.** Raises if: `dist/manifest.yaml` is missing or
  empty; a pinned release string is not listed (lists the available releases
  in the error); the selected release lists no dist files; the resolved
  dist file does not exist; the YAML does not parse to a mapping, or is
  missing `collection.version` or `format-version`; the STIX generator script
  is missing; or the generated ATLAS STIX bundle contains zero techniques.
- **Measured results, 2026-09-23.** Git commit
  `3259f388d19cbcca11bacf12a0ef97f4198f711b`. Content version `2026.09`,
  format version `6.0.0`. Counts: 16 tactics, 208 techniques, 40
  mitigations, 73 case studies.
- **Known characteristics.** ATLAS has no deprecation marker, so ids must be
  compared across manifest versions to detect removals. The repo's
  `ATLAS-latest.yaml` symlinks are one-line placeholder files on a checkout
  without symlink support (e.g. Windows); the notebook resolves the release
  to fetch via `dist/manifest.yaml` instead of reading those symlinks.

### OSCAL_git_exploration

- **Corpus.** OSCAL (Open Security Controls Assessment Language) JSON
  schemas, published by NIST: hierarchical XML/JSON/YAML formats for
  representing the publication, implementation and assessment of security
  controls, across nine models (assessment-plan, assessment-results,
  catalog, complete, component, mapping, poam, profile, ssp).
- **Source.** The GitHub REST API for `usnistgov/OSCAL` releases
  (`/releases/latest` or `/releases/tags/<PIN>`), reading each release's
  attached `oscal_<model>_schema.json` assets directly — the schemas are
  downloaded prebuilt from the release, not built from source.
- **Method.** Download: resolves a release via the GitHub API, then
  downloads each of the nine `oscal_<model>_schema.json` assets by URL.
- **Writes.** To `OSCAL_output/`: a flat copy of each downloaded schema, a
  copy under `<release-tag>/`, and `manifest.json` (repo, release tag,
  published time, retrieval time, pin, per-asset source URL/sha256/paths,
  and any models missing from the release).
- **Version tracking / pin.** `PIN` (a release tag, e.g. `"v1.1.3"`) resolves
  that specific tagged release via the GitHub API instead of `/releases/latest`;
  the resolved tag is recorded in `manifest.json` as `release_tag`.
- **Failure behaviour.** Raises if: the GitHub API call to resolve the
  release does not return HTTP 200; downloading a schema asset does not
  return HTTP 200; or none of the nine expected schema assets are found on
  the resolved release (a partial miss is logged as `missing_models` in the
  manifest rather than raising, as long as at least one schema downloaded).
- **Measured results, 2026-09-23.** Release tag `v1.2.3`, published
  2026-08-07. All 9 / 9 schemas downloaded successfully (assessment-plan,
  assessment-results, catalog, complete, component, mapping, poam, profile,
  ssp).
- **Known characteristics.** A model whose schema is not attached to the
  resolved release is recorded in `missing_models`; this run's release
  (v1.2.3) had all nine.

## Publishers and licensing (external, verified 2026-09-23)

- SSP: Singapore Government ICT&SS Policy Reform site,
  `https://info.standards.tech.gov.sg/ssp/`.
- OSCAL: developed by NIST (National Institute of Standards and Technology)
  through a public, collaborative process — `https://github.com/usnistgov/OSCAL`.
- MITRE ATT&CK: published by the MITRE Corporation as STIX 2.1 collections,
  under MITRE ATT&CK Terms of Use (attack.mitre.org) —
  `https://github.com/mitre-attack/attack-stix-data`.
- MITRE ATLAS: published and maintained by the MITRE Corporation, "Approved
  for Public Release; Distribution Unlimited" —
  `https://github.com/mitre-atlas/atlas-data`.

## Tracked vs gitignored paths

| Path | What it is | Tracked |
|---|---|---|
| `*_git_exploration.ipynb`, `SSP_exploration.ipynb` | how each corpus is obtained | yes |
| `.env-framework` | pip requirements for the throwaway venv | yes |
| `README.md` | this file | yes |
| `SSP_output/` `MITRE_ATTACK_output/` `MITRE_ATLAS_output/` `OSCAL_output/` | the acquired bundles, snapshots and manifests | no |
| `MITRE_ATTACK/` `MITRE_ATLAS/` | upstream clones the notebooks make | no |
