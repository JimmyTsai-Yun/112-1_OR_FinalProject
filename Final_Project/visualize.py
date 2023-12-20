import matplotlib.pyplot as plt

def plot_location_of_each_station(data, result_path):
    
    result_path = result_path + '/Location of Each Station.png'
    
    # 繪製臺大各站點位置
    for i in range(len(data)):
        if '管理學院二館北側' in data[i]['sna']:
            plt.scatter(data[i]['lng'], data[i]['lat'], c='r', s=5)
        elif '綜合體育館停車場前' in data[i]['sna']:
            plt.scatter(data[i]['lng'], data[i]['lat'], c='g', s=5)
        else:
            plt.scatter(data[i]['lng'], data[i]['lat'], c='b', s=5)
    plt.title('Location of Each Station')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.savefig(result_path)
    pass