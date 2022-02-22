from transformers.configuration_utils import PretrainedConfig
from transformers.utils import logging 

logger = logging.get_logger(__name__)

class Top2VecConfig(PretrainedConfig):
    r"""
    :class:`Top2VecConfig` is the configuration class to store the configuration of a
    :class:`~Top2VecModel`. It is used to instantiate a Top2Vec model according to the 
    specified arguments, defining the defining the model architecture.

    Configuration objects inherit from :class:`~transformers.PretrainedConfig` and can be
    used to control the model outputs. Read the documentation from
    :class:`~transformers.PretrainedConfig` for more information.
    """
    pass