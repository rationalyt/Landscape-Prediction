
The project aims to identify the terrain from time series data received from devices like accelerometer, gyroscopic readings, etc. There are a number of input and output files for multiple sessions of each subject. 

                                Preprocessing

The function merge_files() takes the corresponding readings present in '_x' files which represents the readings of the subject recorded by accelerometer, gyrometer,etc  and the classes in '_y' files and merges them into a single dataframe. To match the frequencies of both the readings, the class values are repeated 4 times.

The dataframe returned by the merge_file() function is then standardised. The resulting data frame is then passed to the split_sequence_slide() function. The function divides the dataset into frames of size 60. For each window size the mode of y values are taken and assigned to a window frame of 60 x values. 
So for every 60 readings of x readings there is one label given to it.

To handle the class imbalances we are using the compute_sample_weight function to find out the weights of each class depending on their individual frequencies. 


                                    Model

The model consists of an input layer which is a Bidirectional LSTM and an output layer which is a Dense layer with softmax as its activation function. The hidden layers consists of a Birectional LSTM layer and a Dense layer with relu as its activation function.
The model uses adam optimizer and categorical_loss_entrpoy as its loss function. This model is trained with the dataset generated earlier.

                                Data allocation

Dataset used for training : All subjects except 6
Dataset used for testing : subject 6. 
In the code provided we used all the available data for training, if needed please update this section.


                                Output generation

The model then generates the output file for subjects 9 - 12 given for the project. For generating the output file, the given data is divided into frames of size 60 as we did for training and is given to the model. The output of the model are a bunch of probabilities for each class. The highest probability among them is found and the corresponding label is assigned to each datapoint. To match the output frequency, for every 4 x_values a single y value is assigned. The generated output dataframe is saved as a csv file for each subject.  


Please run all the cells in the presented order. The trained model "model_4.keras" is attached to this file if quick output generation is needed.
