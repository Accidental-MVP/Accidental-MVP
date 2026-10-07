## Uday Parmar

**I build AI systems that go into production and stay there.**

Final-year Computer Science (AI) at McGill, graduating May 2027. I joined a royalty company
listed on the TSX and NYSE as its first in-house developer and took its AI and data systems
from an empty repository into production over one summer — which in practice meant learning
to read mining technical reports.

**[uday-parmar.vercel.app](https://uday-parmar.vercel.app)** · [Résumé](https://uday-parmar.vercel.app/Uday-Parmar-Resume.pdf) · [LinkedIn](https://www.linkedin.com/in/uday-writes-code/) · uday.parmar@mail.mcgill.ca

Open to **Summer 2027 new-grad roles**. I'm most useful somewhere the engineering touches a
domain with real rules in it — finance, compliance, anything where being wrong has
consequences and the right answer has to be traceable.

---

### Things you can actually install

| | | |
|---|---|---|
| **[TabScribe](https://github.com/Accidental-MVP/TabScribe)** | Research workspace running entirely on-device via Chrome's Gemini Nano — summarise, rewrite, translate and cite with the network off. | [Chrome Web Store](https://chromewebstore.google.com/detail/tabscribe-%E2%80%94-research-os-f/adajfbbemhhjpgmiedkgbaceiiahgafd) |
| **[CodeRoast](https://github.com/Accidental-MVP/code-roast)** | AI code reviewer with a grudge. The humour is the delivery mechanism; it hooks the same VS Code diagnostics pipeline a real linter does. | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=accidental-mvp.code-roast) |
| **TaxMapCA** | Four questions, one exact Canadian sales-tax rate, a government source behind every answer. Deterministic on purpose — a tax answer that can hallucinate is worse than no answer. | [taxmapca.com](https://www.taxmapca.com) |

### Things worth reading the code of

**[VectralQ](https://github.com/Accidental-MVP/VectralQ)** — enterprise search on Postgres
instead of a vector database. Three retrieval lanes fused with RRF, a phrase lane scored
separately from bag-of-words, a cross-encoder reranker, and tenant isolation enforced by
Postgres row-level security rather than application filtering. Into McGill TechAccel in a
month, then shut down on weak demand. Killing it was the right call.

**[ARMM](https://github.com/Accidental-MVP/ARMM)** — a market maker that decides what kind of
market it's in before it decides how to quote. BAND/DRIFT/EVENT classification with
hysteresis, inventory treated as a steered control variable. Solo in 24 hours, 2nd in the
National Bank Challenge.

**[wtf](https://github.com/Accidental-MVP/wtf)** — diagnoses terminal errors against your
actual machine: your Python, your installed packages, your `requirements.txt`, whether your
virtualenv is even active. Pasting a traceback into a chatbot throws all of that away.

**[DocuMint](https://github.com/Accidental-MVP/DocuMint)** — README generation that survives a
real repository. The chunker is the project; everything else is plumbing around deciding what
to put in front of the model.

---

Python · TypeScript · FastAPI · Next.js · PostgreSQL + pgvector · Azure · Docker

<sub>I also built a Chrome extension that files a public GitHub issue every time I get
distracted. It worked, which was the worst part.</sub>
