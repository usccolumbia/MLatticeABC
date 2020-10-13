
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

	x = pd.read_csv('cubic_train_test.csv').iloc[:,5:].fillna(0).values #cubic
	y = pd.read_csv('cubic_train_test.csv').iloc[:,2].fillna(0).values 

	x_train, x_test, y_train, y_test  = train_test_split(x,y,test_size=0.1)

	forest=RandomForestRegressor(n_estimators=50,criterion='mse',n_jobs=-1)

	forest.fit(x_train,y_train)
	y_pred=forest.predict(x_test)
	ytp = forest.predict(x_train)
	r2 = r2_score(y_test, y_pred)
	mae = mean_absolute_error(y_test, y_pred)
	mse = mean_squared_error(y_test,y_pred)
	rmse = np.sqrt(mse)
	ls_r2.append(r2)
	ls_mae.append(mae)
	ls_rmse.append(rmse)
	print(i)
	print('r2:',r2,'mae:',mae,'rmse:',rmse)

print('r2:  ',np.mean(ls_r2), np.std(ls_r2,ddof=1))
print('mae: ',np.mean(ls_mae), np.std(ls_mae,ddof=1))
print('rmse:',np.mean(ls_rmse), np.std(ls_rmse,ddof=1))
