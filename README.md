## MLatticeABC: Machine learning for crystal lattice constant (a,b,c) prediction


## Premise

MLatticeABC is a random forest machine learning model with a new feature set combined with the standard composition features such as Magpie descriptors for effective lattice constant prediction. 

If you find our software is useful, please cite it as:<br >

#### Yuxin Li, Wenhui Yang, Rongzhi Dong, Jianjun Hu*, MLatticeABC: Generic Lattice Constant Prediction of Inorganic Materials using Machine Learning, Arxiv. 2020

Developed in 2020.9-10 at <br />
School of Mechanical Engineering<br />
Guizhou University, Guiyang, China <br />

Machine Learning and Evolution Laboratory<br />
Department of Computer Science and Engineering<br />
University of South Carolina, Columbia, USA<br />


## Performance on Materials Project dataset

Prediction performance of MLatticeABC  in terms of R2 score for a,b,c over different crystal systems （10 repeats of random split 9:1)
|Crystal system|train set size  |  test set size |      a       |    b         |       c      |
|-------------|----------------|---------------|-------------|-------------|-------------|
Cubic         | 16492          | 1833          | 0.979±0.016 |             |             | 
Hexagonal     | 8318           | 925           | 0.892±0.019 |             | 0.760±0.061 |
Trigonal      | 9977           | 1109          | 0.843±0.025 |             | 0.705±0.065 |
Tetragonal    | 13188          | 1466          | 0.846±0.024 |             | 0.685±0.044 |
Orthorhombic  | 24120          | 2681          | 0.770±0.019 | 0.579±0.074 | 0.638±0.028 |
Monoclinic    | 26884          | 2988          | 0.520±0.021 | 0.507±0.016 | 0.489±0.029 |
Triclinic     | 13767          | 1530          | 0.800±0.022 | 0.771±0.014 | 0.650±0.056 |
<!--- img src="performance1.png" width="800"--->

## Environment Setup

To use `MLatticeABC` you need to create an environment with the correct dependencies. Using `Anaconda` this can be accomplished with the follow commands:

```bash
conda create --name mlatticeabc python=3.6
conda activate mlatticeabc
conda install --channel conda-forge pymatgen
pip install matminer
pip install scikit-learn==0.23.1
```

## MLatticeABC Setup

Once you have setup an environment with the correct dependencies you can install `mlatticeabc` using the following commands:

```bash
conda activate mlatticeabc
git clone https://github.com/usccolumbia/MLatticeABC
cd MLatticeABC
pip install -e .
```

Pre-trained models are stored in google drive. Download the file `model.zip` from from the [figshare](https://figshare.com/s/af11c43cdae7d239e4cf). After downing the file, copy it to `MLatticeABC` and extract it. the `Model` folder should be in the `MLatticeABC` directory after the extraction is completed.
## Example Use

In order to test your installation you can run the following example from your `MLatticeABC` directory:

```sh
cd /path/to/MLatticeABC/
python predict.py -i full_formula -s crystal_system

for example:
python predict.py -i Mn16Zn24Ge24O96 -s cubic
python predict.py -i Mn16Zn24Ge24O96
```

The following cyrstal_system values are accepted
```
crystal     # crystal system unknown.
cubic
hexagonal
trigonal
tetragonal
orthorhombic
monoclinic
triclinic
```

