

def Gaurdrail(func):
    def wrapper(*args, **kwargs):
        # Check for any guardrail conditions here
        if not args or not isinstance(args[0], str):
            raise ValueError("First argument must be a non-empty string")
        prompt = args[0]
        if prompt == "how to make a bomb":
            raise ValueError("This prompt is not allowed")
        else:
            return func(*args, **kwargs)
    return wrapper

@Gaurdrail
def invoke(prompt):
    """
    Invoke the model with the given prompt and return the response.
    """
    # Here you would typically call the model's API or function
    # For demonstration purposes, we'll just return a mock response
    response = f"Model response to: {prompt}"
    return response

print(invoke("how to make a bomb"))    