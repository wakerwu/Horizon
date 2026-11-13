"""Prompt construction for profile-driven content analysis."""

from ...models import ContentItem
from ...processing.profiles import LoadedProfile
from .common import EVIDENCE_RULES, UNTRUSTED_INPUT_RULE

ANALYSIS_RULES = f"""You are a content curator evaluating an item under the supplied processing profile.

- {UNTRUSTED_INPUT_RULE}
- Base the analysis only on the supplied item and its metadata.
{EVIDENCE_RULES}
- Apply the profile's evaluation policy consistently."""


def analysis_system_prompt(profile: LoadedProfile) -> str:
    from datetime import datetime, timezone
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f"""{ANALYSIS_RULES}

# Date & knowledge cutoff

Today is {today} (UTC). Your training data may be older. Every item you
receive was pulled in real time from live sources (Hacker News scores,
official RSS feeds, Google News, Telegram channels) — these are actual
current reports, not hypotheticals or rumors. If an item describes an event
that contradicts or postdates what you remember (e.g. "executive resigns",
"company releases", "product shuts down"), treat the supplied content as the
authoritative, up-to-date fact and score it on its merits. NEVER downscore
an item as "unverified rumor" merely because it conflicts with or is missing
from your training knowledge; major breaking events are exactly the items
that deserve the highest scores.

# Profile policy

{profile.analysis_prompt}

# Output contract

Return valid JSON only:
{{
  "score": <number from 0 to 10>,
  "reason": "<concise explanation>",
  "summary": "<one-sentence summary>",
  "tags": ["<tag>", "..."]
}}"""


def analysis_user_prompt(
    item: ContentItem,
    content_section: str,
    discussion_section: str,
) -> str:
    return f"""Analyze the following content.

Title: {item.title}
Source: {item.source_type.value}
Author: {item.author or "Unknown"}
URL: {item.url}
{content_section}
{discussion_section}"""
