from matminer.featurizers.conversions import StrToComposition
from matminer.featurizers.composition import ElementProperty
from matminer.featurizers.base import MultipleFeaturizer
from matminer.featurizers import composition as cf
from matminer.featurizers.conversions import StrToComposition
from pymatgen.core.composition import Composition
import numpy as np 
import pandas as pd 
import bz2 
import _pickle as cPickle
import argparse

feature_calculators = MultipleFeaturizer([
    cf.ElementProperty.from_preset(preset_name="magpie"),
    cf.Stoichiometry(),
    cf.ValenceOrbital(props=['frac']),
    cf.IonProperty(fast=True),
    cf.BandCenter(),
    cf.ElementFraction(),
    ])

def generate(fake_df, ignore_errors=False):
    fake_df = np.array([fake_df])
    fake_df = pd.DataFrame(fake_df)
    fake_df.columns = ['full_formula']
    # print(fake_df)
    fake_df = StrToComposition().featurize_dataframe(fake_df, "full_formula", ignore_errors=ignore_errors)
    fake_df = fake_df.dropna()
    fake_df = feature_calculators.featurize_dataframe(fake_df, col_id='composition', ignore_errors=ignore_errors);
    fake_df["NComp"] = fake_df["composition"].apply(len)
    return fake_df

def mlmd(x):
	ls = []
	comp=Composition(x)
	most=comp.num_atoms
	data=np.array(list(comp.as_dict().values()))
	l = len(data)
	s = sum(data)
	a = max(data)
	i = min(data)
	m = np.mean(data)
	v = np.var(data)
	ls.append([most,a,i,m,v,l])
	df = pd.DataFrame(ls)
	return(df)

def decompress_pickle(file): 
  data = bz2.BZ2File(file, 'rb') 
  data = cPickle.load(data) 
  return data

def main():

    print('----------Predicting----------')
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--formula',  type=str, 
                        help="The input crystal formula.")
    parser.add_argument('-s','--crystal_system',  type=str, default='crystal',
                        help="The input crystal system.")
    args = parser.parse_args()
    form = args.formula
    system = args.crystal_system
    ext_magpie = generate(form)
    m = mlmd(form)
    result = ext_magpie.join(m)
    result = result.drop(['MagpieData minimum SpaceGroupNumber','MagpieData maximum SpaceGroupNumber','MagpieData range SpaceGroupNumber','MagpieData mean SpaceGroupNumber','MagpieData avg_dev SpaceGroupNumber','MagpieData mode SpaceGroupNumber'],axis=1)
    result = result.iloc[:,2:]
    dirs = 'Model'
    if system == 'crystal' :
        a =  decompress_pickle(dirs+'/Crystal_a.pbz2')
        b =  decompress_pickle(dirs+'/Crystal_b.pbz2')
        c =  decompress_pickle(dirs+'/Crystal_c.pbz2')
        a = a.predict(result)
        b = b.predict(result)
        c = c.predict(result)
        print('a=',a[0],'b=',b[0],'c=',c[0])
    if system == 'cubic' or  system == 'Cubic':
        forest = decompress_pickle(dirs+'/Cubic.pbz2') #  python predict.py -i K12Mn16O32  -s cubic
        y_pred = forest.predict(result)
        print('a=b=c=',y_pred[0])
    if system == 'hexagonal' or system == 'Hexagonal':
        a = decompress_pickle(dirs+'/Hexagonal_a.pbz2') 
        c = decompress_pickle(dirs+'/Hexagonal_c.pbz2')
        a = a.predict(result)
        c = c.predict(result)
        print('a=b=',a[0],'c=',c[0])
    if system == 'trigonal' or system == 'Trigonal':
        a = decompress_pickle(dirs+'/Trigonal_a.pbz2')
        c = decompress_pickle(dirs+'/Trigonal_c.pbz2')
        a = a.predict(result)
        c = c.predict(result)
        print('a=b=',a[0],'c=',c[0])
    if system == 'tetragonal' or system == 'Tetragonal':
        a = decompress_pickle(dirs+'/Tetragonal_a.pbz2')
        c = decompress_pickle(dirs+'/Tetragonal_c.pbz2')
        a = a.predict(result)
        c = c.predict(result)
        print('a=b=',a[0],'c=',c[0])
    if system == 'orthorhombic' or system == 'Orthorhombic':
        a = decompress_pickle(dirs+'/Orthorhombic_a.pbz2')
        b = decompress_pickle(dirs+'/Orthorhombic_b.pbz2')
        c = decompress_pickle(dirs+'/Orthorhombic_c.pbz2')
        a = a.predict(result)
        b = b.predict(result)
        c = c.predict(result)
        print('a=',a[0],'b=',b[0],'c=',c[0])
    if system == 'monoclinic' or system == 'Monoclinic':
        a = decompress_pickle(dirs+'/Monoclinic_a.pbz2')
        b = decompress_pickle(dirs+'/Monoclinic_b.pbz2')
        c = decompress_pickle(dirs+'/Monoclinic_c.pbz2')
        a = a.predict(result)
        b = b.predict(result)
        c = c.predict(result)
        print('a=',a[0],'b=',b[0],'c=',c[0])
    if system == 'triclinic' or system == 'Triclinic':
        a = decompress_pickle(dirs+'/Triclinic_a.pbz2')
        b = decompress_pickle(dirs+'/Triclinic_b.pbz2')
        c = decompress_pickle(dirs+'/Triclinic_c.pbz2')
        a = a.predict(result)
        b = b.predict(result)
        c = c.predict(result)
        print('a=',a[0],'b=',b[0],'c=',c[0])
    print('-----------Complete-----------')

if __name__ == "__main__":
	main()
