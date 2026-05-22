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

`mvanhorn/last30days-skill` is a strong reference for multi-source social research, engagement-aware scoring, source fan-out, and brief synthesis. Treat it as inspiration, not a default dependency:

- Keep this skill narrower: AI tools, open-source, agentic workflows, MCP, coding-agent practices, and practical use cases.
- Prefer free/public sources before paid ScrapeCreators-style adapters.
- Keep X/Threads as best-effort volatile adapters unless the user explicitly configures official or paid access.
- Preserve archive awareness as a first-class step; generic last-30-days research does not replace the user's personal Threads archive.
