import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import json
import sys
from sklearn.metrics import roc_auc_score
from data_loader import TrainDataLoader, ValTestDataLoader
from model import Net


# can be changed according to config.txt
exer_n = 17746
knowledge_n = 123
student_n = 4163
# can be changed according to command parameter
device = torch.device(('cuda:0') if torch.cuda.is_available() else 'cpu')
epoch_n = 5


def train():
    data_loader = TrainDataLoader() #utility for converting json files into useable data
    net = Net(student_n, exer_n, knowledge_n) #imports the Net Class from model.py

    net = net.to(device)
    optimizer = optim.Adam(net.parameters(), lr=0.002)
    print('training model...')

    loss_function = nn.NLLLoss() #negative log likelihood loss
    for epoch in range(epoch_n):
        data_loader.reset() #sets the pointer of the data loader to 0 
        running_loss = 0.0
        batch_count = 0
        while not data_loader.is_end(): #iterate through the batches ends when the data loaders pointer reaches the end of the data
            batch_count += 1
            input_stu_ids, input_exer_ids, input_knowledge_embs, labels = data_loader.next_batch()
            input_stu_ids, input_exer_ids, input_knowledge_embs, labels = input_stu_ids.to(device), input_exer_ids.to(device), input_knowledge_embs.to(device), labels.to(device)
            optimizer.zero_grad() #zeros gradient accumulated from previous passes
            output_1 = net.forward(input_stu_ids, input_exer_ids, input_knowledge_embs) #passing input values through model and layers to predict the probability of a correct response
            output_0 = torch.ones(output_1.size()).to(device) - output_1 # inverts output_1 to predict the probability of an incorrect response
            output = torch.cat((output_0, output_1), 1) #combines the two outputs into a single tensor with 2 columns

            # grad_penalty = 0
            loss = loss_function(torch.log(output), labels) #computation of loss for this batch
            loss.backward()
            optimizer.step()
            net.apply_clipper()

            running_loss += loss.item()
            if batch_count % 200 == 199:
                print('[%d, %5d] loss: %.3f' % (epoch + 1, batch_count + 1, running_loss / 200)) #print statement that appears periodically during training
                running_loss = 0.0
        #end of batch while loop

        # validate and save current model every epoch
        rmse, auc = validate(net, epoch)
        save_snapshot(net, 'model/model_epoch' + str(epoch + 1)) #outputs a snapshot to the model forlder


def validate(model, epoch):
    data_loader = ValTestDataLoader('validation') # utility for converting json validation data to useable form. Validation parameter specifies different from test
    net = Net(student_n, exer_n, knowledge_n)
    print('validating model...')
    data_loader.reset() # sets pointer to 0 in data loader
    # load model parameters
    net.load_state_dict(model.state_dict())
    net = net.to(device)
    net.eval() # evaluates the model

    correct_count, exer_count = 0, 0
    batch_count, batch_avg_loss = 0, 0.0
    pred_all, label_all = [], []
    while not data_loader.is_end():
        batch_count += 1
        input_stu_ids, input_exer_ids, input_knowledge_embs, labels = data_loader.next_batch() # receive data from data loader
        input_stu_ids, input_exer_ids, input_knowledge_embs, labels = input_stu_ids.to(device), input_exer_ids.to(
            device), input_knowledge_embs.to(device), labels.to(device) # format loaded data for use on device
        output = net.forward(input_stu_ids, input_exer_ids, input_knowledge_embs) # pass loaded data to the model
        output = output.view(-1)
        # compute accuracy
        for i in range(len(labels)): #compares model generated values in "output" variable to the correct labels to determine accuracy
            if (labels[i] == 1 and output[i] > 0.5) or (labels[i] == 0 and output[i] < 0.5):
                correct_count += 1
        exer_count += len(labels)
        pred_all += output.to(torch.device('cpu')).tolist()
        label_all += labels.to(torch.device('cpu')).tolist()

    pred_all = np.array(pred_all)
    label_all = np.array(label_all)
    # compute accuracy
    accuracy = correct_count / exer_count
    # compute RMSE
    rmse = np.sqrt(np.mean((label_all - pred_all) ** 2))
    # compute AUC
    auc = roc_auc_score(label_all, pred_all)
    print('epoch= %d, accuracy= %f, rmse= %f, auc= %f' % (epoch+1, accuracy, rmse, auc))
    with open('result/model_val.txt', 'a', encoding='utf8') as f:
        f.write('epoch= %d, accuracy= %f, rmse= %f, auc= %f\n' % (epoch+1, accuracy, rmse, auc))

    return rmse, auc


def save_snapshot(model, filename): #utility to save snapshots of the model throughout training
    f = open(filename, 'wb')
    torch.save(model.state_dict(), f)
    f.close()


if __name__ == '__main__': #used for providing feedback on the command line
    if (len(sys.argv) != 3) or ((sys.argv[1] != 'cpu') and ('cuda:' not in sys.argv[1])) or (not sys.argv[2].isdigit()):
        print('command:\n\tpython train.py {device} {epoch}\nexample:\n\tpython train.py cuda:0 70')
        exit(1)
    else:
        device = torch.device(sys.argv[1])
        epoch_n = int(sys.argv[2])

    # global student_n, exer_n, knowledge_n, device
    with open('config.txt') as i_f:
        i_f.readline()
        student_n, exer_n, knowledge_n = list(map(eval, i_f.readline().split(',')))

    train()
