import os
import zipfile

#unzip the dataset
local_zip = '../datasets/rockPaperScissors/rps.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('../datasets/rockPaperScissors/')
zip_ref.close()

#unzip training data
local_zip = '../datasets/rockPaperScissors/rps-test-set.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('../datasets/rockPaperScissors/')
zip_ref.close()

