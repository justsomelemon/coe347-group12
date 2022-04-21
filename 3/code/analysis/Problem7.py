def main():
    import matplotlib.pyplot as plt

    # ------------------- DATA PARSING -------------------
    path = "/home/mandy/Documents/Intro to CFD/OF 3/"  # File path to the file

    a = [32, 126]
    b = [1, 2, 4, 8, 16, 32, 64]    # P, number of processors
    Exec_time = []
    Clock_time = []
    speedup = []
    eighty = [1*.8, 2*.8, 4*.8, 8*.8, 16*.8, 32*.8, 64*.8]
    sixty = [1*.6, 2*.6, 4*.6, 8*.6, 16*.6, 32*.6, 64*.6]



    for j in range(len(a)):

        Exec_time.append([])
        Clock_time.append([])
        speedup.append([])

        for i in range(len(b)):
            file_name = str(a[j]) + '_' + str(b[i])  # File name
            data = path + file_name

            # read the file into a list of lines
            with open(data, 'r') as f:
                lines = f.read().split("\n")

            Exec_time[j].append([])
            Clock_time[j].append([])

            word = 'ExecutionTime'

            for k, line in enumerate(lines):
                if word in line:
                    line = line.split()
                    Exec_time[j][i].append(float(line[2]))
                    Clock_time[j][i].append(float(line[6]))

            speedup[j].append((Exec_time[j][0][-1]/len(Exec_time[j][0]))/(Exec_time[j][i][-1]/len(Exec_time[j][i])))

            f.close()

    # Make Graphs!
    plt.figure(figsize=(8, 6))
    plt.plot(b, speedup[0], 'r')
    plt.plot(b, b, 'k')
    plt.plot(b, eighty, '--k')
    plt.plot(b, sixty, '--b')
    plt.ylabel('Speed-up,T(1)/T(P)')
    plt.xlabel('Number of processors, P')
    plt.title('η = P^(−1) T(1)/T(P) Case ' + str(a[0]))
    plt.legend(['Actual (1 M cells)', 'Ideal', '80% Efficient', '60% Efficient'])
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.plot(b, speedup[1], 'r')
    plt.plot(b, b, 'k')
    plt.plot(b, eighty, '--k')
    plt.plot(b, sixty, '--b')
    plt.ylabel('Speed-up,T(1)/T(P)')
    plt.xlabel('Number of processors, P')
    plt.title('η = P^(−1) T(1)/T(P) Case ' + str(a[1]))
    plt.legend(['Actual (1 M cells)', 'Ideal', '80% Efficient', '60% Efficient'])
    plt.show()

    return


main()
