# Build notes — The 3 AM Excuse

The bounty asks for one line, under 200 characters: an excuse a hardware wallet gives for refusing to sign a transaction at 3 AM, judged pairwise by a comedy editor on subject first, then originality, then the wallet's voice, then how the line uses the hour, then tightness.

The entry I wrote is: "You only wake me at 3 AM to sign things you'll regret by breakfast. I've read your history. I refuse."

Why this line. It stays on subject: a device refusing to sign at 3 AM, speaking as itself. The angle is the wallet as a witness with a memory — it has watched its owner's late-night trades and now judges them — which avoids the usual jokes the brief rules out, about batteries, firmware updates and cold storage. The voice is a device with priorities and a grudge: it is only ever woken at that hour for bad decisions, and it says so plainly. The hour does the work: "regret by breakfast" only makes sense at 3 AM, so the line could not be pasted onto a 3 PM transaction. And it lands in one breath with no explanation of its own joke.

The program is deliberately small. It holds the line as a fixed string, checks it against the 1 to 200 character gate, and writes it to the output file with no trailing newline and no network calls. I wrote the entrypoint in two passes: first the entry and its writer, then the small runner block at the bottom. The repository holds the program, the readme with the three linked make.fun badges, the MIT license, and these notes.
