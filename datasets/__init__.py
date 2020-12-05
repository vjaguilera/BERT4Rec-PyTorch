from .ml_1m import ML1MDataset
from .meli import MELIDataset

DATASETS = {
    ML1MDataset.code(): ML1MDataset,
    MELIDataset.code(): MELIDataset
}


def dataset_factory(args):
    dataset = DATASETS[args.dataset_code]
    return dataset(args)
