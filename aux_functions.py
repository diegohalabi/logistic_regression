def inverse_logit(x):
    """
    Inverse logit function

    Parameters
    ----------
    x : float
        Value to be transformed

    Returns
    -------
    float
        Transformed value
    """
    import numpy as np
    return 1 / (1 + np.exp(-x))


def param_mean(param, model, data):
    """
    Calculates the mean of a parameter in a model.

    Parameters
    ----------
    param : str
        The parameter to be calculated.
    model : str
        The model to be used.
    data : DataFrame
        The data to be used.

    Returns
    -------
    float
        The mean of the parameter.

    """
    return model.params[param] * data[param].mean()