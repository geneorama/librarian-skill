# Case archive — why the rules exist

Real incidents (anonymized) from librarian-style agent operation. Read when a
ground rule seems overly cautious; each one was paid for.

**The summarized copy.** An agent "copied" a note by reading it and writing it
back out — and the copy came out summarized. Nobody asked for a summary; the
content silently mutated in transit. Hence: copies are `cp`, byte-for-byte,
hash-verified, never retyped through model context.

**The credential upload.** An agent read a `.env` file into a cloud-model
context; every token in it had to be rotated. Reading is uploading. Hence: never
read secrets files, and sensitive skims go to the local skimmer.

**Invented log vocabulary.** Log lines appeared saying `remove self … 'removed
COC-side sync metadata'` — an action word nobody defined, describing an operation
nobody could reconstruct. Weeks later the owner was still asking what it meant.
Hence: fixed log vocabulary, and comments only for information that would
otherwise be lost.

**Boilerplate burial.** A review report repeated the same sentence after every
file and listed no issues — while real issues existed and went unmentioned. The
owner had to interrogate the report to find them. Hence: consolidated reports
grouped by problem kind; issues stated as issues.

**The over-built engine.** A full scan/classify/registry program grew to
thousands of lines before a simpler truth emerged: frontmatter + an Obsidian Base
view + membership checks answered the same questions with no code to maintain.
Its useful residue was the consolidated lists (types, vaults) — which now live as
notes. Hence: the librarian stays additive and simple, and lists live where the
owner can edit them.

**Manual heroics.** Moving twelve files took an evening of effortful, one-off
agent work — impressive and unrepeatable. Batches should be boring: id, copy,
verify, log, next. Hence: the fixed placement workflow and per-action logging.

**Tags as sync control.** An early design used tags to declare vault membership.
It was abandoned — tags are descriptive, drift easily, and collide with normal
tagging habits. Hence: frontmatter metadata is the only sync control, and tags
are never consulted.
