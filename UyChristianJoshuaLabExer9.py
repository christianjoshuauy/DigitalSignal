import matplotlib.pyplot as plt

def plot_signal(signal, title):
    signal.append(signal[-1]) 
    plt.figure(figsize=(12, 2))
    plt.step(range(len(signal)), signal, where='post', linewidth=2)
    plt.title(title)
    plt.ylim(-2, 2)
    plt.yticks([-1, 0, 1])
    plt.grid(True)
    plt.show()

def nrz_l(data):
    signal = [1 if bit == '1' else -1 for bit in data]
    plot_signal(signal, "NRZ-L Encoding")
    return signal

def nrz_i(data, initial):
    signal = []
    level = initial
    for bit in data:
        if bit == '1':
            level = -level  
        signal.append(level)
    plot_signal(signal, "NRZ-I Encoding")
    return signal

def bipolar_ami(data, initial):
    signal = []
    last_level = -initial
    for bit in data:
        if bit == '1':
            signal.append(last_level)
            last_level = -last_level
        else:
            signal.append(0)
    plot_signal(signal, "Bipolar AMI Encoding")
    return signal

def pseudoternary(data, initial):
    signal = []
    last_level = -initial
    for bit in data:
        if bit == '0':
            signal.append(last_level)
            last_level = -last_level
        else:
            signal.append(0)
    plot_signal(signal, "Pseudoternary Encoding")
    return signal

def manchester(data):
    signal = []
    for bit in data:
        if bit == '0':
            signal.extend([1, -1])
        else:
            signal.extend([-1, 1])
    plot_signal(signal, "Manchester Encoding")
    return signal

def differential_manchester(data, initial):
    signal = []
    level = -initial
    for bit in data:
        if bit == '0':
            signal.extend([-level, level])
        else:
            level = -level
            signal.extend([-level, level])
    plot_signal(signal, "Differential Manchester Encoding")
    return signal

def main():
    is_initially_low = input("Is the initial level low? (y/n): ")
    if is_initially_low.lower() == 'y':
        initial = -1
        print("Initial level is low.")
    elif is_initially_low.lower() == 'n':
        initial = 1
        print("Initial level is high.")
    else:
        print("Invalid input. Assuming initial level is low.")

    data = input("Enter binary data (e.g., 1011001): ")
    if not set(data).issubset({'0', '1'}):
        print("Invalid input. Please enter binary data only.")
        return

    print("NRZ-L Signal: ", nrz_l(data))
    print("NRZ-I Signal: ", nrz_i(data, initial))
    print("Bipolar AMI Signal: ", bipolar_ami(data, initial))
    print("Pseudoternary Signal: ", pseudoternary(data, initial))
    print("Manchester Signal: ", manchester(data))
    print("Differential Manchester Signal: ", differential_manchester(data, initial))

if __name__ == "__main__":
    main()
