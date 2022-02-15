from ML_Pipeline import json_spacy
from ML_Pipeline import utils


train= json_spacy.convert_data_to_spacy("C:\\Users\\Bouch\\PycharmProjects\\resumeParser\\input\\training\\Entity Recognition in Resumes.json")

# print(train[0])
print('Done! Converted into json format!')

print('checking if model exists')

model = utils.check_existing_model('model')
