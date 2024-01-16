def hello(name):
    """
    The function `hello(name)` prints "Hello [name]" and returns 0.

    Args:
        name (str): In the `hello` function given above the `name` parameter is
            an argument that is passed to the function whenever it is called.

    Returns:
        int: The output returned by the function "hello" is 0.

    """
    print "Hello", name
    return 0

if __name__ == "__main__":
    hello("world")
