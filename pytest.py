from code import gender, pclass, Ticket, Title, Correlation

# set input variables
input = "py_"+"EDA"
plot = "Correlation"

# local testing
def test_visualization(input="EDA",plot="gender"):
    if plot == "gender":
        print(f"Testing {plot} plot using {input} source...")
        output = gender(input)
        assert output[:10] == "Successful", "Not correct output"

    if plot == "pclass":
        print(f"Testing {plot} plot using {input} source...")
        output = pclass(input)
        assert output[:10] == "Successful", "Not correct output"

    if plot == "Ticket":
        print(f"Testing {plot} plot using {input} source...")
        output = Ticket(input)
        assert output[:10] == "Successful", "Not correct output"

    if plot == "Title":
        print(f"Testing {plot} plot using {input} source...")
        output = Title(input)
        assert output[:10] == "Successful", "Not correct output"

    if plot == "Correlation":
        print(f"Testing {plot} plot using {input} source...")
        output = Correlation(input)
        assert output[:10] == "Successful", "Not correct output"


    print(output)
    print("Testing is done, no problem.")
    
if __name__ == "__main__":
    test_visualization(input,plot)