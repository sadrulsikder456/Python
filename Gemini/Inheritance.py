class BaseModel:
    def __init__(self,modelname):
        self.name=modelname
        print(f"The model name is :{self.name}")
    def train(self):
        print("The Model is training.....")
class DeepLearningModel(BaseModel):
    def AddLayer(self):
        print("New Neural Network layer added.")

dl_model=DeepLearningModel("DenseNet121")

dl_model.train()
dl_model.AddLayer()