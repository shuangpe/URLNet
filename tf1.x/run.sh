conda create -y -n URLNet python=3.7
conda activate URLNet
pip install -U pip
pip install tensorflow==1.15.0 protobuf==3.20.0 tqdm tflearn

python3 train.py --data.data_dir ../dataset/train_10000.txt
