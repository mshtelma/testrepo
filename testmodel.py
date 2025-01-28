import argparse
from typing import Any

from openai import OpenAI

DEFAULT_KWARGS = {
    "temperature": 0.95,
}


def generate_text(
        prompt: dict[str, str],
        generation_kwargs: dict[str, Any] | None = None,
):
    client = OpenAI(
        api_key="EMPTY",
        base_url="http://localhost:8000/v1",
    )
    if not generation_kwargs:
        generation_kwargs = DEFAULT_KWARGS.copy()

    completion = client.chat.completions.create(
        model="model",
        messages=[
            {"role": "user", "content": prompt},
        ],
        **generation_kwargs
    )
    text = completion.choices[0].message.content
    print(f"PROMPT: {prompt}\nAnswer: {text}\n\n\n")
    return text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--strings', nargs='+', required=True, help='Array of prompts')

    args = parser.parse_args()
    print("Testing model...")
    print("Received array of strings:")
    for string in args.strings:
        generate_text(string)

    print("Structured generation done.")


if __name__ == "__main__":
    main()
