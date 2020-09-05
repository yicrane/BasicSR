from basicsr.utils import get_root_logger
from basicsr.utils.registry import Registry

MODELS = Registry('models')


def create_model(opt):
    """Create model.

    Args:
        opt (dict): Configuration. It constains:
            model_type (str): Model type.
    """
    model_type = opt['model_type']

    # dynamic instantiation: registry
    model_cls = MODELS.get(model_type)
    if model_cls is None:
        raise ValueError(f'Model {model_type} is not found or registered.')

    model = model_cls(opt)

    logger = get_root_logger()
    logger.info(f'Model [{model.__class__.__name__}] is created.')
    return model
