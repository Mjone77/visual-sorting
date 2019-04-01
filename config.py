# Config variables
_settings = {
    ### Lists ###
    'NUM_ELEMENTS': 500,            # Number of elements to generate for the random list
    'MIN_ELEMENT_VALUE': 0,         # Minimum value of the elements in the generated list
    'MAX_ELEMENT_VALUE': 99999,     # Maximum value of the elements in the generated list
    'ENUM_LIST': True,              # True: Generate list with elements that equal their indexes then shuffle. Ignores min/max values. False: Generate list with random numbers between min and max.
    ### Sorts to perform ###
    'DO_CONCAVE': False,             # Concave sort
    'DO_QUICK': True,              # Quick sort
    ### Sorting Attributes ###
    'QUICK': {
        'pivot_method': 'median'    # 'first', 'last', 'middle', or 'median' of the three
    },
    ### Debug ###
    'VERBOSE': False,               # Increases output
}

def config(setting):
    try:
        return _settings[setting]
    except:
        raise Exception("{} is not a valid config option.".format(setting))