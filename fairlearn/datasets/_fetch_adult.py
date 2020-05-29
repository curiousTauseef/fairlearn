import os

from sklearn.datasets import fetch_openml


def fetch_adult(*, version='1', cache=True, data_home=None,
                as_frame=False, return_X_y=False):
    """Load the UCI Adult dataset (binary classification).

    Download it if necessary.

    ==============   ==============
    Samples total             48842
    Dimensionality               14
    Features                   real
    Classes                       2
    ==============   ==============

    Source: https://archive.ics.uci.edu/ml/datasets/Adult
    Ronny Kohavi and Barry Becker, "Scaling Up the Accuracy of Naive-Bayes
    Classifiers: a Decision-Tree Hybrid", Proceedings of the Second
    International Conference on Knowledge Discovery and Data Mining, 1996

    Prediction task is to determine whether a person makes over $50,000 a
    year.

    Parameters
    ----------
    version : integer or 'active', default='active'
        Version of the dataset. Can only be provided if also ``name`` is given.
        If 'active' the oldest version that's still active is used. Since
        there may be more than one active version of a dataset, and those
        versions may fundamentally be different from one another, setting an
        exact version is highly recommended.

    cache : boolean, default=True
        Whether to cache downloaded datasets using joblib.

    data_home : optional, default: None
        Specify another download and cache folder for the datasets. By default
        all scikit-learn data is stored in '~/fairlearn_data' subfolders.

    as_frame : boolean, default=False
        If True, the data is a pandas DataFrame including columns with
        appropriate dtypes (numeric, string or categorical). The target is
        a pandas DataFrame or Series depending on the number of target_columns.
        The Bunch will contain a ``frame`` attribute with the target and the
        data. If ``return_X_y`` is True, then ``(data, target)`` will be pandas
        DataFrames or Series as describe above.

    return_X_y : boolean, default=False.
        If True, returns ``(data.data, data.target)`` instead of a Bunch
        object.

    Returns
    -------
    dataset : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : ndarray, shape (48842, 14)
            Each row corresponding to the 14 feature values in order.
            If ``as_frame`` is True, ``data`` is a pandas object.
        target : numpy array of shape (48842,)
            Each value represents whether the person earns more than $50,000
            a year (1) or not (0).
            If ``as_frame`` is True, ``target`` is a pandas object.
        feature_names : list of length 14
            Array of ordered feature names used in the dataset.
        DESCR : string
            Description of the UCI Adult dataset.

    Notes
    -----
    This dataset consists of 48842 samples and 14 features.
    """
    if data_home is None:
        data_home = os.path.join(os.path.expanduser('~'), "fairlearn_data")

    return fetch_openml(
        data_id=1590,
        data_home=data_home,
        # version=version,
        cache=cache,
        as_frame=as_frame,
        return_X_y=return_X_y,
    )
