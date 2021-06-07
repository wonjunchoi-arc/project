from dataclasses import dataclass


@dataclass
class Dataset(object):
    context: str # 파일이 존재하는 경로 ./data/
    fname: str   # 얘가 KB_housing
    house: object

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def house(self) -> str: return self._house

    @house.setter
    def house(self, house): self._house = house


