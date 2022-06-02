from code import gender, pclass, Ticket, Title, Correlation

# set input variables
input = "EDA"

# local testing
def test_visualization():
    print(f"Testing pclass using {input}...")
    assert pclass(input) == "Successful! Figure saved to \"/data/pclass{source}.png\"", "Not correct output"

    
if __name__ == "__main__":
    test_visualization()