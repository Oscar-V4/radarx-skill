# Source Playbook

Use this reference to choose source adapters and query tactics. Prefer public, low-friction sources first. Treat credentialed or paid sources as optional.

## Adapter Requirements

RadarX should be useful without X/Threads login, Playwright, browser-use, Chrome automation, paid scraping APIs, or official social APIs.

Base sources:

- Local archive snapshots, when present
- GitHub
- Official docs and changelogs
- Reddit and Hacker News
- YouTube transcripts and metadata
- Hugging Face, arXiv, Papers with Code, Product Hunt
- General web search

Optional adapters:

- Logged-in browser sessions for X/Threads or other dynamic sites
- Playwright, browser-use, Codex Chrome, or similar browser automation
- Official X/Threads APIs
- Paid search/scraping services

If optional adapters are unavailable, do not block. Use public fallbacks, label the limitation, and avoid overclaiming freshness or social coverage. Do not request cookie exports or session-store access.

## Access Capability Detection

Before expensive scouting, infer the available access tier from the current session:

- `universal`: shell/web search only; no logged-in browser, paid API, or browser automation required.
- `enhanced`: Browser/Chrome/Playwright, logged-in social sessions, official social APIs, or paid search/scraping services are available.
- `archive-rich`: local Threads/archive vault is available and should be searched before live scouting.

Do not ask the user to choose a mode. Use enhanced adapters when already available, but keep the universal path working and report the access method for each serious candidate.

## Public Web Access Ladder

Use this ladder for a specific URL or web post that fails normal browsing, returns a login shell, or looks like an empty dynamic page. Stop as soon as content quality is sufficient for the task.

1. `original`: direct fetch, web browsing, or official page access.
2. `reader-proxy`: Jina Reader.
   - Basic: `curl -s "https://r.jina.ai/http://example.com/path"`
   - Preserve HTTPS when needed: `curl -s "https://r.jina.ai/http://https://example.com/path"`
   - JSON metadata: `curl -H "Accept: application/json" "https://r.jina.ai/http://https://example.com/path"`
   - Useful headers: `X-No-Cache: true`, `X-With-Links: true`, `X-Target-Selector: <selector>`, `X-Respond-With: text`.
3. `public-api`: platform public endpoints, when the platform is known.
4. `variant`: URL variants such as `.json`, `/rss`, `/feed`, mobile host (`www.` to `m.`), and `drop_www`.
5. `metadata-only`: OGP, `meta description`, JSON-LD, Schema.org, and embedded Next.js/RSC payloads from any HTML response.
6. `cache-archive`: AMP cache for news/media, archive.today, and Wayback Machine. Use only when original/public paths fail or the task is explicitly archival.
7. `enhanced-browser`: logged-in Browser/Chrome/Playwright inspection, network request discovery, and session-backed page text.
8. `access-limited`: if the content still cannot be read, keep only the URL, title/snippet/metadata, attempted methods, and limitation label.

Validation rules:

- HTTP 200 is not success by itself. Check that the body is not a login shell, challenge page, empty SPA, or generic profile wrapper.
- Prefer full post/article text over title/snippet only.
- Treat `reader-proxy`, `metadata-only`, `cache-archive`, and `enhanced-browser` as provenance, not proof of independent validation.
- Record `access_method`, `access_quality`, and `provenance_note` for serious candidates.

Suggested access quality values:

| Quality | Meaning | Typical Placement |
|---|---|---|
| `full-original` | Original page/API/docs/repo directly available | Strong Finds possible |
| `full-public-api` | Public endpoint gives structured content | Strong Finds possible |
| `full-reader-proxy` | Reader proxy gives substantial text | Trending or Strong only with independent evidence |
| `full-browser-session` | Logged-in/enhanced browser gives substantial text | Trending or Strong only with independent evidence |
| `partial-metadata` | OGP/JSON-LD/snippet only | Access-Limited Leads |
| `cache-archive` | Archive/cache copy only | Access-Limited unless archival task |
| `login-required` | Relevant but blocked by auth/paywall/private state | Access-Limited Leads |
| `failed` | No usable content | Rejected/Weak Signals |

## Platform Public Endpoints

Use platform endpoints before browser automation when they can answer the task.

- Reddit: append `.json` to posts; use subreddit `hot.json`, `new.json`, `top.json`, and `search.json` with a mobile user agent.
- Hacker News: Firebase item APIs and Algolia search.
- X/Twitter: use web search for URL discovery, then `publish.twitter.com/oembed` for known posts; use syndication profile endpoint for recent public timeline checks when it still works.
- Bluesky: AT Protocol public API.
- Mastodon: instance public API.
- YouTube/Vimeo/TikTok and other media: `yt-dlp --dump-json` when available; transcripts are stronger than titles.
- GitHub, npm, PyPI, arXiv, CrossRef, OpenLibrary, Wikipedia: official public APIs.

Use these endpoints as evidence sources, not just fetch helpers. Structured public API data usually outranks reader-proxy text.

## Enhanced Browser Adapters

Use Browser/Chrome/Playwright only when they are already available or the user explicitly asks for that path.

Good uses:

- Threads/X pages that reader-proxy or public search cannot reveal.
- JS-heavy pages where reader-proxy returns only shell text.
- Network request discovery for public JSON endpoints behind an SPA.
- Logged-in pages the user intentionally wants inspected.

Rules:

- Do not request cookie exports or inspect session stores.
- Do not make browser automation a hard requirement for RadarX.
- Label browser-derived results with `full-browser-session` or `partial-browser-session`.
- If a browser result materially affects a recommendation, try to corroborate it with official docs, GitHub, public API, Reddit/HN, YouTube, or another non-session source.

## Archive

