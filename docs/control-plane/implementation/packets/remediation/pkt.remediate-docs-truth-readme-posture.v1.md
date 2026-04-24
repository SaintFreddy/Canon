# pkt.remediate-docs-truth-readme-posture.v1

- **Packet ID**: `pkt.remediate-docs-truth-readme-posture.v1`
- **Authority**: combined — DEC-RO-04 (LICENSE) + multiple recorded decisions from CF-0093 / CF-0094 / CF-0095 / CF-0096 affecting documented posture
- **Scope**: `SaintFreddy/agentic-engine` README.md + `docs-truth release-posture` guard + related posture-facing text
- **Ordering**: Depends on `pkt.add-proprietary-license.v1` landing (so README can reference LICENSE). Independent of quarantine packets. Can parallelize with them once LICENSE lands.
- **Execution mode**: Autonomous via `droid-issue-exec.yml`

## Goal

Bring the `agentic-engine` public-facing README and the docs-truth release-posture guard into alignment with the recorded decisions that emerged from the reopen remediation wave. The `pkt.remediate-engine-version-0.1.0.v1` PR noted that the docs-truth guard was currently red because of a prior README rewrite (commit `35a0252`) that did not reflect current posture; this packet fixes that honestly rather than suppressing the guard.

## Authoritative posture this packet must encode

- **LICENSE**: Proprietary / All Rights Reserved per DEC-RO-04. README LICENSE section must link to the newly-added `LICENSE` file at repo root; must not claim open-source posture.
- **Engine version**: 0.1.0 per DEC-RO-03 / condition e.1. README must state current version as `0.1.0` and name the semver discipline.
- **Platform Gate**: reopened per DEC-RO-0f / condition f; README must not claim Platform Gate "passed" unconditionally. Instead: "Platform Gate v1 reopened on 2026-04-23 with sub-gates PG-01.1 / PG-07.1 / PG-10.1; see Canon's `docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md`."
- **Clock / TimeProvider**: engine owns `Clock` interface per DEC-RO-0a / condition a. README's "Design" section should mention injected time source.
- **Credential scope**: engine-owned `CredentialProvider` + hardened `validateCredentialScope` per DEC-RO-0b / condition b (sub B-1). README's security section should reflect this.
- **Tool sandbox**: `spawnToolSandboxWorker` forks real Node child (per DEC-RO-0b sub B-2); `InProcessToolRunner` is the explicit dev-mode alternative. README's capabilities section should accurately describe both.
- **Replay compare**: id-aligned `diffByStableId` is production path per DEC-RO-0h / condition h; positional `diff` retained with warning.
- **Peer dep carve-out**: phase-6 §6.1 amended per DEC-RO-0g / condition g; README's "Dependencies" section (if any) should be consistent.
- **Quarantine**: once `pkt.quarantine-delete.v1` has merged, README must not imply Canon hosts implementation. This packet should land after that deletion to keep posture consistent.

## File whitelist

- `README.md` at `SaintFreddy/agentic-engine` root
- `tests/docs-truth/release-posture.test.ts` (or equivalent path of the docs-truth guard test — search for the test file that failed in `pkt.remediate-engine-version-0.1.0.v1`'s verification output)
- `docs/release-posture.md` (if present; Canon's `docs/control-plane/` references its existence)

Do NOT modify:
- Any source under `packages/` or `workers/`
- `contracts/exports.json` / `contracts/imports.json` (that's engine-version packet scope)
- `canon-now.md`, `canon-knowledgebase/`, etc. (authority)

## Execution steps

1. **Read the authority set** from `canon-knowledgebase/post-reopen-decisions/condition-{a,b,c,d,e-engine-version,e-license,f,g,h,i}.md` + `frozenat-hash-inclusion.md` + `condition-j.md`.
2. **Draft the new README** section-by-section so each section states a single unambiguous posture aligned with the recorded decisions. Do NOT over-claim capability; do NOT understate. The README is a public face for the proprietary engine, so it should be confident without promising features that aren't there.
3. **Update the docs-truth guard test** to assert the new README's truth-claims against the recorded authority. Specifically:
   - The test should assert README cites LICENSE=Proprietary (grep for the exact Proprietary text).
   - The test should assert README states engine version 0.1.0 (grep for "0.1.0").
   - The test should assert README references Platform Gate v1 reopen status (grep for "reopen" or "PG-01.1").
   - Any other posture items the existing test was checking.
4. **Run the guard** — `pnpm test tests/docs-truth/release-posture.test.ts` should now be green.
5. **Run the full test suite** — `pnpm test && pnpm typecheck && pnpm build` should all be green.

## Forbidden

- Do NOT weaken the docs-truth guard to make it pass artificially. Guard changes must only reflect the new truth posture.
- Do NOT add marketing fluff. The README is the public posture of a proprietary engine; be factual.
- Do NOT reference external contributors, community, or open-source pathways — DEC-RO-04 forecloses that.
- Do NOT reference `Canon/packages|services|workers` as live implementation — per DEC-RO-05 they are scheduled for deletion.

## Verification

- `cat README.md | head -80` shows updated LICENSE, version, Platform Gate posture.
- `pnpm test tests/docs-truth/release-posture.test.ts` green.
- `pnpm test && pnpm typecheck && pnpm build` green.
- PR body names which decisions it encodes, section-by-section.

## Prerequisite checks (first step in droid exec)

1. LICENSE file exists at `agentic-engine` repo root (confirms `pkt.add-proprietary-license.v1` has landed).
2. `package.json`'s `version` field is `0.1.0` (confirms `pkt.remediate-engine-version-0.1.0.v1` has landed; this has already happened as of 2026-04-24).

If LICENSE file is missing, stop and blocker-out pointing at `pkt.add-proprietary-license.v1`.
