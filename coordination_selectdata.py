import json
import pandas as pd
import numpy as np
import matplotlib as plt
import glob
import csv
import os
import os

os.chdir(r'-jsonファイルを保存しているフォルダを指定-')


def getFileName(path):
    filelist = glob.glob(path + "/*")
    return filelist

def getSpecificData(filelist):
    for i in range(len(filelist)):
        with open(filelist[i]) as f:
            data = json.load(f)
            data = np.array(data['people'][0]['pose_keypoints_2d']).reshape(-1,3)
        df = pd.DataFrame(data, columns=['X','Y','P'], index=["Nose", "Neck", "RShoulder", "RElbow", "RWrist", "LShoulder", "LElbow", "LWrist", "MidHip", "RHip", \
            "RKnee", "RAnkle", "LHip", "LKnee", "LAnkle", "REye", "LEye", "REar", "LEar", "LBigToe", "LSmallToe", "LHeel", "RBigToe", "RSmallToe", "RHeel"])

        # 自分の必要なデータを取り出す
        writeCSV([float(df.at["LKnee", "X"]), float(df.at["LKnee", "Y"])])


def writeCSV(data):
    with open('gait_sample_output.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\n') 
        writer.writerow(data)

def main():
    filelist = getFileName(input("JSONのディレクトリのパスを入力:　"))
    with open('gait_sample_output.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n') 
        # 自分の必要なデータの列の名前を用意。上のデータと同じだけの列数を揃える。
        writer.writerow(["LKnee_X","LKnee_Y"])
    getSpecificData(filelist)

if __name__ == '__main__':
    main()