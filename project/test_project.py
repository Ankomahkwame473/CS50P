from project import display_knust_results, display_other_results, calculate_grade

def test_calculate_grade():
    assert calculate_grade("knust", [73, 66, 80, 91, 72, 70, 66], [2, 2, 3, 3, 2, 4, 2]) == (["A", "B", "A", "A", "A", "A", "B"], ["Excellent", "Very Good", "Excellent", "Excellent", "Excellent", "Excellent", "Very Good"], 'First Class', 74.83333333333333, [])

def test_display_other_results():
     assert display_other_results(['science', 'maths'], [2, 3], [80, 90], ['A', 'A'], ['Excellent', 'Excellent'], [4, 4]) == ([['science', 2, 80, 4, 'A', 'Excellent'], ['maths', 3, 90, 4, 'A', 'Excellent']], ['Course Name', 'Credits', 'Mark', 'Grade Point', 'Grade', 'Interpretation'])

def test_display_knust_results():
    assert display_knust_results(['science', 'maths'], [2, 3], [80, 90], ['A', 'A'], ['Excellent', 'Excellent']) == ([['science', 2, 80, 'A', 'Excellent'], ['maths', 3, 90, 'A', 'Excellent']], ['Course Name', 'Credits', 'Mark', 'Grade', 'Interpretation'])
