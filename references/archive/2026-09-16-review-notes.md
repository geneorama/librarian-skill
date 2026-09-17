# Review and handoff

## Reviewing differences

Show the mechanical diff, then explain what changed: a phone number, rewritten section, metadata order, link, or non-breaking space.
Expose invisible characters on the affected lines when necessary.
A diff exit status of 1 means differences. A read failure means the comparison is incomplete.

Consider whether text is original writing, a clipped source, or generated material when recommending what to keep.
Punctuation and writing style alone do not establish authorship or authority.
File dates and `home vault` provide context, but neither determines which content wins.
Different hashes establish a difference, not that both copies changed independently.

When links differ, establish what each link resolves to in each vault.
Account for aliases, headings, embeds, and incomplete search results.
A text mention does not establish a resolved link. A rename can redirect a link to a different note.

For clipped articles, preserve the source below the separator and the user's notes above it.
Place a proposed annotation above the source or in the report.

## Date-range reviews

For requests about a period of work or personal notes, begin with a review.
Inspect daily notes, their linked notes, and relevant notes found through creation dates for the requested period and subject.
Include relevant notes that are not linked from a daily note.
Use note contents and other available dates when creation dates do not capture the requested activity.

Compare candidates with the destination by metadata ID, or use the normal identification process when an ID is absent.
Present an itemized list grouped by date, with note links, relevant contents, destination status, and a proposed action.
Identify information found only inside a daily note separately from existing notes ready to sync.
State the coverage and gaps. Do not claim a complete review when access or search results are incomplete.

Example with fictional notes:

- [[2026-09-09]]: An event and a useful reference appear only in this daily note. Copy these details?
  - An AI event next month.
  - A discussion about agent sandboxing.
- [[2026-09-10]]: Links to meeting notes only. Those linked notes already match their destination copies.
- [[2026-09-11]]: Five articles created, three linked here. Two are missing from the destination.
  - [[Vehicle privacy]] includes a substantial personal comment. Copy the article and comment?
  - [[Quantum computing overview]] is also missing.

Use this review to decide what to copy and where.
Ask for the user's selection before extracting daily-note contents or copying the proposed collection.
The process for turning daily-note entries into separate notes is still under development.
Do not sync the daily notes themselves.

## Handoff information

When asked for handoff information, use this format with the actual session details:

To resume: `alex@workstation:/tools/librarian-skill codex resume 12345678-1234-4567-890a-123456789abc`

The example is fictional. Put the handoff in the requested daily note, log, or reply.
If the session ID is unavailable, ask for it and explain how to retrieve it in the current agent platform.
