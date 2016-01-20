# dgfann_lcad

## Simulating Robotic Cars Using Multi-Layer Neural Networks

We proposed a simulator for robotic cars based on two multi-layer recurrent neural networks [1]. These networks are intended to simulate the mechanisms that govern how a set of effort commands changes the car’s velocity and the direction it is moving. The first neural network receives as input a temporal sequence of current and previous throttle and brake efforts, along with a temporal sequence of the previous car’s velocities (estimated by the network), and outputs the velocity that the real car would achieve in the next time interval given these inputs. The second neural network estimates the arctangent of curvature (a variable related to the steering wheel angle) that a real car would reach in the next time interval given a temporal sequence of current and previous steering efforts and previous arctangents of curvatures of the car. 
We have built and used a genetic algorithm framework for optimizing the configuration (number of layers, neuron types, number of neurons, etc.) of the neural networks that comprise the simulator.
We evaluated the performance of our simulator using real-world datasets acquired using an autonomous robotic car (Fig. 1). Experimental results showed that our simulator was able to simulate in real time how a set of efforts influences the car’s velocity and arctangent of curvature. While navigating in a map of a real-world environment, our car simulator was able to emulate the velocity and arctangent of curvature of the real car with mean squared error of 2.2x10^-3 (m/s)2 and 4.0x10^-5 rad^2, respectively.

![alt text](IARA.jpg)

**Fig. 1.	Intelligent and Autonomous Robotic Automobile (IARA), the robotic car platform simulated in this work (see it operating autonomously at https://youtu.be/LBM--2dAvyI).**

## Installing dgfann

This project was used by LCAD to create the Neural Networks employed in the LCAD Robot Simulator [1].

Note: The original project is from https://github.com/jeiks/gdfann

## Data sets employed in [1]

We have used IARA to collect samples for the training and test datasets, Tv and Tc (see sections III.B and III.C). For that, we have set IARA to run autonomously in typical operating situations and logged data according with Tv and Tc descriptions, with k = 120 for Tv and k = 40 for Tc. The number of input-output pairs, n, collected for Tv was equal to 5,369, and for Tc was equal to 7,686. After data collection, each dataset was shuffled and split into two parts, (a) and (b), where (a) received 1/3 of the samples and (b) 2/3 of the samples. Part (a) was used as the test set, while part (b) was divided into the training (2/3 of (b)), and validation (1/3 of (b)) sets. 

TODO: descrever os datasets (tamanho e formato).

## How to use the dgfann to find configurations of neural networks (NN) and train these NNs

## How to run your NNs and see the results

## Additional data and experiments

## References
[1] Alberto F. De Souza, Jacson Rodrigues Correia da Silva, Filipe Mutz, Claudine Badue, Thiago Oliveira-Santos, "Simulating Robotic Cars Using Multi-Layer Neural Networks", submitted to IJCNN'2016.
