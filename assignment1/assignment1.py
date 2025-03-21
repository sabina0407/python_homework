# Write your code here.

# Write your code here.

# Task 1: Hello
def hello():
    return "Hello!"

# Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

# Task 3: Calculator
def calc(a, b, c = "multiply"):
    try:
        match c:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

# Task 4: Data Type Conversion

def data_type_conversion(value, type):
    try:
        if type == "int":
            return int(value)
        elif type == "float":
            return float(value)
        elif  type == "str":
            return str(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."

# Task 5: Grading System, using *args

def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except:
        return "Invalid data was provided."

# Task 6: Use a For Loop with a Range

def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

# Task 7: student Scores, Using **kwargs

def student_scores(type, **kwargs):
    if type == "best":
        best_student = max(kwargs, key=kwargs.get)
        return best_student
    elif type == "mean":
        scores = kwargs.values()
        return sum(scores) / len(scores)
    else:
        return None

# Task 8: Titleize, with String and List Operations

def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    
    words = string.split()
    words[0] = words[0].capitalize()
    words[-1] = words[-1].capitalize()

    for i, word in enumerate(words[1:-1], start=1):
        if word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()

    return " ".join(words)

# Task 9: Hangman, with more String Operations

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result


# Task 10: Pig Latin, Another String Manipulation Exercise

def pig_latin(sentence):
    vowels = {"a", "e", "i", "o", "u"}
    result = []

    try:
        if not sentence:
            return ""

        words = sentence.lower().split()

        for word in words:
            if word[0] in vowels:
                result.append(word + "ay")
            elif word.startswith("qu"):
                result.append(word[2:] + "quay")
            elif word[1:3] == "qu":
                result.append(word[3:] + word[:3] + "ay")
            else:
                for i, letter in enumerate(word):
                    if letter in vowels:
                        result.append(word[i:] + word[:i] + "ay")
                        break
                else:
                    result.append(word + "ay")

        return " ".join(result) 

    except Exception as e:
        return f"An error occurred: {str(e)}"