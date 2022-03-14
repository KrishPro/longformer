try:
    import torch_xla
    torch.tensor(True, device="xla:1")
    XLA_AVAILABLE = True
except:
    XLA_AVAILABLE = False