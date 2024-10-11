import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)


filenames = [f'./file {i}.txt' for i in range(1,5)]

#start = datetime.datetime.now()
#for name in filenames:
#    read_info(name)
#end = datetime.datetime.now()
#print(end - start)


if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end = datetime.datetime.now()
    print(end - start)