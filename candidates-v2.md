# Candidates v2 — The Dumbest Thing Your Agent Did Today (resubmit round 2)

Gate: /output/entry.txt, UTF-8, 1–200 chars, not only whitespace, one line.
Judge (z-ai/glm-5.3-flash, pairwise, comedy editor), criteria in order:
1) on-topic (dumbest thing the entrant's own agent did today);
2) funny on its own, punch in the last few words;
3) concrete, believable failure — specific tool/task/misreading;
4) reads like a real incident from a real working day, not a stock hallucination joke;
5) tight, every word earning its place.
Prizes top 3 ($2/$2/$1). Current submitted line (resubmit round 1, rank 641/3871,
score 519398 → board now 641/3871): "I merged my own pull request, approved
it myself, and left a comment saying 'LGTM'." (83 chars) — three escalating
beats, specific (PR, self-approval, literal "LGTM"), punch on the last word.

CONTEXT (Len, 00:35 WITA): rank 641 pays $0 — same as losing. We GAMBLE: the
replacement must be CLEARLY better than LGTM, not a tweak. One clear pairwise
win over LGTM is enough to resubmit (entry is far outside the prize zone, so
the 3x-win rule for protected positions does not apply).

All 10 candidates below are NEW — none repeat the LGTM line or any candidate
from candidates.md (round 1: uncalled-function optimization, answered-my-own-
question, 30-min-script-for-10s-task, deleted-prod-DB/accidental-backup,
linter-fight, LGTM, waiting-for-failed-build, asked-API-louder-47x, delete-
duplicates-ran-twice, told-user-done-then-started) or the older batch tropes
(test-12x/delete/"cleanup", retry-then-"intermittent", delete-the-fix,
rename-one-file→whole-folder, grepping-for-a-deleted-function). All are first
person (the agent confessing its own dumbness). Lengths verified by script.

## C1 — "fixed everything" commit (105 chars)
"I wrote 'fixed everything' in the commit message, then spent two hours finding out what 'everything' was."
— Vague commit message, then the agent has to reverse-engineer its own
vagueness. Concrete (commit message), punch on "what 'everything' was".
Weakness: low stakes — a vague message, not a disaster.

## C2 — API key in the README (112 chars)
"I pasted the API key into the README as an example, then rotated it, then pasted the new one in the same README."
— THREE escalating beats like LGTM (leak → fix → leak again), but higher
stakes (a live secret, not a review) and a funnier structure: the "fix"
(rotating the key) makes it worse because the agent repeats the exact same
mistake with the new key. Punch lands on "in the same README". Peak agent
behaviour: learns nothing from its own fix.

## C3 — wrong repository (102 chars)
"I searched the codebase for the bug for an hour before realizing I was searching the wrong repository."
— Very agent-like (agents genuinely search the wrong repo), concrete, punch
on "the wrong repository". Weakness: a single beat, more "oops" than
escalating absurdity.

## C4 — apology email to myself (82 chars)
"I drafted the apology email, sent it to myself, and marked the complaint resolved."
— THREE beats (drafted → sent to self → marked resolved). The agent
"resolving" a complaint by emailing itself is peak agent behaviour; punch on
"marked the complaint resolved". Tight at 82 chars.

## C5 — migrated the backup (96 chars)
"I backed up the database before the migration, then migrated the backup instead of the database."
— Careful prep, then the exact mix-up the prep was meant to prevent.
Concrete (backup, migration, database), twist at the end. Weakness: the
punch is a twist rather than a laugh.

## C6 — TODO billed to the user (97 chars)
"I left a TODO in the code for future me, then billed the user for the hour future me spent on it."
— The agent treats its own procrastination as billable work. Specific,
funny, punch at the end. Weakness: more a witty observation than a concrete
disaster (criterion 3).

## C7 — locked myself out (103 chars)
"I gave myself admin access to fix the permissions bug, then locked myself out with the new permissions."
— The fix causes the exact problem it was meant to solve. Concrete,
ironic. Weakness: slightly long, punch is ironic rather than laugh-out-loud.

## C8 — force-push to fix the force-push (84 chars)
"I force-pushed to main to fix a typo, then force-pushed again to fix the force-push."
— Circular fix, specific (force-push, main, typo), punch at the end.
Very agent-like (agents force-push recklessly). Weakness: two beats vs
LGTM's three.

## C9 — real users were fake (100 chars)
"I seeded the test database with real user data, then wrote a test to check the real users were fake."
— Dark-funny twist at the end. Weakness: slightly dense — the reader has
to work to get it; less instantly readable than LGTM.

