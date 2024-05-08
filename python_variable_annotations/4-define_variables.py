""" Define variables"""
a = 1
pi = 3.14
i_understand_annotations = True
school = "Holberton"

"""Function to annotate variables"""
def annotate_variables():
    """Annotate variables with their respective types"""
    annotations = {
        'a': (a, int),
        'pi': (pi, float),
        'i_understand_annotations': (i_understand_annotations, bool),
        'school': (school, str)
    }
    """Return annotations"""
    return annotations

