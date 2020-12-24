import numpy as np
import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

ls_r2=[]
ls_mae = []
ls_rmse = []
for i in range(10):
	print(i)
	x = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[106952:,11:].fillna(0).values #cubic
	y = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[106952:,4].fillna(0).values #137 255
	# x = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[:15297,11:].fillna(0).values #1-2
	# y = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[:15297,4].fillna(0).values
	# x = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[15297:45169,11:].fillna(0).values #3-15
	# y = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[15297:45169,4].fillna(0).values
	# x = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[45169:71969,11:].fillna(0).values #16-74
	# y = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[45169:71969,4].fillna(0).values 
	# x = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[71969:86623,11:].fillna(0).values #75-142
	# y = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[71969:86623,4].fillna(0).values 
	# x = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[86623:97709,11:].fillna(0).values #143-167
	# y = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[86623:97709,4].fillna(0).values
	# x = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[97709:106952,11:].fillna(0).values #169-194
	# y = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[97709:106952,4].fillna(0).values
	# x = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[:,11:].fillna(0).values #all
	# y = pd.read_csv('Element_atom_no_stat+Enhanced_magpie.csv').iloc[:,4].fillna(0).values

	x_train, x_test, y_train, y_test  = train_test_split(x,y,test_size=0.1)

	forest=RandomForestRegressor(n_estimators=50,
								 # min_samples_split=10,
	                             criterion='mse',
	                             # min_samples_leaf=2,
	                             n_jobs=-1)

	forest.fit(x_train,y_train)
	y_pred=forest.predict(x_test)
	r2 = r2_score(y_test, y_pred)
	mae = mean_absolute_error(y_test, y_pred)
	mse = mean_squared_error(y_test,y_pred)
	rmse = np.sqrt(mse)
	ls_r2.append(r2)
	ls_mae.append(mae)
	ls_rmse.append(rmse)
	print(r2)


print(np.mean(ls_r2), '+-' ,np.std(ls_r2,ddof=1))
print(np.mean(ls_mae), '+-' ,np.std(ls_mae,ddof=1))
print(np.mean(ls_rmse), '+-' ,np.std(ls_rmse,ddof=1))