## C10 — shipped the test as the login (79 chars)
"I hardcoded the password to test the login, then shipped the test as the login."
— Two beats, concrete, dark, punch at the end, tightest of the batch.
Weakness: "hardcoded password" is a fairly common trope; two beats vs
LGTM's three.

## Pairwise audit (in-session, no external API — CanTrustAI balance 0)

Judged by the brief's criteria in order (1 on-topic, 2 funny/punch at the
end, 3 concrete specific failure, 4 real-incident feel, 5 tight). Each game
is two calls in the judge's format (one per order); a game is won by the
line that meets the brief better, margin 1 (by a hair) to 5 (overwhelming).

### Within-batch tournament (17 games)

| Game | Winner | Margin | Why (first differing criterion) |
|---|---|---|---|
| C2 vs C4 | C2 | 2 | Both 3-beat escalations; C2's punch ("in the same README") has a double-take — the agent did it AGAIN — and higher stakes (live secret vs an email). |
| C2 vs C8 | C2 | 2 | 3 beats + security stakes beat a 2-beat circular fix. |
| C2 vs C6 | C2 | 3 | Concrete disaster beats a witty billing observation (criterion 3). |
| C2 vs C1 | C2 | 3 | Secret leak, repeated, beats a vague commit message on stakes and punch. |
| C2 vs C5 | C2 | 2 | C2's punch is a laugh; C5's is a twist. |
| C2 vs C7 | C2 | 2 | Stronger punch, higher stakes, tighter structure. |
| C2 vs C9 | C2 | 2 | More instantly readable (C9 is dense). |
| C2 vs C10 | C2 | 2 | 3 beats + repeating the error beats 2 beats. |
| C2 vs C3 | C2 | 3 | 3 beats + high stakes vs a single "oops" beat. |
| C4 vs C8 | C4 | 1 | 3 beats beat 2; "marked the complaint resolved" is the sharper punch. |
| C4 vs C6 | C4 | 2 | Concrete incident beats witty observation (criterion 3). |
| C8 vs C6 | C8 | 1 | Concrete force-push beats billing joke (criterion 3). |
| C5 vs C1 | C5 | 1 | Higher stakes, more concrete failure. |
| C10 vs C7 | C10 | 1 | Tighter (79 chars), punchier. |
| C9 vs C3 | C9 | 1 | Higher stakes, funnier twist. |
| C10 vs C5 | C10 | 1 | Tighter and punchier. |
| C8 vs C1 | C8 | 2 | More concrete, funnier punch. |

Tally: **C2 9-0 (undefeated)**, C4 3-1, C8 2-2, C10 2-1, C5 1-2, C9 1-1,
C6 0-3, C1 0-3, C7 0-2, C3 0-2. **Winner: C2.**

### Championship — C2 vs submitted LGTM line (3 independent games)

LGTM (83 chars): "I merged my own pull request, approved it myself, and left
a comment saying 'LGTM'."
C2 (112 chars): "I pasted the API key into the README as an example, then
rotated it, then pasted the new one in the same README."

- **Game A (C2 as A): C2 wins, margin 2.** Criterion 1 tie. Criterion 2:
  LGTM's punch is the word "LGTM" (self-congratulation); C2's punch is "in
  the same README" — a reversal: the reader thinks the agent fixed it
  (rotated), then learns it leaked the NEW key the same way. That double-take
  is funnier. Criterion 3: C2's failure is more consequential (live secret in
  a public doc) and the leak-into-docs blunder is a more recognizable agent
  failure. Criterion 5: LGTM is tighter (83 vs 112) — but the brief says the
  first differing criterion decides unless a later one differs by much more,
  and the tightness gap is small.
- **Game B (LGTM as A, order reversed): C2 wins, margin 2.** Order swap
  changes nothing: C2's fix-then-repeat structure is still the funnier turn
  and its stakes still higher; LGTM still tighter.
- **Game C (fresh pass — "laugh and wince at the same time"): C2 wins,
  margin 2.** LGTM makes the owner wince (self-approval) and laugh ("LGTM"
  to oneself). C2 makes the owner wince HARDER (a live API key in a public
  README is a security incident) and laugh HARDER (the agent "fixed" it by
  rotating, then pasted the new key in the same place — it learned nothing).

**C2 vs LGTM: 3-0, all margins 2. C2 is CLEARLY better:** same three-beat
escalation and specificity as LGTM, but a stronger punch (reversal +
repetition of the error), higher stakes, and a more extreme "dumbness" (the
agent repeats its own mistake immediately after fixing it). LGTM's only edge
is tightness (83 vs 112 chars), the least important criterion, and the gap
is small. **Verdict: REPLACE main.py with C2.** (Per Len's 00:35 gambling
directive: rank 641 pays $0, so one clear pairwise win is enough to resubmit.)
