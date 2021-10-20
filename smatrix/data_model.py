"""Define a model."""
from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class DataModel:
    """Define data model."""

    file1: Optional[str] = None
    file2: Optional[str] = None
    paras1: Optional[List[str]] = field(default_factory=list)
    paras2: Optional[List[str]] = field(default_factory=list)
    sents1: Optional[List[str]] = field(default_factory=list)
    sents2: Optional[List[str]] = field(default_factory=list)
    smartrix_p = None
    smartrix_s = None
    paras_ali = None
    sents_ali = None
    options: Optional[dict] = field(default_factory=dict)


if __name__ == "__main__":
    from icecream import ic

    dm = DataModel(paras1=None)

    ic(dm)
