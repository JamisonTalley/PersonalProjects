# GroundUpSGD.py
# Jamison Talley
# 2024-03-17

import numpy as np
import matplotlib.pyplot as plt

class myNeuralNetwork(object):
    def __init__(self, n_in=2, n_layer1=5, n_layer2=5, n_out=1, learning_rate=0.1, batch_size = 20):
        # initialize the hyperparameters of the network
        self.n_in = n_in
        self.n_layer1 = n_layer1
        self.n_layer2 = n_layer2
        self.n_out = n_out
        self.learning_rate = learning_rate
        shape = [n_in,n_layer1,n_layer2,n_out]
        
        # initialize the data structure for storing the weights, pre-activations,
        # activations, and delta values
        self.weights = []
        self.F = []
        self.H = []
        self.Delta = []
        for i1 in range(len(shape) - 1):
            self.weights.append(np.ones((shape[i1] + 1,shape[i1 + 1])))
            self.F.append(np.zeros((shape[i1] + 1)))
            self.H.append(np.zeros((shape[i1] + 1)))
            self.Delta.append(np.zeros((shape[i1 + 1] + 1)))

        # Use He initialization to fill the weights tensor
        self.opt_weights(shape)

        # calculate the number of weights in the network
        self.n_weights = 0
        for i1 in range(len(self.weights)):
            shape = np.shape(self.weights[i1])
            self.n_weights += shape[0] * shape[1]
        self.batch_size = min(batch_size, self.n_weights)

    # He initialization for network weights
    def opt_weights(self,shape):
        for i1 in range(len(self.weights)):
            variance = 4.0 / (shape[i1] + shape[i1 + 1])
            for i2 in range(len(self.weights[i1])):
                self.weights[i1][i2] = np.random.normal(0,variance,len(self.weights[i1][i2]))
        return None
    
    # takes a scalar between 0 and self.n_weights, and returns the index of that weight
    # in self.weights. Returns False if the number is out of bounds of self.weights
    def ravel(self,weight_number):
        counter = 0
        for i1 in range(len(self.weights)):
            for i2 in range(len(self.weights[i1])):
                for i3 in range(len(self.weights[i1][i2])):
                    if counter == weight_number:
                        return [i1,i2,i3]
                    counter += 1
        return False

    # does a forward pass through the network with some input vector, x, while
    # recording the pre and post activation values in self.F and self.H respectively
    def forward_propagation(self, x):
        self.F[0] = np.insert(np.copy(x),0,1.0)
        self.H[0] = np.insert(np.copy(x),0,1.0)
        for i1 in range(len(self.weights) - 1):
            self.F[i1 + 1] = np.insert(np.matmul(self.H[i1],self.weights[i1]),0,1.0)
            for i2 in range(len(self.F[i1+1])):
                if self.F[i1+1][i2] < 0:
                    self.H[i1+1][i2] = 0.0
                else:
                    self.H[i1+1][i2] = self.F[i1+1][i2]
        y_hat = np.matmul(self.H[-1], self.weights[-1])
        return y_hat

    # computes the mean squared error loss
    def compute_loss(self, X, Y):
        loss = 0
        Y_hat = self.predict(X)
        for i1 in range(len(X)):
            loss += np.square(Y_hat[i1] - Y[i1]) / self.n_out
        return loss / len(X)

    # backpropogation pass that uses the activation and pre-activation values 
    # calculated in the forward_propagation step to calculate the Delta values
    # for each layer in the network for a given pair of input and output vectors
    def backpropagate(self, x, y):
        y_hat = self.forward_propagation(x)
        self.Delta[-1] = np.insert(y_hat - y,0,0)
        
        for i1 in range(len(self.Delta) - 2,-1,-1):
            for i2 in range(len(self.Delta[i1])):
                self.Delta[i1][i2] = (self.F[i1 + 1][i2] > 0) * np.dot(self.weights[i1 + 1][i2,:],self.Delta[i1 + 1][1:])
                
        return None

    # calls backpropagate at a point, and changes the values of the weights specified by
    # the array 'batch' accordingly
    def stochastic_gradient_descent_step(self, batch, x, y):
        self.backpropagate(x,y)
        for i1 in range(len(batch)):
            w = self.ravel(batch[i1])
            self.weights[w[0]][w[1],w[2]] -= self.learning_rate * self.Delta[w[0]][w[2] + 1] * self.H[w[0]][w[1]]
        
        return None

    # performs stochastic gradent decent on the model for a given training data set: X and Y
    def fit(self, X, Y, max_epochs, X_test=[],Y_test=[]):
        self.Losses_train = []
        self.Losses_test = []
        for i1 in range(max_epochs):
            for i2 in range(len(X)):
                # create a random subset of the weights to use in the SGD step
                batch_order = np.arange(self.n_weights)
                np.random.shuffle(batch_order)
                batch = np.copy(batch_order)[0:self.batch_size]
                # perform SGD step
                self.stochastic_gradient_descent_step(batch, X[i2],Y[i2])
            
            # record the loss against the training and testing data sets at each epoch
            self.Losses_train.append(self.compute_loss(self.predict(X),Y))
            self.Losses_test.append(self.compute_loss(self.predict(X_test),Y_test))
        return None

    def predict(self, X):
        # return the model's prediction for every input vector in X
        y_hat = np.zeros(len(X))
        for i1 in range(len(X)):
            y_hat[i1] = self.forward_propagation(X[i1])
        return y_hat

def main():
    # create data
    def makeSincData(n,noise=0.03):
        x = np.random.uniform(-6,6,n)
        y = np.sinc(np.sqrt((x)**2))+np.random.normal(0, noise, n)
        return (x,y)

    n = 500
    noise = 0.001
    x_train,y_train = makeSincData(n, noise)
    x_val,y_val = makeSincData(n, noise)
    x_test,y_test = makeSincData(n, noise)

    # train the model
    my_net = myNeuralNetwork(n_in=1,n_layer1=10,n_layer2=10,n_out=1,learning_rate=0.01,batch_size=20)
    my_net.fit(X=x_train,Y=y_train,max_epochs=500,X_test=x_test,Y_test=y_test)
    
    # plot the performance of the model
    epochs = range(500)
    x_vis = np.linspace(-6,6,100)
    y_vis = my_net.predict(x_vis)
    fig, (ax1,ax2) = plt.subplots(1,2,figsize=(14,6))
    ax1.plot(x_vis,y_vis, color="red", label="Trained Model")
    ax1.scatter(x_train,y_train, color="blue", label="Training Data")
    ax1.set_xlabel("Input")
    ax1.set_ylabel("Output")
    ax1.legend()
    print("Mean Squared Error: ",my_net.compute_loss(X=x_test,Y=y_test))

    my_net.Losses_train.reverse()
    my_net.Losses_test.reverse()
    ax2.plot(epochs,my_net.Losses_train, color = 'orange',label='Training Loss')
    ax2.plot(epochs,my_net.Losses_test, color = 'green',label='Testing Loss')
    ax2.legend()
    ax2.set_xlabel("Epoch")
    ax2.set_ylabel("Loss")
    plt.show()

if __name__ == '__main__':
    main()