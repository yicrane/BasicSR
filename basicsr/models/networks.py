from basicsr.models.archs import ARCHS


# Generator
def define_net_g(opt):
    # dynamic instantiation: registry
    arch_type = opt.pop('type')
    arch_cls = ARCHS.get(arch_type)
    if arch_cls is None:
        raise ValueError(f'Arch {arch_type} is not found or registered.')

    net_g = arch_cls(**opt)
    return net_g


# Discriminator
def define_net_d(opt):
    # dynamic instantiation: registry
    arch_type = opt.pop('type')
    arch_cls = ARCHS.get(arch_type)
    if arch_cls is None:
        raise ValueError(f'Arch {arch_type} is not found or registered.')

    net_d = arch_cls(**opt)
    return net_d
