# Review and publish

These commands use Bash on Linux or Git Bash on Windows.
Run them from this checkout after reviewing the changes.
They do not install the skill or change any vault notes.

## Commit the rewrite

```bash
# Read-only: inspect the changes and the email for the next commit.
git status --short
git diff --check
git diff --stat
git diff
git config user.email
```

Use your GitHub-provided private email before committing.
Review new files too, since ordinary `git diff` does not display untracked files.
The following paths cover this rewrite, including the removed references.
Local review notes matching `review-*.md` and files under `config/` remain excluded.

```bash
# Changes the index: stage the reviewed skill, notes, examples, and helper edits.
git add -A -- .gitignore SKILL.md README.md MAINTENANCE.md \
  references config-sample scripts

# Read-only: inspect exactly what will enter the commit.
git diff --cached --check
git diff --cached

# Changes local Git history: record the reviewed rewrite.
git commit -m "Align librarian skill with the interactive sync workflow"
```

## Replace the published branch history

Use this section after committing, while the working tree is clean.
The commands assume the existing branches are `main` and `dev`, with remote `origin`.
Close the existing development pull request in GitHub before replacing its branch history.

An orphan branch starts a new history with no parent commit.
`git checkout --orphan` preserves the selected snapshot in the index and working tree.
See [git checkout](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---orphanltnew-branchgt).

```bash
# Updates local remote-tracking refs. Inspect the current branch and tags first.
git fetch origin
git status --short
git branch -av
git tag

# Creates a new root commit containing the current committed files.
# clean-main must be an unused local branch name.
git checkout --orphan clean-main
git commit -m "Initial public version"
git branch -M main

# Read-only: this must show one commit with the intended author email.
git log --format=fuller
```

Review that commit before running the publication commands.

```bash
# Replaces remote main with the new history, then deletes the old dev branch.
git push --force-with-lease origin main
git push origin --delete dev
```

Run the local cleanup only after both pushes succeed.

```bash
# Deletes the old local dev branch and removes stale remote-tracking refs.
git branch -D dev
git fetch --prune origin

# Read-only: inspect all remaining branch and tag references.
git for-each-ref --format='%(refname)'
git log --all --format='%h %ae %s'
```

If a tag or another branch retains the old commits, review that reference before deleting it.
The commands above replace branch history. They do not purge local reflogs or GitHub's retained pull-request references and cached views.
See [GitHub's history-removal guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

The force-with-lease option checks for an unexpected remote change before replacing a branch.
See [git push](https://git-scm.com/docs/git-push#Documentation/git-push.txt---force-with-lease).
