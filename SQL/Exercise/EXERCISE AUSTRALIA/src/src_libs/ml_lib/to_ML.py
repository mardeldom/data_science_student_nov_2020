def encoder(label):
    le = preprocessing.LabelEncoder()
    le.fit(label)
    lb= le.transform(label)
    return lb

def normalize(x):
    scaler = MinMaxScaler() 
    scaler.fit(x)
    x_normalized = scaler.transform(x)
    return x_normalized


