def safe_subtract(a, b):
    """
    Subtracts the second value from the first, handling type errors.
    """
    try:
        return a - b                 
    except TypeError:
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None                  

print(safe_subtract(250, 28))            #222
print(safe_subtract(75, 331))            #-256
print(safe_subtract(8, "DataScience"))   #None
print(safe_subtract([84,5], [22]))       #None
