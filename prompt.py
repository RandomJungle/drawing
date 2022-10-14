import json
import random
import spacy

from typing import List, Dict


def read_prompt_file(prompt_path: str) -> List[str]:
    prompts = []
    with open(prompt_path, 'r') as prompt_file:
        for line in prompt_file.readlines():
            prompts.append(line.strip())
    return prompts


def draw_prompt(prompt_path: str, prompt_num: int = 1) -> List[str]:
    prompts = read_prompt_file(prompt_path)
    return random.choices(prompts, k=prompt_num)


def analyze_prompt_list(prompt_list: List[str]) -> Dict[str, List[str]]:
    json_dict = {
        "adjectives": [],
        "nouns": [],
        "verbs": [],
        "adverbs": []
    }
    nlp = spacy.load("en_core_web_lg")
    for prompt in prompt_list:
        analyzed = nlp(prompt.lower())
        for token in analyzed:
            if token.dep_ == 'ROOT':
                if token.pos_ == 'ADJ':
                    json_dict['adjectives'].append(prompt)
                elif token.pos_ == 'VERB':
                    json_dict['verbs'].append(prompt)
                elif token.pos_ in ['ADV', 'ADP']:
                    json_dict['adverbs'].append(prompt)
                elif token.pos_ in ['NOUN', 'PROPN']:
                    json_dict['nouns'].append(prompt)
    return json_dict


def read_json_file(json_path):
    with open(json_path, 'r+') as json_file:
        json_dict = json.loads(json_file.read())
    return json_dict


def draw_prompt_from_json(
        json_dict: Dict[str, List[str]],
        with_adjective: bool = False) -> str:
    noun = random.choice(json_dict.get("nouns"))
    if with_adjective:
        adjective = random.choice(json_dict.get("adjectives"))
        return f"{adjective} {noun}"
    return noun


if __name__ == '__main__':
    json_file = "/home/juliette/Projects/drawing/data/prompts/analyzed_prompts.json"
    print(draw_prompt_from_json(read_json_file(json_file), True))