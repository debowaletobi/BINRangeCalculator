from flask import Flask, render_template, request
from Models.CardBinOptimization import OptimizeBinRanging

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html")


def add_commas(number):
    """
    Adds appropriate commas to an integer.
    
    Args:
    - number (int): The integer to which commas will be added.
    
    Returns:
    - str: The integer with commas added.
    """
    # Convert the integer to a string and split it into groups of three from the right
    number_str = str(number)
    parts = []
    while number_str:
        parts.append(number_str[-3:])
        number_str = number_str[:-3]
    # Join the groups with commas and return the result
    return ','.join(reversed(parts))

@app.route("/calculate", methods=["POST", "GET"])
def result():
    if request.method == 'POST':
        inputs = request.form.to_dict() 
        lower_bin_bound = int(inputs.get("lower bin bound", 0))
        upper_bin_bound = int(inputs.get("upper bin bound", 0))
        pan_length = int(inputs.get("pan length", 16))

        try:
            card_no = OptimizeBinRanging(lower_bin_bound, upper_bin_bound, pan_length).no_cards_possible
            card_no = f"{add_commas(card_no)} cards"
        except Exception as e:
            print("Error:", str(e))
            card_no = e
		
        post_lower_bin_bound = inputs.get("lower bin bound", '')
        post_upper_bin_bound = inputs.get("upper bin bound", '')
        post_pan_length = inputs.get("pan length", 16)
        

        return render_template("index.html", card_no=card_no,
                               post_lower_bin_bound=post_lower_bin_bound,
                               post_upper_bin_bound=post_upper_bin_bound,
                               post_pan_length=post_pan_length)

    # If it's a GET request, simply render the template
    return render_template("index.html", pan_length)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
	