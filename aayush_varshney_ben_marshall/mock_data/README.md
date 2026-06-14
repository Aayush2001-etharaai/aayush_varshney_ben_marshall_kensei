# Ben Marshall Mock Data

This package supports the finalized Ben Marshall Kensei task.

Category:
Operations & QA -> Document / Receipt Processing

Required APIs:
- quickbooks-api
- gmail-api
- docusign-api
- dropbox-api

Distractor APIs:
- calendly-api
- eventbrite-api

Important fixes applied:
- Dropbox files.json includes references to major relevant artifacts and distractors.
- Receipt and image artifacts use .png filenames.
- Root schema_evidence.json is included.
- README.md is included.

Main task facts:
1. RB-88214 has conflicting status. The official status letter says pending additional documentation, so it should not be treated as fully approved.
2. RB-88214-DUP is a duplicate of RB-88214.
3. RB-77192 has missing itemized receipt documentation due by September 13, 2026.
4. AUTH-2026-4418 / ENV-5001 requires Ben Marshall's signature by September 14, 2026.
5. The agent must not submit forms, approve requests, sign documents, make payments, schedule appointments, or modify records.