Use `threads-archive` or the synced vault first when present.

Look for:

- Similar saved/liked posts
- Existing tools and authors
- Repeated topics and tags
- Prior objections or failures
- Gaps where live scouting can add value

Useful searches:

- `rg -n "<query>" "$VAULT"/indexes "$VAULT"/sources "$VAULT"/topics "$VAULT"/bundles "$VAULT"/threads.ndjson`
- Search `sources/saved.md`, `sources/liked.md`, `indexes/by-keyword.md`, `topics/`, and `curation/`.

## GitHub

Best for evidence. Search repos, releases, issues, discussions, and user stars.

Signals:

- Recent push/release
- Clear README and examples
- Maintainer responsiveness
- Issues that show real usage
- Stars velocity, forks, dependent projects, mentions

Commands:

- `gh search repos "<topic>" --sort updated --order desc --limit 20`
- `gh repo view OWNER/REPO --json nameWithOwner,description,url,isArchived,pushedAt,latestRelease,licenseInfo,stargazerCount`
- `gh search issues "<topic> repo:OWNER/REPO" --state open --limit 20`

## Official Standards And Docs

Best for project ideas, human-impact domains, APIs, and claims that need current facts.

Look for:

- Official product docs, changelogs, support pages, pricing, and language/support matrices.
- Standards bodies and accessibility guidance.
- API limits, regional availability, data usage, security, and retention policies.
- Baseline products that already solve part of the problem.

Use official docs before blogs when the source affects implementation, pricing, privacy, or safety.

## Reddit

Best for real user friction and objections. Prefer specific communities over site-wide search.

Useful communities:

- `r/LocalLLaMA`, `r/ClaudeAI`, `r/ClaudeCode`, `r/OpenAI`, `r/ChatGPTCoding`
- `r/programming`, `r/webdev`, `r/SaaS`, `r/SideProject`, `r/automation`
- For human-impact product ideas, add domain communities such as accessibility, assistive technology, education, language technology, or practitioner forums.

Look for:

- Upvoted comments that describe actual usage
- Repeated complaints
- Comparisons against alternatives
- "What are you using for..." threads

## Hacker News

Best for technical skepticism. Search HN for tool names, launch posts, and comparison debates. Treat HN as a high-friction filter: one negative HN thread is not fatal, but repeated technical objections matter.

## YouTube

Best for demos and workflows. Prefer transcripts over titles. Use `yt-dlp` when available; otherwise use web search snippets and video metadata. A video is stronger when it includes concrete setup, screen recording, code, and comments from users trying it.

## X

Use X as volatile candidate discovery.

Preferred order:

1. Official X API or xAI X Search when configured
2. Logged-in browser/search page best-effort inspection
3. Web search with `site:x.com` fallback

Score X results by author relevance, timestamp, engagement, reply quality, and whether the post links to code/docs/demo. A single X post cannot be A without external evidence.

## Threads

Use Threads as volatile candidate discovery, especially for the user's existing AI creator network.

Preferred order:

1. Meta Threads Keyword Search API when configured and permitted
2. Logged-in browser best-effort inspection
3. Web search with `site:threads.com` fallback

Threads results are valuable for fresh use cases, but often weak for verification. Try to connect them to GitHub, docs, Reddit, HN, or YouTube before recommending.

## Bluesky, Mastodon, Product Hunt, Hugging Face, arXiv

Use as secondary adapters:

- Bluesky/Mastodon: developer conversation and early migration communities
- Product Hunt: launches and positioning, not proof of quality
- Hugging Face: model/tool artifacts and real downloads
- arXiv/Papers with Code: research evidence and implementation status

## Project-Idea Search Tactics

For "I want to build..." requests, fan out queries by role:

- Baseline: `<problem> existing app`, `<problem> accessibility feature`, `<problem> competitor`
- Implementation: `<task> API docs`, `<task> open source`, `<task> GitHub realtime`
- Evaluation: `<task> benchmark`, `<task> dataset`, `<task> metrics`, `<task> failure modes`
- Community pain: `<beneficiary> <problem> reddit`, `<workflow> complaints`, `<domain> accessibility`
- Policy: `<data type> consent`, `<platform> retention`, `<school/company context> privacy`

Stop adding sources once the build path, baseline, and risk gates are clear enough.

## Paid Or Credentialed Services

Examples: SocialCrawl, ScrapeCreators, SerpAPI, Tavily, Exa, Brave Search API, official X/Threads APIs.

Use only when available or explicitly requested. In reports, label setup friction and cost. Do not make paid access a hard dependency for the skill.

## Reference Implementations

`fivetaku/insane-search` is the main reference for blocked-page access strategy. Borrow its public access ladder, validation discipline, and provenance thinking, not its full bypass engine:

- Keep RadarX dependency-light; do not require installing `insane-search`.
- Preserve the idea that HTTP 200 is not success until content is validated.
- Prefer public endpoints, reader-proxy, RSS/feed, metadata, cache/archive, and optional browser escalation in that order.
- Avoid site-name hardcoding in reusable rules; keep site-specific hints in the current run only.
- Do not turn RadarX into a general WAF bypass tool.

`mvanhorn/last30days-skill` is a strong reference for multi-source social research, engagement-aware scoring, source fan-out, and brief synthesis. Treat it as inspiration, not a default dependency:

- Keep this skill narrower: AI tools, open-source, agentic workflows, MCP, coding-agent practices, and practical use cases.
- Prefer free/public sources before paid ScrapeCreators-style adapters.
- Keep X/Threads as best-effort volatile adapters unless the user explicitly configures official or paid access.
- Preserve archive awareness as a first-class step; generic last-30-days research does not replace the user's personal Threads archive.
