# dgfann_lcad

dgfann is a Distributed Genetic Algorithm framework for optimizing the configuration (number of layers, neuron types, number of neurons, etc.) of the neural networks (NN). dgfann finds  the configurations of NNs and train them using fann (https://github.com/libfann/fann).

## Simulating Robotic Cars Using Multi-Layer Neural Networks

We proposed a simulator for robotic cars based on two multi-layer recurrent neural networks [1]. These networks are intended to simulate the mechanisms that govern how a set of effort commands changes the car’s velocity and the direction it is moving. The first neural network receives as input a temporal sequence of current and previous throttle and brake efforts, along with a temporal sequence of the previous car’s velocities (estimated by the network), and outputs the velocity that the real car would achieve in the next time interval given these inputs. The second neural network estimates the arctangent of curvature (a variable related to the steering wheel angle [1]) that a real car would reach in the next time interval given a temporal sequence of current and previous steering efforts and previous arctangents of curvatures of the car. 
We have built and used a genetic algorithm framework for optimizing the configuration (number of layers, neuron types, number of neurons, etc.) of the neural networks that comprise the simulator.
We evaluated the performance of our simulator using real-world datasets acquired using an autonomous robotic car (Fig. 1). Experimental results showed that our simulator was able to simulate in real time how a set of efforts influences the car’s velocity and arctangent of curvature. While navigating in a map of a real-world environment, our car simulator was able to emulate the velocity and arctangent of curvature of the real car with mean squared error of 2.2x10^-3 (m/s)2 and 4.0x10^-5 rad^2, respectively [1].

![alt text](IARA.jpg)

**Fig. 1.	Intelligent and Autonomous Robotic Automobile (IARA), the robotic car platform simulated in this work (see it operating autonomously at https://youtu.be/LBM--2dAvyI).**

## Installing dgfann

To install our genetic algorithm framework (dgfann) in Ubuntu:

* Install fann (http://leenissen.dk)
```sh
  sudo apt-get install libfann-dev
```
* Install dgfann
  * git clone https://github.com/LCAD-UFES/dgfann_lcad.git
  * sudo apt-get install python-jsonrpclib
  * sudo apt-get install gnuplot-x11

Note: An initial version of dgfann can be found at https://github.com/jeiks/gdfann

## Data sets employed in [1]

In [1], we have used IARA (Fig. 1, above) to collect samples for building a training and a test datasets, T<sub>v</sub> and T<sub>c</sub> (see sections III.B and III.C of [1]). For that, we have set IARA to run autonomously in typical operating situations and logged data according with T<sub>v</sub> and T<sub>c</sub> descriptions, with k = 120 for T<sub>v</sub> and k = 40 for T<sub>c</sub>. The number of input-output pairs, n, collected for T<sub>v</sub> was equal to 5,366, and for T<sub>c</sub> was equal to 7,683. After data collection, each dataset was shuffled and split into two parts, (a) and (b), where (a) received 1/3 of the samples and (b) 2/3 of the samples. Part (a) was used as the test sets, T<sub>v</sub><sup>te</sup> and T<sub>c</sub><sup>te</sup>, while part (b) was divided into the training (2/3 of (b)), T<sub>v</sub><sup>tr</sup> and T<sub>c</sub><sup>tr</sup>, and validation (1/3 of (b)), T<sub>v</sub><sup>va</sup> and T<sub>c</sub><sup>va</sup>, sets. 

These datasets are part of this repository:

- [T<sub>v</sub><sup>te</sup>](dgfann_velocity/entradas/testes.train)
- [T<sub>c</sub><sup>te</sup>](dgfann_aoc/entradas/testes.train)
- [T<sub>v</sub><sup>tr</sup>](dgfann_velocity/entradas/treino.train)
- [T<sub>c</sub><sup>tr</sup>](dgfann_aoc/entradas/treino.train)
- [T<sub>v</sub><sup>va</sup>](dgfann_velocity/entradas/validacao.train)
- [T<sub>c</sub><sup>va</sup>](dgfann_aoc/entradas/validacao.train)

All T<sub>v</sub> and T<sub>c</sub> datasets follow the format:

```
# Header: a line with three values: number of samples, network-input size, and network-output size
<number of samples> <network-input size> <network-output size>

# Samples: <number of samples> lines with <network-input size> values followed by <network-output size> values
<input 1> <input 2> ... <input <network-input size>> <output 1> <output 2> ... <output <network-output size>>
...
```

Where all T<sub>v</sub> datasets have \<network-input size\> equal to 360 and \<network-output size\> equal 1, while all T<sub>c</sub> datasets have \<network-input size\> equal to 80 and \<network-output size\> equal 1.

## How to use the dgfann to find configurations of neural networks (NN) and train these NNs

To use the dgfann to find configurations of neural networks (NN) and train these NNs follow the steps below. 

For running the genetic algorithm in a single machine to configure and train the Velocity neural network [1]:

1. Go to the directory of the Velocity neural network:
```sh
  cd dgfann_velocity
```
2. Set the parameters of this network in the file config.py
2. Create the datasets and the GA individual's evaluator:
```sh
  make
```
2. In RNAGenetico.py, make shure you have 'distribuido=False' 
3. Run GA with the command:
```sh
  ./RNAGenetico.py
```
3. When finished, if you ran it distributed, copy the dgfann folder from all nodes to master. Put all these folders in dgfann parent folder.
```
        Ex.: parent_folder/
                01-dgfann
                02-dgfann
                ...
                nn-dgfann
```
4. Now, inside master dgfann folder, you can get the Neural Networks created by the last population with the command:
```
  ./utils/01-copiar_redes.sh
```
5. Then, you can test these Neural Networks with test set and build the plots with:
```
    ./utils/02-gen_plots.sh
    # the plots will be placed in 'results_plots'
    # the neural outputs will be placed in 'results_ann'
```

For running the genetic algorithm in a cluster:


## How to run your NNs and see the results

## Additional data and experiments

## References

    [1] Alberto F. De Souza, Jacson Rodrigues Correia da Silva, Filipe Mutz, Claudine Badue, Thiago Oliveira-Santos, "Simulating Robotic Cars Using Multi-Layer Neural Networks", submitted to IJCNN'2016.
