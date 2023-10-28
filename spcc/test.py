import os
def left_factor(grammar):
    """
    Applies left factoring to a given grammar and returns the modified grammar.

    Parameters:
    grammar (str): A string representing the grammar.

    Returns:
    str: The modified grammar after applying left factoring.
    """
    productions = grammar.split("\n")
    nonterminals = set()

    # Extract nonterminals from the grammar
    for production in productions:
        nonterminal = production.split("->")[0].strip()
        nonterminals.add(nonterminal)

    # Apply left factoring to each nonterminal
    for nonterminal in nonterminals:
        # Find all productions for the current nonterminal
        productions_for_nonterminal = [
            production.strip() for production in productions if production.startswith(nonterminal)
        ]

        # Find the longest common prefix for the productions
        longest_common_prefix = os.path.commonprefix(productions_for_nonterminal)

        # If there is a longest common prefix, factor it out
        if longest_common_prefix:
            # Create a new nonterminal to represent the factored out prefix
            new_nonterminal = f"{nonterminal}'"

            # Update the grammar to include the new nonterminal and its productions
            grammar += f"\n{new_nonterminal} -> {longest_common_prefix}"

            # Update the original productions to use the new nonterminal and remove the prefix
            for i, production in enumerate(productions_for_nonterminal):
                if production.startswith(longest_common_prefix):
                    productions[i] = f"{nonterminal} -> {new_nonterminal} {production[len(longest_common_prefix):]}"

    # Return the modified grammar
    return "\n".join(productions)

grammar = """
S->iEtS
S->iEtSeS
S->a
"""

print(left_factor(grammar))