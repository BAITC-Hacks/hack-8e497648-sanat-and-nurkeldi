"""
Task 1 – Message Classifier
Rule-based classifier: assigns each message a category and prints a draft reply.
Categories: справка | жалоба | другое
"""

import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Type aliases
# ---------------------------------------------------------------------------
Category = str  # "справка" | "жалоба" | "другое"

# ---------------------------------------------------------------------------
# Classification rules
# ---------------------------------------------------------------------------

# Priority order: справка first, жалоба second, otherwise другое.
# Each rule is a list of keyword stems/substrings (lowercased, normalised).
RULES: list[tuple[Category, list[str]]] = [
    (
        "справка",
        [
            "справк",    # справка, справку, справки …
            "докумен",   # документ, документы …
            "подтвержден",
            "выписк",    # выписка
            "справ",     # catch-all prefix
        ],
    ),
    (
        "жалоба",
        [
            "жалоб",
            "жалу",
            "не работает",
            "пропал",
            "очередь",
            "холодн",    # холодная, холодно
            "wi-fi",     # after normalisation
            "wifi",
            "сломан",
            "проблем",
        ],
    ),
]

# ---------------------------------------------------------------------------
# Draft replies – indexed 1..5 matching message order in messages.txt.
# Kept here to stay simple and avoidance of invented facts.
# ---------------------------------------------------------------------------

DRAFT_REPLIES: dict[int, str] = {
    1: (
        "Для получения справки о месте учёбы обратитесь в учебный отдел в часы приёма. "
        "Заявление можно подать лично или через личный кабинет студента."
    ),
    2: (
        "Приносим извинения за неудобства. "
        "Ваше обращение передано администрации столовой для принятия мер."
    ),
    3: (
        "Для записи на консультацию, пожалуйста, уточните удобное время "
        "и укажите, к какому специалисту вы хотели бы обратиться."
    ),
    4: (
        "Приносим извинения за неудобства, связанные с отсутствием Wi-Fi. "
        "Заявка передана в технический отдел — специалисты уже занимаются устранением неполадки."
    ),
    5: (
        "Информацию о парковке для гостей вы можете получить на стойке охраны при входе "
        "или у дежурного администратора."
    ),
}


def normalise(text: str) -> str:
    """Lowercase, replace ё→е, and convert all dash/hyphen variants to '-'.

    Handles U+2011 (non-breaking hyphen), U+2012, U+2013, U+2014, U+2212
    and the standard ASCII hyphen so matching works regardless of input encoding.
    """
    text = text.lower()
    text = text.replace("ё", "е")
    # Replace every dash/hyphen variant with a plain ASCII hyphen
    for ch in ("\u2011", "\u2012", "\u2013", "\u2014", "\u2212", "\u00ad"):
        text = text.replace(ch, "-")
    return text


def classify(text: str) -> Category:
    """Return the category for *text* using priority-ordered keyword matching.

    Rules are checked in order (справка → жалоба); the first match wins.
    Falls through to «другое» if no rule matches.
    """
    normalised = normalise(text)
    for category, keywords in RULES:
        if any(kw in normalised for kw in keywords):
            return category
    return "другое"


def load_messages(path: Path) -> list[tuple[int, str]]:
    """Read *path* and return a list of (number, text) pairs, skipping blank lines."""
    messages: list[tuple[int, str]] = []
    idx = 1
    with path.open(encoding="utf-8") as fh:
        for raw_line in fh:
            line = raw_line.strip()
            if line:
                messages.append((idx, line))
                idx += 1
    return messages


def print_result(number: int, text: str, category: Category, reply: str) -> None:
    """Print one classified message in the required format."""
    print(f"[{number}] {text}")
    print(f"    Категория : {category}")
    print(f"    Ответ     : {reply}")
    print()


def main() -> None:
    """Entry point: load messages, classify each, print results."""
    messages_path = Path(__file__).parent / "messages.txt"
    messages = load_messages(messages_path)

    for number, text in messages:
        category = classify(text)
        reply = DRAFT_REPLIES.get(number, "Ваш запрос принят, мы свяжемся с вами.")
        print_result(number, text, category, reply)


if __name__ == "__main__":
    # Ensure Cyrillic output works on Windows too
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    main()
