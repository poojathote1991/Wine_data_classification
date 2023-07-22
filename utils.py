import numpy as np
import pickle
import config

class WindData():
    def __init__(self,Alcohol,Malic_acid,Ash,Acl,Mg,Phenols,Flavanoids
                     ,Nonflavanoid_phenols,Proanth,Color_int,Hue,OD,Proline):
        print("**************INIT FUNCTION*****************")
        self.Alcohol=Alcohol
        self.Malic_acid=Malic_acid
        self.Ash=Ash
        self.Acl=Acl
        self.Mg=Mg
        self.Phenols=Phenols
        self.Flavanoids=Flavanoids
        self.Nonflavanoid_phenols=Nonflavanoid_phenols
        self.Proanth=Proanth
        self.Color_int=Color_int
        self.Hue=Hue
        self.OD=OD
        self.Proline=Proline
    def __load_saved_data(self):
        model_file_name=config.MODEL_FILE_PATH
        with open(model_file_name,'rb') as f:
            self.model=pickle.load(f)

    def get_predicted_class(self):
        
        self.__load_saved_data()
        test_array=np.zeros([1,self.model.n_features_in_])
        test_array[0,0]=self.Alcohol
        test_array[0,1]=self.Malic_acid
        test_array[0,2]=self.Ash
        test_array[0,3]=self.Acl
        test_array[0,4]=self.Mg
        test_array[0,5]=self.Phenols
        test_array[0,6]=self.Flavanoids
        test_array[0,7]=self.Nonflavanoid_phenols
        test_array[0,8]=self.Proanth
        test_array[0,9]=self.Color_int
        test_array[0,10]=self.Hue
        test_array[0,11]=self.OD
        test_array[0,12]=self.Proline
        predicted_class=self.model.predict(test_array)
        print("predicted_class is : ",predicted_class)
        return predicted_class