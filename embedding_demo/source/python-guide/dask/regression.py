import dask.array as da
from distributed import Client, LocalCluster
from sklearn.datasets import make_regression

import lightgbm as lgb

if __name__ == "__main__":
    print("loading data")

    X, y = make_regression(n_samples=1000, n_features=50)

    print("initializing a Dask cluster")

    cluster = LocalCluster(n_workers=2)
    client = Client(cluster)

    print("created a Dask LocalCluster")

    print("distributing training data on the Dask cluster")

    dX = da.from_array(X, chunks=(100, 50))
    dy = da.from_array(y, chunks=(100,))

    print("beginning training")

    dask_model = lgb.DaskLGBMRegressor(n_estimators=10)
    dask_model.fit(dX, dy)
    assert dask_model.fitted_

    print("done training")
