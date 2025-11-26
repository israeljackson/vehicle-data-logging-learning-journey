def temp_convert(value, from_unit=None, to_unit=None):
    """
    Converts a temperature 'value' from one unit ('C', 'F', 'K') 
    to another unit ('C', 'F', 'K').

    Args:
        value (float/int): The temperature value to convert.
        from_unit (str, optional): The unit of the input value (e.g., 'C'). Defaults to None.
        to_unit (str, optional): The unit to convert to (e.g., 'F'). Defaults to None.

    Returns:
        float: The converted temperature value.

    Raises:
        ValueError: If a unit is invalid, or if the temperature is below absolute zero.
    """

     #convert given temperature
    def k_to_c(t):
        """From kelvin to celsius"""
        return t - 273.15
    
    def c_to_k(t):
        """From celcuis to kelvin"""
        return t + 273.15

    def c_to_f(t):
        """From celcius to ferenheit"""
        return ((9/5) * t) + 32  
    
    def f_to_c(t):
        """From farenheit to celsius"""
        return (5/9) * (t - 32)
    
    def f_to_k(t):
        """From farenheit to kelvin"""
        return (t - 32) * (5/9) + 273.15
    
    def k_to_f(t):
        """From kelvin to farenheit"""
        return (t - 273.15) *(9/5) + 32
    
    if from_unit is None or to_unit is None:
        raise ValueError("Both 'from_unit' and 'to_unit' must be specified.")
    
    #handle uppercase inputs
    from_temp = from_unit.lower()
    to_temp = to_unit.lower()

    #manage temoeratures below absolute zero
    if (value < -273.15 and from_temp == 'c') or \
        (value < 0 and from_temp == 'k') or \
        (value < -459.67 and from_temp == 'f'):
        raise ValueError("Input temperature is below absolute zero.")
    
    if from_temp == to_temp:
        return value
    elif from_temp == 'c' and to_temp == 'k':
        return c_to_k(value)  
    elif from_temp == 'k' and to_temp == 'c':
        return k_to_c(value)  
    elif from_temp == 'c' and to_temp == 'f':
        return c_to_f(value)  
    elif from_temp == 'f' and to_temp == 'c':
        return f_to_c(value)  
    elif from_temp =='f' and to_temp == 'k':
        return f_to_k(value)
    elif from_temp == 'k' and to_temp == 'f':
        return k_to_f(value)
    else:
        raise ValueError("Invalid unit entered. Units must be 'C', 'F', or 'k'")

result = temp_convert(273.15, from_unit='k', to_unit='c')
print(f"273.15 k is {result}c")