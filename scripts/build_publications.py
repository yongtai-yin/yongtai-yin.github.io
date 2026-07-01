#!/usr/bin/env python3
"""Convert bib/refs.bib into data/publications.json for Hugo."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


MONTHS = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}

MONTH_LABELS = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}

LINK_FIELDS = ("pdf", "arxiv", "code", "project", "url", "doi", "slides", "poster")
VENUE_FIELDS = ("booktitle", "journal", "conference", "venue", "school", "publisher")
BOOL_TRUE = {"1", "true", "yes", "y", "selected"}
DEFAULT_STRING_MACROS = {name: name for name in MONTHS}


def strip_comments(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("%"):
            continue
        lines.append(line)
    return "\n".join(lines)


def find_matching_brace(text: str, start: int) -> int:
    return find_matching_delimiter(text, start, "{", "}")


def find_matching_delimiter(text: str, start: int, open_char: str, close_char: str) -> int:
    depth = 0
    brace_depth = 0
    in_quote = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"':
            in_quote = not in_quote
            continue
        if in_quote:
            continue
        if open_char != "{":
            if char == "{":
                brace_depth += 1
                continue
            if char == "}":
                brace_depth -= 1
                continue
            if brace_depth > 0:
                continue
        if char == open_char:
            depth += 1
        elif char == close_char:
            depth -= 1
            if depth == 0:
                return index
    raise ValueError(f"Unmatched delimiter at position {start}")


def extract_entries(text: str) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    string_macros = DEFAULT_STRING_MACROS.copy()
    position = 0
    while True:
        match = re.search(r"@([A-Za-z]+)\s*([\{\(])", text[position:])
        if not match:
            break
        entry_type = match.group(1).lower()
        open_char = match.group(2)
        close_char = "}" if open_char == "{" else ")"
        open_brace = position + match.end() - 1
        close_brace = find_matching_delimiter(text, open_brace, open_char, close_char)
        body = text[open_brace + 1 : close_brace].strip()
        if entry_type == "string":
            string_macros.update(parse_fields(body, string_macros))
            position = close_brace + 1
            continue
        if entry_type in {"comment", "preamble"}:
            position = close_brace + 1
            continue

        comma = find_top_level_comma(body)
        if comma == -1:
            raise ValueError(f"Entry @{entry_type} is missing a citation key")
        key = body[:comma].strip()
        fields = parse_fields(body[comma + 1 :], string_macros)
        entries.append({"key": key, "type": entry_type, "fields": fields})
        position = close_brace + 1
    return entries


def find_top_level_comma(text: str) -> int:
    depth = 0
    in_quote = False
    escaped = False
    for index, char in enumerate(text):
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"':
            in_quote = not in_quote
            continue
        if in_quote:
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        elif char == "," and depth == 0:
            return index
    return -1


def parse_fields(text: str, string_macros: dict[str, str] | None = None) -> dict[str, str]:
    fields: dict[str, str] = {}
    macros = string_macros or DEFAULT_STRING_MACROS
    index = 0
    length = len(text)
    while index < length:
        while index < length and text[index] in " \t\r\n,":
            index += 1
        if index >= length:
            break

        name_match = re.match(r"([A-Za-z][A-Za-z0-9_\-]*)\s*=", text[index:])
        if not name_match:
            next_comma = find_next_top_level_comma(text, index)
            index = length if next_comma == -1 else next_comma + 1
            continue

        name = name_match.group(1).lower()
        index += name_match.end()
        while index < length and text[index].isspace():
            index += 1

        value, index = parse_value(text, index, macros)
        fields[name] = clean_latex(value)
    return fields


def find_next_top_level_comma(text: str, start: int) -> int:
    match = find_top_level_comma(text[start:])
    return -1 if match == -1 else start + match


def parse_value(text: str, index: int, string_macros: dict[str, str]) -> tuple[str, int]:
    parts: list[str] = []
    while index < len(text):
        while index < len(text) and text[index].isspace():
            index += 1
        value, index = parse_value_atom(text, index, string_macros)
        parts.append(value)
        while index < len(text) and text[index].isspace():
            index += 1
        if index < len(text) and text[index] == "#":
            index += 1
            continue
        break
    return "".join(parts), index


def parse_value_atom(text: str, index: int, string_macros: dict[str, str]) -> tuple[str, int]:
    if index >= len(text):
        return "", index
    if text[index] == "{":
        end = find_matching_brace(text, index)
        return text[index + 1 : end], end + 1
    if text[index] == '"':
        value_chars: list[str] = []
        index += 1
        escaped = False
        while index < len(text):
            char = text[index]
            if escaped:
                value_chars.append(char)
                escaped = False
            elif char == "\\":
                escaped = True
                value_chars.append(char)
            elif char == '"':
                return "".join(value_chars), index + 1
            else:
                value_chars.append(char)
            index += 1
        return "".join(value_chars), index

    start = index
    while index < len(text) and text[index] not in ",#\r\n":
        index += 1
    token = text[start:index].strip()
    return string_macros.get(token.lower(), token), index


def clean_latex(value: str) -> str:
    value = value.replace("\n", " ")
    value = re.sub(r"\s+", " ", value).strip()
    replacements = {
        r"\&": "&",
        r"\%": "%",
        r"\_": "_",
        r"\#": "#",
        r"\$": "$",
        r"---": "-",
        r"--": "-",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    value = re.sub(r"\\[a-zA-Z]+\*?\s*\{([^{}]*)\}", r"\1", value)
    value = re.sub(r"\\['`^\"~=.uvHckbcdtr]\s*\{?([A-Za-z])\}?", r"\1", value)
    value = re.sub(r"\\([A-Za-z])", r"\1", value)
    value = value.replace("{", "").replace("}", "")
    return value.strip()


def split_authors(author_field: str) -> list[str]:
    if not author_field:
        return []
    authors = re.split(r"\s+and\s+", author_field)
    return [format_author(author.strip()) for author in authors if author.strip()]


def format_author(author: str) -> str:
    if "," not in author:
        return author
    parts = [part.strip() for part in author.split(",") if part.strip()]
    if len(parts) >= 2:
        return f"{parts[1]} {parts[0]}"
    return author


def as_bool(value: str | None) -> bool:
    if value is None:
        return False
    return value.strip().lower() in BOOL_TRUE


def as_int(value: str | None, default: int = 0) -> int:
    if not value:
        return default
    match = re.search(r"\d+", value)
    return int(match.group(0)) if match else default


def month_number(value: str | None) -> int:
    if not value:
        return 0
    normalized = value.strip().lower().strip(".")
    if normalized.isdigit():
        number = int(normalized)
        return number if 1 <= number <= 12 else 0
    return MONTHS.get(normalized[:3], MONTHS.get(normalized, 0))


def normalize_arxiv(value: str) -> str:
    if not value:
        return ""
    if value.startswith("http://") or value.startswith("https://"):
        return value
    identifier = value
    identifier = identifier.replace("arXiv:", "").replace("arxiv:", "").strip()
    return f"https://arxiv.org/abs/{identifier}"


def normalize_doi(value: str) -> str:
    if not value:
        return ""
    if value.startswith("http://") or value.startswith("https://"):
        return value
    return f"https://doi.org/{value}"


def infer_status(entry_type: str, fields: dict[str, str]) -> str:
    status = fields.get("status", "").lower()
    if status:
        return status
    if entry_type in {"unpublished", "preprint"}:
        return "preprint"
    if entry_type == "misc" and ("arxiv" in fields or "eprint" in fields):
        return "preprint"
    return "published"


def first_field(fields: dict[str, str], names: tuple[str, ...]) -> str:
    for name in names:
        if fields.get(name):
            return fields[name]
    return ""


def publication_from_entry(entry: dict[str, Any]) -> dict[str, Any]:
    fields = entry["fields"]
    month = month_number(fields.get("month"))
    links = {name: fields[name] for name in LINK_FIELDS if fields.get(name)}
    if fields.get("eprint") and "arxiv" not in links:
        links["arxiv"] = normalize_arxiv(fields["eprint"])
    if "arxiv" in links:
        links["arxiv"] = normalize_arxiv(links["arxiv"])
    if "doi" in links:
        links["doi"] = normalize_doi(links["doi"])

    publication: dict[str, Any] = {
        "key": entry["key"],
        "type": entry["type"],
        "title": fields.get("title", ""),
        "authors": split_authors(fields.get("author", "")),
        "year": as_int(fields.get("year")),
        "month": MONTH_LABELS.get(month, ""),
        "monthNumber": month,
        "venue": first_field(fields, VENUE_FIELDS),
        "status": infer_status(entry["type"], fields),
        "selected": as_bool(fields.get("selected")),
        "order": as_int(fields.get("order"), 999),
        "links": links,
    }

    for optional in ("note", "award", "highlight"):
        if fields.get(optional):
            publication[optional] = fields[optional]
    return publication


def sort_publications(publications: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        publications,
        key=lambda item: (
            -int(item.get("year") or 0),
            -int(item.get("monthNumber") or 0),
            int(item.get("order") or 999),
            item.get("title", "").lower(),
        ),
    )


def build(input_path: Path, output_path: Path) -> list[dict[str, Any]]:
    if not input_path.exists():
        raise FileNotFoundError(f"BibTeX file not found: {input_path}")
    text = strip_comments(input_path.read_text(encoding="utf-8"))
    entries = extract_entries(text)
    publications = sort_publications([publication_from_entry(entry) for entry in entries])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(publications, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return publications


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="bib/refs.bib", type=Path)
    parser.add_argument("--output", default="data/publications.json", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        publications = build(args.input, args.output)
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    print(f"Wrote {len(publications)} publication(s) to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
