from pydantic import BaseModel
import argparse
from openai import OpenAI

client = OpenAI()
MODEL = "gpt-4o-mini"


class Command(BaseModel):
    unix_command: str


def predict(prompt):
    response = client.responses.parse(
        model=MODEL,
        instructions="You are unix command line expert. For users query generate valid unix command line command.",
        input=prompt,
        text_format=Command
    )
    return response.output_parsed.unix_command


def main():
    parser = argparse.ArgumentParser(description="Unix terminal expert. For given prompt generates unix command.")
    parser.add_argument("unix_cmd_desc", type=str, nargs="+", help="describe what you wanna do")
    args = parser.parse_args().unix_cmd_desc
    prompt = ' '.join(args)
    return predict(prompt)
