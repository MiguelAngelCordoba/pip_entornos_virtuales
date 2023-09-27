from matplotlib import pyplot

def generacion_plot():
    llaves = ["estudio","trabajo","deporte"]
    valores = [60,20,20]

    fig, ax = pyplot.subplots()
    ax.pie(valores, labels=llaves)
    #pyplot.show()  # para solo verla una vez
    pyplot.savefig("fig1.png")
    pyplot.close() 