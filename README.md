# Extract-text-from-the-images
# Aim
To build a CRNN network that can predict the single-line text in a given image.

# Dataset
TRSynth100k Images : https://www.kaggle.com/eabdul/textimageocr/tasks

# Approach

- Importing the required libraries
- Download the required dataset
### Pre-processing
- Find null values and replace those missing values with string “null”
- Create a data frame with image path and corresponding labels (save as csv file)
- Create a mapping from characters to integer and save in pickle format(char2int.pkl)
- Create a mapping from integer to character and save in pickle format (int2char.pkl)
### Define configurations paths
### Training the model
- Split the data into train and validation
- Create train and validation datasets
- Define the loss function
- Create the model object
- Define the optimizer
- Training loop
- Save the trained model
### Predictions
= Select image for prediction
= Apply augmentations
- Take the model output
- Apply softmax and take label predictions
- Use the ‘ph’ string character and convert integer predictions to string
- Display the output
