from bokeh.plotting import output_file, save, figure
from selenium import webdriver
from EntityClass import EntityClass
plots = dict()

def prepare_plots(entities):
    done = []
    for i in entities:
        if i.id not in done:
            plots[i.id] = webdriver.Chrome()
        done.append(i.id)

def plot(lines, id):
    #print(lines)
    output_file(id+".html",title=id)
    p = figure(plot_width=600,plot_height=600)
    x_axis_values = []
    for line in lines:
        x_axis_values.append(list(range(0, len(line)-1)))
    p.multi_line(xs = x_axis_values, ys = lines, color = ['blue','green','purple'])
    save(p)
    plots[id].get("file:///C:/Users/Prism/Desktop/Priyank/csp5/"+id+".html")
    #plots[id].navigate().to("file:///C:/Users/Prism/Desktop/Priyank/csp5/"+id+".html")




