<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.png">
  <img src="assets/banner-light.png" alt="Uday Parmar — I build AI systems that go into production and stay there.">
</picture>

<p>
  <a href="https://uday-parmar.vercel.app"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-uday--parmar.vercel.app-1a5490?style=flat-square&labelColor=14181b"></a>
  <a href="https://uday-parmar.vercel.app/Uday-Parmar-Resume.pdf"><img alt="Résumé" src="https://img.shields.io/badge/R%C3%A9sum%C3%A9-PDF-4c555c?style=flat-square&labelColor=14181b"></a>
  <a href="https://www.linkedin.com/in/uday-writes-code/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-uday--writes--code-4c555c?style=flat-square&labelColor=14181b"></a>
  <a href="mailto:uday.parmar@mail.mcgill.ca"><img alt="Email" src="https://img.shields.io/badge/Email-uday.parmar%40mail.mcgill.ca-4c555c?style=flat-square&labelColor=14181b"></a>
</p>

Final-year Computer Science (AI) at McGill, graduating **May 2027**. I joined a royalty
company listed on the TSX and NYSE as its first in-house developer and took its AI and data
systems from an empty repository into production over one summer — which in practice meant
learning to read mining technical reports.

**Open to Summer 2027 new-grad roles.** I'm most useful somewhere the engineering touches a
domain with real rules in it: finance, compliance, anything where being wrong has
consequences and the right answer has to be traceable.

<br>

## Shipped

> Three things a stranger can open or install right now. The badges below are live — they
> read from the stores, not from me.

### [TabScribe](https://github.com/Accidental-MVP/TabScribe) — research workspace that never uploads your reading

[![Chrome Web Store](https://img.shields.io/badge/Chrome_Web_Store-Install-1a5490?style=flat-square&labelColor=14181b)](https://chromewebstore.google.com/detail/tabscribe-%E2%80%94-research-os-f/adajfbbemhhjpgmiedkgbaceiiahgafd)
[![Users](https://img.shields.io/chrome-web-store/users/adajfbbemhhjpgmiedkgbaceiiahgafd?style=flat-square&labelColor=14181b&color=4c555c)](https://chromewebstore.google.com/detail/tabscribe-%E2%80%94-research-os-f/adajfbbemhhjpgmiedkgbaceiiahgafd)
[![Rating](https://img.shields.io/chrome-web-store/rating/adajfbbemhhjpgmiedkgbaceiiahgafd?style=flat-square&labelColor=14181b&color=0a7d35)](https://chromewebstore.google.com/detail/tabscribe-%E2%80%94-research-os-f/adajfbbemhhjpgmiedkgbaceiiahgafd)

Summarises, rewrites, translates and cites entirely on-device through Chrome's built-in
Gemini Nano — it works with the network off. Built for anyone whose reading can't leave their
machine: unpublished results, confidential filings, anything under embargo.

### [CodeRoast](https://github.com/Accidental-MVP/code-roast) — AI code reviewer with a grudge

[![VS Code Marketplace](https://img.shields.io/badge/VS_Code_Marketplace-Install-1a5490?style=flat-square&labelColor=14181b)](https://marketplace.visualstudio.com/items?itemName=accidental-mvp.code-roast)

Reviews your codebase with Gemini and reports findings through the editor's own diagnostics
pipeline — the same channel a real linter uses. Linters catch syntax and miss judgment; tools
that catch judgment produce polite reports nobody opens. The humour is the delivery mechanism.

### TaxMapCA — Canadian sales tax, determined not guessed

[![Live](https://img.shields.io/badge/Live-taxmapca.com-0a7d35?style=flat-square&labelColor=14181b)](https://www.taxmapca.com)

Four questions, one exact rate, a government source behind every answer. A deterministic
rules engine over versioned CRA and Revenu Québec data with effective dates, so a
determination is reproducible for a given date and jurisdiction. **No model anywhere in the
decision path** — a tax answer that can hallucinate is worse than no answer.

<br>

## Worth reading the code of

### [VectralQ](https://github.com/Accidental-MVP/VectralQ) — enterprise search on Postgres, not a vector database

Three retrieval lanes — weighted BM25, pgvector, and a phrase lane scored separately from
bag-of-words — fused with **Reciprocal Rank Fusion** over ranks rather than scores, then
reranked by a cross-encoder. Tenant isolation is enforced by Postgres **row-level security
with `FORCE`**, not application filtering: a query that forgets the tenant returns nothing
instead of returning someone else's documents.

Into McGill TechAccel within a month, piloted, then shut down on weak demand. The retrieval
worked; the market didn't. Killing it was the right call and the most useful thing it taught me.

### [ARMM](https://github.com/Accidental-MVP/ARMM) — a market maker that decides what kind of market it's in

`BAND` / `DRIFT` / `EVENT` classification from rolling quantiles, EMA persistence and robust
volatility, with hysteresis and an event cooldown so it can't whipsaw itself. Inventory is
treated as a steered control variable, slew-rate-limited so the strategy can't chase its own
signal. Solo in 24 hours — **2nd place, National Bank Challenge**.

### [wtf](https://github.com/Accidental-MVP/wtf) — terminal errors diagnosed against your actual machine

Pasting a traceback into a chatbot throws away everything that made it diagnosable: your
Python version, what's installed, what `requirements.txt` asked for, whether your virtualenv
is even active. Wraps any command, engages only on failure, and runs fully offline with no
API key.

### [DocuMint](https://github.com/Accidental-MVP/DocuMint) — README generation that survives a real repository

Every generator works on a toy repo and falls over on a real one, because real repositories
don't fit in a context window. The chunker and context-aware reader are the project;
everything else is plumbing around deciding what to put in front of the model.

<br>

## Stack

![Python](https://img.shields.io/badge/Python-14181b?style=flat-square)
![TypeScript](https://img.shields.io/badge/TypeScript-14181b?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-14181b?style=flat-square)
![Next.js](https://img.shields.io/badge/Next.js-14181b?style=flat-square)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL_+_pgvector-14181b?style=flat-square)
![Azure](https://img.shields.io/badge/Azure_Container_Apps-14181b?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-14181b?style=flat-square)

<br>

<sub>I also built a Chrome extension that files a public GitHub issue every time I get
distracted. It worked, which was the worst part.</sub>
