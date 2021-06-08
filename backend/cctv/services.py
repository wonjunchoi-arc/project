from cctv.models import CctvDTO
from common.services import CommonServices
import pandas as pd

class CctvService(CommonServices):

    dto = CctvDTO()

    def new_model(self, payload):
        this = self.dto
        this.context = './data/'
        this.fname = payload  # train.csv
        return pd.read_csv(this.context + this.fname)

    def new_model_excel(self, payload):
        this = self.dto
        this.context = './data/'
        this.fname = payload  # train.csv
        return pd.read_excel(this.context + this.fname)


