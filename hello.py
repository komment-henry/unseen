def hello(name):
    """
    This function prints "Hello <name>" to the console and returns the integer
    value 0.

    Args:
        name (str): The `name` input parameter is not used anywhere inside the
            `hello` function. It is simply printed as part of the greeting message.

    Returns:
        int: The output returned by the `hello` function is `0`.

    """
    print "Hello", name
    return 0

if __name__ == "__main__":
    hello("world")

