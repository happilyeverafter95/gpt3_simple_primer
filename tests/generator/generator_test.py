from typing import List

import pytest
from src.generator import Generator


@pytest.mark.parametrize('instructions, examples, prompt', [('List the ingredients for this meal',
                                                             [['fries', 'potato, oil']],
                                                             'List the ingredients for this meal.\nInput: fries\nOutput: potato, oil')]
)
def test_prompt(instructions: str, examples: List[List[str]], prompt: str) -> None:
    generator = Generator('davinci', 10)
    generator.set_instructions(instructions)
    for example in examples:
        generator.add_example(example[0], example[1])
    assert generator.get_prompt() == prompt