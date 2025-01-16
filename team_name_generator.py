"""
PRIMM: Team Name Generator
This program demonstrates a random team name generator. Some of the code reeks and some
is not bad. 

January 2025
"""

import random
from typing import List

def get_adjective() -> str:
    """
    Gets a random adjective for the team name. This is generally the first
    word in the name.
    
    Returns:
        str: a random adjective
    """
    rnd: int = random.randint(1, 10)
    
    if rnd == 1:
        return "lugubrious"

    if rnd == 2: 
        return "effulgent"
    
    if rnd == 3:
        return "inscrutable"

    if rnd == 4:
        return "ineffable"
    
    if rnd == 5:
        return "pernicious"
    
    if rnd == 6:
        return "highfalutin"
    
    if rnd == 8:
        return "fancy-dancy"
    
    if rnd == 9:
        return "melifluous"
    
    if rnd == 10:
        return "sesquipedalian"

def get_noun() -> str:
    """
    Write the doc string!
    """
        # create a list of words
    words: List[str] = ["serendipity", "zeitgeist", "perspicacity", "juxtaposition",
    "ineffability", "paradigm", "verisimilitude", "cacophony", "alacrity", "vicissitude"]

        # manually add fancier words
    words.append("surfeit")
    words.insert(0, "dearth")
    words.insert(3, "paucity")
        
        # do some replacing
    words[0] = "proclivity"
    words[-1] = "truculence"

        # What do I do?
    words.pop(1)
    words.remove("truculence")

    rnd: int = random.randint(1, 5)

    return words[rnd]

def main() -> None:
    adjective: str = get_adjective()
    noun: str = get_noun()

    print(f"{adjective} {noun}")

if __name__ == "__main__":
    main()