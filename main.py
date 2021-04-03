def log_message(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("decorator_logs.txt.", 'a') as f:
            f.write(result+"\n")

        print(result)
        return result

    return wrapper


@log_message
def a_function_that_returns_a_string():
    return "a string"


@log_message
def a_function_that_returns_a_strings_with_a_newline(s):
    return "{}\n".format(s)


@log_message
def a_function_that_returns_another_string(string=""):
    return "Another string"


a = a_function_that_returns_a_string()
b = a_function_that_returns_a_strings_with_a_newline('Python string')
c = a_function_that_returns_another_string()
