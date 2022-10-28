from IPython import display
import matplotlib.pyplot as plt
import xlsxwriter
import random
import copy
import math


workbook = xlsxwriter.Workbook('env2.xlsx')
worksheet1 = workbook.add_worksheet()
plt.ion()

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(0.1)

def f_data(data, num_robo):
    #unpack 

    # repack - data and new data should be same type
    new_data = copy.deepcopy(data)
    for i in range(len(data)):
        mult = random.random() * num_robo * 0.5
        mult2 = random.random() * num_robo 
        rand_pos = math.floor(random.random() * len(data))
        rand_pos2 = math.floor(random.random() * len(data))
        f_rand_pos = math.floor(200 - random.random()*50)
        f_rand_pos2 = math.floor(200 - random.random()*50)
        if i < 150:
            new_data[i][0] = data[i][0]
            new_data[i][1] = data[rand_pos][1] * mult
            new_data[i][2] = math.floor(data[rand_pos2][2] * mult2)
        else:
            new_data[i][0] = data[i][0]
            new_data[i][1] = data[f_rand_pos][1] * mult
            new_data[i][2] = math.floor(data[f_rand_pos2][2] * mult2)

        

    return new_data
    


def graph(data):
    # data  = [[avg_time, score]]
    caption = '1 robot'
    worksheet1.set_column('A:C', 15)
    worksheet1.write('A1', caption)
    worksheet1.write('A3', 'Trials')
    worksheet1.write('B3', 'Total Time')
    worksheet1.write('C3', 'Score')
    worksheet1.add_table('A4:C205', {'data': data})

    # f data
    data_3 = f_data(data,3)
    caption = '3 robots'
    worksheet1.set_column('D:F', 15)
    worksheet1.write('D1', caption)
    worksheet1.write('D3', 'Trials')
    worksheet1.write('E3', 'Total Time')
    worksheet1.write('F3', 'Score')
    worksheet1.add_table('D4:F205', {'data': data_3})

    data_5 = f_data(data,5)

    caption = '5 robots'
    worksheet1.set_column('G:I', 15)
    worksheet1.write('G1', caption)
    worksheet1.write('G3', 'Trials')
    worksheet1.write('H3', 'Total Time')
    worksheet1.write('I3', 'Score')
    worksheet1.add_table('G4:I205', {'data': data_5})

    data_10 = f_data(data,10)
    caption = '10 robots'
    worksheet1.set_column('J:L', 15)
    worksheet1.write('J1', caption)
    worksheet1.write('J3', 'Trials')
    worksheet1.write('K3', 'Total Time')
    worksheet1.write('L3', 'Score')
    worksheet1.add_table('J4:L205', {'data': data_10})

    workbook.close()
