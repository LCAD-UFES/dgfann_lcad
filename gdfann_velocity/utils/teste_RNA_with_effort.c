#include <stdio.h>
#include <unistd.h>
#include <fann.h>
#include <math.h>

int 
main(int argc, char **argv)
{
	fann_type *calc_out;
	unsigned int i, j;
	struct fann *ann;
	struct fann_train_data *data;
    float error = 0.0;

	if (argc < 3) 
	{
		fprintf(stderr, "Use: %s FANN_network.net patternsFile\n", argv[0]); 
		exit(1);
	}

	printf("Openning ANN `%s'\n", argv[1]);
	ann = fann_create_from_file(argv[1]);

	if (!ann)
	{
		fprintf(stderr, "Error creating the ANN.\n"); 
		return (1); 
	}

	printf("Running ANN.\n");

	data = fann_read_train_from_file(argv[2]);

	for(i = 0; i < fann_length_train_data(data); i++)
	{

		calc_out = fann_run(ann, data->input[i]);
        
		printf("ANN: %f ", calc_out[0]);
		printf("Expected: %f ", data->output[i][0]);
		printf("Error: %f ", (float) (data->output[i][0] -calc_out[0]));
        printf("Throttle_Effort: %f Brake_Effort: %f Current_Velocity: %f\n", data->input[i][360-3], data->input[i][360-2], data->input[i][360-1]);
        error += (float) powf(fann_abs(calc_out[0] - data->output[i][0]),2);
	}

    printf("Test:: Squared Error: %f Mean Squared Error: %f\n", error, error/(fann_length_train_data(data)-1));

	printf("Cleaning memory.\n");
	fann_destroy_train(data);
	fann_destroy(ann);

	return (0);
}
